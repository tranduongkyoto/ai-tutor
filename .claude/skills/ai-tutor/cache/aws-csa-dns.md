# DNS - AWS CSA Content Cache

## Services & Concepts

### DNS (Domain Name System)
- Translates human-friendly hostnames into machine IP addresses (e.g., www.google.com => 172.217.18.36)
- Backbone of the Internet; uses hierarchical naming structure
- Hierarchy: `.com` → `example.com` → `www.example.com` → `api.example.com`

### DNS Terminology
- **Domain Registrar**: Where you buy/register domain names — Amazon Route 53, GoDaddy, etc.
- **DNS Records**: A, AAAA, CNAME, NS, and more
- **Zone File**: Contains DNS records
- **Name Server**: Resolves DNS queries — Authoritative or Non-Authoritative
- **TLD (Top Level Domain)**: .com, .us, .in, .gov, .org
- **SLD (Second Level Domain)**: amazon.com, google.com
- **FQDN (Fully Qualified Domain Name)**: Full path — `http://api.www.example.com.` (includes root `.`)
- **Root**: Implicit `.` at end of every FQDN, managed by ICANN
- **Protocol**: http/https prefix before the domain

### Amazon Route 53
- Highly available, scalable, fully managed and **Authoritative** DNS
  - Authoritative = customer (you) can update the DNS records
- Also a **Domain Registrar** (can register domains directly)
- Ability to **health check** your resources
- **Only AWS service with 100% availability SLA**
- Name "53" refers to the traditional DNS port (port 53)

### Route 53 – Records
- Define how to route traffic for a domain
- Each record contains:
  - **Domain/subdomain Name** — e.g., example.com
  - **Record Type** — e.g., A, AAAA
  - **Value** — e.g., 12.34.56.78
  - **Routing Policy** — how Route 53 responds to queries
  - **TTL** — amount of time the record is cached at DNS Resolvers
- Must-know record types: **A / AAAA / CNAME / NS**
- Advanced record types: CAA / DS / MX / NAPTR / PTR / SOA / TXT / SPF / SRV

### Record Types
- **A** — maps hostname to IPv4
- **AAAA** — maps hostname to IPv6
- **CNAME** — maps hostname to another hostname
  - Target must have an A or AAAA record
  - **Cannot create CNAME for Zone Apex (root domain)** — e.g., can't do example.com, CAN do www.example.com
- **NS** — Name Servers for the Hosted Zone; control how traffic is routed for a domain

### Hosted Zones
- Container for records that define how to route traffic to a domain and its subdomains
- **Public Hosted Zones**: Records for routing traffic on the Internet (public domain names) — e.g., `application1.mypublicdomain.com`
- **Private Hosted Zones**: Records for routing traffic within one or more VPCs (private domain names) — e.g., `application1.company.internal`
- Cost: **$0.50 per month per hosted zone**

### Alias Records
- Route 53 extension to DNS functionality
- Maps hostname to an **AWS resource** (not just any hostname)
- Automatically recognizes changes in the resource's IP addresses (dynamic IPs handled transparently)
- Unlike CNAME, **can be used for the Zone Apex** (e.g., example.com)
- Always of type **A or AAAA** (IPv4/IPv6) for AWS resources
- **You cannot set TTL** on Alias records (Route 53 manages it)
- Free of charge; has native health check integration
- **Alias Record Targets**:
  - Elastic Load Balancers
  - CloudFront Distributions
  - API Gateway
  - Elastic Beanstalk environments
  - S3 Websites
  - VPC Interface Endpoints
  - Global Accelerator
  - Route 53 record in the same hosted zone
  - **Cannot target an EC2 DNS name**

### TTL (Time To Live)
- Amount of time client caches the DNS result
- **High TTL** (e.g., 24 hr): Less traffic to Route 53, possibly outdated records
- **Low TTL** (e.g., 60 sec): More Route 53 queries (higher cost), records outdated less time, easier to change records
- TTL is **mandatory for each DNS record except Alias records**

### Health Checks
- HTTP Health Checks are only for **public resources**
- Health Check enables Automated DNS Failover
- 3 types:
  1. **Monitor an endpoint** — application, server, or other AWS resource
  2. **Calculated Health Checks** — monitor other health checks (combine results)
  3. **CloudWatch Alarm-based** — monitor CloudWatch Alarms (useful for private resources)
- Health Checks integrated with CloudWatch metrics

### Health Checks – Monitor an Endpoint
- About **15 global health checkers** check endpoint health
- Healthy/Unhealthy threshold: **3** (default)
- Interval: **30 sec** (can set to 10 sec — higher cost)
- Supported protocols: **HTTP, HTTPS, TCP**
- If **> 18%** of health checkers report endpoint healthy → Route 53 considers it **Healthy**; otherwise **Unhealthy**
- Health Check passes when endpoint responds with **2xx or 3xx** status codes
- Can pass/fail based on text in the **first 5,120 bytes** of the response
- Must configure firewall/router to allow incoming requests from Route 53 Health Checker IP ranges
- Ability to choose which locations (regions) Route 53 uses for checks

### Calculated Health Checks
- Combine results of multiple child health checks into a single parent health check
- Logical operators: **OR, AND, NOT**
- Can monitor up to **256 Child Health Checks**
- Specify how many child checks need to pass for parent to pass
- Use case: perform maintenance without causing all health checks to fail

### Health Checks – Private Hosted Zones
- Route 53 health checkers are **outside the VPC** — cannot access private endpoints
- Workaround: Create a **CloudWatch Metric** + **CloudWatch Alarm**, then create a Health Check that monitors the CloudWatch Alarm

### Routing Policies
- Define how Route 53 **responds to DNS queries**
- DNS does NOT route traffic — it only responds to DNS queries (different from load balancer routing)
- Supported policies: **Simple, Weighted, Failover, Latency-based, Geolocation, Multi-Value Answer, Geoproximity, IP-based**

### Routing Policy – Simple
- Route traffic to a single resource
- Can specify multiple values in the same record
- If multiple values returned, **client chooses a random one**
- When Alias enabled, specify only one AWS resource
- **Cannot be associated with Health Checks**

### Routing Policy – Weighted
- Control % of requests going to each specific resource
- Formula: `traffic (%) = weight_for_record / sum_of_all_weights`
- Weights **don't need to sum to 100**
- DNS records must have the same name and type
- **Can be associated with Health Checks**
- Use cases: load balancing between regions, testing new application versions
- Assign weight **0** to stop sending traffic to a resource
- If **all records have weight 0**, all records returned equally

### Routing Policy – Latency-based
- Redirect to resource with **lowest latency** relative to user
- Latency based on traffic between users and **AWS Regions** (not geographic distance)
- Example: German users may go to US region if that has lowest latency
- **Can be associated with Health Checks** (failover capability)

### Routing Policy – Failover (Active-Passive)
- Primary record has **mandatory health check**
- If primary unhealthy → Route 53 returns secondary (disaster recovery) record
- Client → Route 53 → Primary EC2 (health-checked) / Secondary EC2 (DR fallback)

### Routing Policy – Geolocation
- Routing based on **user's location** (different from latency-based!)
- Specify location by Continent, Country, or US State (most precise match wins)
- Should create a **"Default" record** for no-match cases
- Use cases: website localization, restrict content distribution, load balancing
- **Can be associated with Health Checks**

### Routing Policy – Geoproximity
- Route traffic based on geographic location of **both users and resources**
- Ability to shift more traffic using **bias** values
  - Expand (1 to 99): more traffic to the resource
  - Shrink (-1 to -99): less traffic to the resource
- Resources: AWS resources (specify region) or non-AWS (specify latitude/longitude)
- **Must use Route 53 Traffic Flow** to use this feature

### Routing Policy – IP-based Routing
- Routing based on **clients' IP addresses**
- Provide a list of CIDRs for clients and corresponding endpoints/locations
- Use cases: optimize performance, reduce network costs, route ISP users to specific endpoints
- Uses CIDR Collections with mappings to record values

### Routing Policy – Multi-Value
- Use when routing to multiple resources
- Route 53 returns multiple values/resources
- **Can be associated with Health Checks** (returns only healthy resource values)
- Up to **8 healthy records** returned per Multi-Value query
- **NOT a substitute for ELB** — client-side load balancing only

### Domain Registrar vs. DNS Service
- Domain Registrar: where you buy the domain (GoDaddy, Amazon Registrar Inc.)
- DNS Service: where you manage DNS records (can be different from registrar)
- Example: buy domain from GoDaddy, use Route 53 to manage DNS records
- To use Route 53 as DNS for 3rd-party registrar domain:
  1. Create a Hosted Zone in Route 53
  2. Update NS Records at the 3rd-party registrar to use Route 53 Name Servers
- **Domain Registrar ≠ DNS Service** (but registrars usually include basic DNS features)

### Route 53 – Hybrid DNS
- By default, Route 53 Resolver automatically answers DNS queries for:
  - Local domain names for EC2 instances
  - Records in Private Hosted Zones
  - Records in public Name Servers
- **Hybrid DNS**: resolving DNS queries between VPC (Route 53 Resolver) and your on-premises networks (other DNS Resolvers)
- Networks: VPC itself / Peered VPC / On-premises (via Direct Connect or AWS VPN)

### Route 53 – Resolver Endpoints
- **Inbound Endpoint**: Allows your on-premises DNS Resolvers to resolve domain names for AWS resources (EC2 instances) and Private Hosted Zone records
  - On-premises server queries app.aws.private → on-premises DNS resolver → Inbound Endpoint in VPC → Route 53 Resolver → Private Hosted Zone
- **Outbound Endpoint**: Route 53 Resolver forwards DNS queries to your on-premises DNS Resolvers
  - EC2 instance queries web.onpremise.private → Route 53 Resolver → Outbound Endpoint in VPC → on-premises DNS Resolver
- Both use VPN or Direct Connect connection between VPC and on-premises data center


## Key Configurations

- **Hosted Zone cost**: $0.50/month per zone
- **Health check interval**: 30 sec default, 10 sec (higher cost option)
- **Health check threshold**: 3 (default healthy/unhealthy)
- **Health check quorum**: >18% of global health checkers must report healthy
- **Health check response inspection**: first 5,120 bytes of response body
- **Calculated Health Check max children**: 256 child checks
- **Multi-Value max records returned**: 8 healthy records per query
- **Weighted routing**: weights don't need to sum to 100; weight=0 stops traffic
- **Geoproximity bias range**: -99 to +99 (negative shrinks, positive expands region)
- **TTL**: mandatory on all records except Alias records
- **Alias records**: TTL not settable; cannot target EC2 DNS names
- **CNAME restriction**: cannot use at Zone Apex (root domain)
- **Alias advantage**: works at Zone Apex; free; auto-tracks resource IP changes


## Architectural Patterns

### Public Domain with AWS Resources
- Public Hosted Zone → A/Alias records pointing to EC2 (Public IP), ALB, CloudFront, S3 Website
- Use Alias for AWS resources (free, supports apex, auto IP tracking)
- Use CNAME only for non-AWS hostnames or subdomains

### Private Internal DNS (VPC)
- Private Hosted Zone associated with one or more VPCs
- EC2 instances resolve internal names (e.g., api.example.internal → 10.0.0.10)
- RDS instances accessible via internal DNS names (e.g., db.example.internal → 10.0.0.35)
- Health checks for private resources → use CloudWatch Alarm → Health Check monitors alarm

### Multi-Region Active-Active with Weighted
- Same record name, different values (IPs) with weights (e.g., 70/20/10)
- Use for gradual traffic shifting, blue-green deployments, canary testing
- Associate with health checks for automatic failover when weighted targets fail

### Multi-Region Active-Passive Failover
- Primary record with mandatory health check
- Secondary record as DR fallback
- Route 53 automatically switches to secondary when primary health check fails

### Global Low-Latency Routing
- Latency-based routing with one record per region
- Users automatically directed to closest-latency AWS region
- Combine with health checks for failover if a region becomes unhealthy

### Hybrid On-Premises + AWS DNS
- VPN or Direct Connect between on-premises and AWS VPC
- Inbound Endpoint: on-premises servers resolve AWS private hostnames
- Outbound Endpoint: AWS EC2 instances resolve on-premises hostnames
- Route 53 Resolver handles both directions

### 3rd-Party Registrar + Route 53 DNS
- Buy domain at GoDaddy/Namecheap
- Create Public Hosted Zone in Route 53
- Copy Route 53 NS record values into GoDaddy nameserver settings
- Route 53 now authoritative for the domain


## Important Numbers & Limits

| Item | Value |
|------|-------|
| Route 53 availability SLA | 100% |
| DNS port | 53 |
| Hosted zone cost | $0.50/month |
| Health check interval (default) | 30 seconds |
| Health check interval (fast) | 10 seconds (higher cost) |
| Health check threshold | 3 (default) |
| Health check quorum | >18% of global checkers |
| Global health checker count | ~15 |
| Response body inspection limit | 5,120 bytes (first N bytes) |
| Calculated Health Check max children | 256 |
| Multi-Value max records returned | 8 |
| Geoproximity bias expand range | 1 to 99 |
| Geoproximity bias shrink range | -1 to -99 |
| TTL example (high) | 24 hours |
| TTL example (low) | 60 seconds |


## Diagram Descriptions

### How DNS Works (Resolution Flow)
- Web browser (with CACHE/TTL) queries Local DNS Server for example.com
- Local DNS Server queries Root DNS Server (managed by ICANN) → returns .com NS at 1.2.3.4
- Local DNS Server queries TLD DNS Server (.com, managed by IANA branch of ICANN) → returns example.com NS at 5.6.7.8
- Local DNS Server queries SLD DNS Server (example.com, managed by Domain Registrar e.g., Amazon Registrar Inc.) → returns example.com IP 9.10.11.12
- Local DNS Server returns IP to browser; browser caches for TTL duration
- Browser makes HTTP request directly to Web Server at 9.10.11.12

### DNS Terminology URL Breakdown
- `http://api.www.example.com.`
  - `http://` = Protocol
  - `api.www` = Sub Domain
  - `example.com` = SLD
  - `.com` = TLD
  - `.` (trailing) = Root
  - Full path = FQDN

### Public vs. Private Hosted Zone Comparison
- **Public**: Client → Public Hosted Zone → routes to S3, CloudFront, EC2 (Public IP), ALB — all internet-accessible
- **Private**: Within VPC, EC2 instances query Private Hosted Zone for internal names like api.example.internal (10.0.0.10) and db.example.internal (10.0.0.35, RDS)

### TTL Flow
- Client queries Route 53 → gets A record 12.34.56.78 with TTL value
- Client caches result for TTL duration
- Client makes HTTP requests directly to web server
- During TTL period, no additional DNS queries needed

### Failover Routing Diagram
- Client → Route 53 (DNS Requests) → Health Check (mandatory) on Primary EC2
- If Primary healthy: traffic goes to Primary EC2
- If Primary unhealthy: failover activates → traffic goes to Secondary EC2 (Disaster Recovery)

### Geoproximity Bias Effect
- Diagram 1 (Bias 0/0): US split evenly at midpoint between us-west-1 and us-east-1 — equal traffic areas
- Diagram 2 (us-east-1 Bias: 50): Division line shifts westward — more users directed to us-east-1 (larger catchment area)

### Resolver Inbound Endpoint (Hybrid DNS)
- On-premises server (web.onpremise.private) queries app.aws.private
- On-premises DNS Resolvers forward query via VPN/DX to Resolver Inbound Endpoint in VPC private subnet
- Inbound Endpoint → Route 53 Resolver → Private Hosted Zone lookup → returns IP of EC2 (app.aws.private)

### Resolver Outbound Endpoint (Hybrid DNS)
- EC2 instance (app.aws.private) queries web.onpremise.private
- Route 53 Resolver → Resolver Outbound Endpoint in private subnet
- Outbound Endpoint forwards query via VPN/DX to on-premises DNS Resolvers (onpremise.private)
- Returns answer back to EC2 instance


## Exam-Relevant Details

### CNAME vs Alias — Critical Distinctions
| Feature | CNAME | Alias |
|---------|-------|-------|
| Zone Apex (root domain) | NOT allowed | Allowed |
| Target | Any hostname | AWS resources only |
| Cost | Charged per query | Free |
| TTL | You set it | Route 53 manages it |
| Health Check | No native | Yes (native) |
| EC2 DNS names | Yes | NO — not supported |

### Routing Policy — Key Distinguishing Factors
| Policy | Key Characteristic | Health Checks? |
|--------|-------------------|----------------|
| Simple | Single or random multi-value; no health check | No |
| Weighted | % control by weight ratio; weight=0 disables | Yes |
| Latency | Lowest latency to AWS Region (not geographic) | Yes |
| Failover | Active-Passive; mandatory health check on primary | Yes (required) |
| Geolocation | Based on WHERE user is (country/continent/state) | Yes |
| Geoproximity | Based on proximity + bias shift; requires Traffic Flow | No (needs Traffic Flow) |
| Multi-Value | Up to 8 healthy values; NOT a replacement for ELB | Yes |
| IP-based | CIDR-to-endpoint mapping | No |

### Common Exam Traps
- **Geolocation vs Latency-based**: Geolocation = WHERE user is (country). Latency = WHICH region is fastest. A German user might get US region with latency-based if it's faster.
- **CNAME at root domain**: Cannot do example.com CNAME, but CAN do www.example.com CNAME. Use Alias for root domain.
- **Alias cannot target EC2 DNS names** — this is the one AWS service excluded.
- **Multi-Value ≠ ELB**: Multi-Value is client-side selection from up to 8 healthy DNS responses. ELB actually routes and load balances TCP/HTTP connections.
- **Simple routing + multiple values**: Route 53 returns ALL values; the CLIENT randomly picks one. Route 53 does not pick.
- **Health Checks on private resources**: HTTP health checkers are outside VPC and can't reach private IPs. Use CloudWatch Alarm + health check on alarm.
- **TTL on Alias**: You cannot set TTL on Alias records — Route 53 controls it. TTL is mandatory on all other record types.
- **Domain Registrar ≠ DNS Service**: You can buy at GoDaddy and use Route 53 for DNS (or vice versa). They are separate concerns.
- **Weighted all-zeros**: If all weighted records have weight=0, all are returned equally (not zero traffic).
- **Route 53 is Authoritative DNS**: Means YOU control the records. Non-authoritative = caching resolver (ISP/local DNS).
- **100% SLA**: Route 53 is the only AWS service with 100% availability SLA — exam may test this.
- **Geoproximity requires Traffic Flow**: Cannot use Geoproximity routing without enabling the Traffic Flow feature.
- **Failover requires health check**: Health check on primary is mandatory, not optional, for Failover policy.
- **Inbound vs Outbound Resolver Endpoints**: Inbound = on-premises resolves AWS names INTO AWS. Outbound = AWS resolves on-premises names OUT to on-premises.

### Keywords That Signal Services
- "Highly available DNS" / "100% SLA" → Route 53
- "Route traffic based on user location" → Geolocation (not latency)
- "Lowest network latency" → Latency-based routing
- "Active-passive failover" / "disaster recovery DNS" → Failover routing
- "Blue-green deployment / canary testing via DNS" → Weighted routing
- "Shift traffic gradually using bias" → Geoproximity
- "Route users from specific ISP" → IP-based routing
- "Multiple healthy endpoints via DNS" → Multi-Value (remember: not ELB replacement)
- "Point apex/root domain to ALB/CloudFront" → Alias record
- "Private DNS inside VPC" → Private Hosted Zone
- "On-premises servers resolving AWS names" → Inbound Resolver Endpoint
- "AWS EC2 resolving on-premises hostnames" → Outbound Resolver Endpoint
- "Combine multiple health checks" → Calculated Health Checks
