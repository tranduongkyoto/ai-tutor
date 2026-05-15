# Networking - AWS CSA Content Cache

## Services & Concepts

### Amazon VPC (Virtual Private Cloud)
- Isolated virtual network in AWS cloud; you define IP ranges, subnets, route tables, gateways
- Max 5 VPCs per region (soft limit, can be increased)
- Max 5 CIDR blocks per VPC; each CIDR: min /28 (16 IPs), max /16 (65,536 IPs)
- Only private IPv4 ranges allowed: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16
- VPC CIDR must NOT overlap with other networks (corporate, peered VPCs)
- Default VPC: exists in every account, has Internet connectivity, all EC2 get public IPv4, provides public and private DNS names

### CIDR (Classless Inter-Domain Routing)
- Two components: Base IP + Subnet Mask
- Subnet mask defines how many bits can change: /32=1 IP, /31=2, /30=4, /29=8, /28=16, /27=32, /26=64, /25=128, /24=256, /16=65,536, /0=all IPs
- /8 = 255.0.0.0, /16 = 255.255.0.0, /24 = 255.255.255.0, /32 = 255.255.255.255
- Private IP ranges (IANA): 10.0.0.0/8 (big networks), 172.16.0.0/12 (AWS default VPC range), 192.168.0.0/16 (home networks)
- All other IPs are public

### Subnets
- Tied to a single Availability Zone; define a CIDR within the VPC CIDR
- Public subnet: has route to Internet Gateway; Private subnet: no direct internet route
- AWS reserves 5 IPs per subnet (first 4 + last 1); example for 10.0.0.0/24:
  - 10.0.0.0 = Network address
  - 10.0.0.1 = VPC router (reserved by AWS)
  - 10.0.0.2 = Amazon-provided DNS (reserved by AWS)
  - 10.0.0.3 = Future use (reserved by AWS)
  - 10.0.0.255 = Broadcast (not supported, reserved)

### Internet Gateway (IGW)
- Allows VPC resources to connect to the Internet
- Horizontally scaled, highly available, redundant — managed by AWS
- Created separately from VPC; one VPC attaches to exactly one IGW (1:1 relationship)
- IGW alone does NOT give internet access — route tables must also be updated (add 0.0.0.0/0 → IGW)

### Route Tables
- Control where network traffic is directed from subnets
- Each subnet must be associated with a route table
- Public subnet route table: local route + 0.0.0.0/0 → IGW
- Private subnet route table: local route + 0.0.0.0/0 → NAT Gateway or NAT Instance

### Bastion Host
- EC2 instance in public subnet used to SSH into private EC2 instances
- Bastion SG: allow inbound SSH (port 22) from restricted CIDR (corporate public IP range only)
- Private instance SG: allow SSH from Bastion Host SG or Bastion's private IP
- Architecture: Internet → Bastion (public subnet) → SSH → private instances

### NAT Instance (Outdated — still on exam)
- EC2 instance that performs Network Address Translation for private subnet instances
- Must be in a public subnet; must have Elastic IP attached
- Must disable EC2 Source/Destination Check setting
- Route tables must route private subnet traffic to NAT Instance
- Not highly available out-of-box; need ASG + resilient user-data script for HA
- Bandwidth depends on EC2 instance type; you manage Security Groups
- Pre-configured Amazon Linux AMI reached end of support Dec 31, 2020

### NAT Gateway (NATGW)
- AWS-managed NAT; higher bandwidth, HA within AZ, no administration needed
- Created in specific AZ with Elastic IP; pay per hour + per GB data
- Starting bandwidth: 5 Gbps; auto-scales up to 100 Gbps
- Cannot be used by EC2 in the SAME subnet (only from other subnets)
- Traffic path: Private Subnet → NATGW (public subnet) → IGW → Internet
- No Security Groups to manage
- For HA across AZs: create one NATGW per AZ — no cross-AZ failover needed (if AZ goes down, no NAT needed)

### Regional NAT Gateway (RNAT)
- Highly available NAT Gateway associated with the VPC (not a single AZ)
- Has its own route tables; eliminates need for per-AZ deployments
- No Public Subnets needed to host RNAT
- Automatically detects resources in new AZ and expands

### Network ACL (NACL)
- Stateless firewall at the subnet level (applies to all instances in subnet automatically)
- One NACL per subnet; new subnets assigned Default NACL
- Supports both ALLOW and DENY rules
- Rules numbered 1–32766; lower number = higher precedence; first match wins
- Last rule is asterisk (*) = implicit DENY if no rule matches
- AWS recommends numbering rules in increments of 100
- Newly created custom NACLs deny all traffic by default
- Default NACL: allows all inbound and outbound (do NOT modify — create custom NACLs instead)
- Stateless: return traffic must be explicitly allowed (must handle ephemeral ports)
- Use NACLs to block specific IP addresses at subnet level

### Ephemeral Ports
- Clients connect to defined port, respond on a random ephemeral port
- IANA & MS Windows 10: ports 49152–65535
- Linux kernels: ports 32768–60999
- NACL rules must allow inbound/outbound on ephemeral port ranges for return traffic
- Example: web tier NACL must allow outbound TCP 1024–65535 to DB subnet for DB responses

### Security Groups
- Stateful firewall at EC2 instance level (return traffic automatically allowed)
- Supports ALLOW rules only (no DENY)
- All rules evaluated before decision; applies only when explicitly assigned to instance

### Security Group vs NACL Comparison
| Feature | Security Group | NACL |
|---------|---------------|------|
| Level | Instance | Subnet |
| Rules | Allow only | Allow + Deny |
| State | Stateful | Stateless |
| Rule evaluation | All rules evaluated | First match wins |
| Application | Assigned explicitly | Auto to all instances in subnet |

### VPC Peering
- Private connection between two VPCs using AWS network; behave as one network
- Must NOT have overlapping CIDRs
- NOT transitive: A-B and B-C does not give A-C connectivity (must create A-C separately)
- Can peer VPCs across different AWS accounts and regions
- Must update route tables in each VPC's subnets to enable EC2 communication
- Can reference security groups in peered VPC (same-region cross-account)

### VPC Endpoints (AWS PrivateLink)
- Connect to AWS services via private network instead of public Internet
- Remove the need for IGW, NATGW to access AWS services
- Redundant and scale horizontally
- Troubleshooting: check DNS Setting Resolution in VPC + Route Tables

**Interface Endpoints (PrivateLink)**
- Provisions ENI (private IP) as entry point; must attach Security Group
- Supports most AWS services
- Cost: $ per hour + $ per GB data processed
- Preferred when access is required from on-premises (S2S VPN/Direct Connect), different VPC, or different region

**Gateway Endpoints**
- Provisions a gateway used as target in route table (no Security Groups)
- Supports ONLY S3 and DynamoDB
- FREE
- Preferred for in-VPC access to S3/DynamoDB (most exam scenarios)

### VPC Flow Logs
- Capture IP traffic information at three levels: VPC, Subnet, ENI
- Destinations: Amazon S3, CloudWatch Logs, Kinesis Data Firehose
- Captures info from AWS managed interfaces too: ELB, RDS, ElastiCache, Redshift, WorkSpaces, NATGW, Transit Gateway
- Flow log record fields: version, account-id, interface-id, srcaddr, dstaddr, srcport, dstport, protocol, packets, bytes, start, end, action, log-status
- Use ACTION field to troubleshoot: Inbound REJECT = NACL or SG issue; Inbound ACCEPT + Outbound REJECT = NACL issue (stateless)
- Query with Amazon Athena (on S3) or CloudWatch Logs Insights
- IAM Role needs: logs:CreateLogGroup, logs:CreateLogStream, logs:PutLogEvents

**Flow Log Architecture Patterns**
- VPC Flow Logs → CloudWatch Logs → CloudWatch Contributor Insights → Top-10 IPs
- VPC Flow Logs → CloudWatch Logs → Metric Filter (SSH/RDP) → CW Alarm → SNS
- VPC Flow Logs → S3 → Athena → QuickSight

### AWS Site-to-Site VPN
- Encrypted VPN connection over public Internet between on-premises and VPC
- Components:
  - **Virtual Private Gateway (VGW)**: VPN concentrator on AWS side; attached to VPC; customizable ASN
  - **Customer Gateway (CGW)**: Software app or physical device on customer side
- Setup: enable Route Propagation for VGW in route table associated with subnets
- For ICMP ping from on-prem to EC2: add ICMP protocol to SG inbound rules
- If CGW behind NAT device with NAT-T enabled: use public IP of NAT device

### AWS VPN CloudHub
- Hub-and-spoke VPN model for multiple sites with multiple VPN connections
- Connect multiple Customer Gateways to same VGW with dynamic routing
- Traffic goes over public Internet (it is a VPN); low-cost solution
- Use case: primary or secondary connectivity between different office locations

### AWS Direct Connect (DX)
- Dedicated private physical connection from on-premises to AWS (bypasses public Internet)
- Setup requires connection between DC and AWS Direct Connect Location
- Requires Virtual Private Gateway on VPC
- Access public resources (S3) and private (EC2) on same connection
- Supports both IPv4 and IPv6
- Data in transit is NOT encrypted (private but not encrypted)
- For encryption: combine Direct Connect + VPN = IPsec-encrypted private connection
- Lead time: often longer than 1 month to establish

**Connection Types**
- Dedicated: 1 Gbps to 400 Gbps; physical ethernet port; request made to AWS first
- Hosted: 50 Mbps to 25 Gbps; via AWS Direct Connect Partners; capacity add/remove on demand

**Direct Connect Resiliency**
- High Resiliency: one connection at each of multiple DX locations
- Maximum Resiliency: separate connections on separate devices at multiple locations

**Direct Connect Gateway**
- Required when connecting to VPCs in multiple different regions (same account)
- Single DX connection → Direct Connect Gateway → VPCs in any region

### AWS VPN CloudHub vs Direct Connect
- CloudHub: VPN over public Internet, low-cost, hub-and-spoke, multiple sites
- Direct Connect: private dedicated line, consistent performance, higher bandwidth

### Transit Gateway
- Solves complex hub-and-spoke peering for thousands of VPCs and on-premises connections
- Regional resource; can work cross-region
- Share cross-account via Resource Access Manager (RAM)
- Can peer Transit Gateways across regions
- Route Tables control which VPCs can communicate
- Works with Direct Connect Gateway and VPN connections
- Only AWS service that supports IP Multicast
- Diagram: TGW sits centrally; multiple VPCs, VPN connections, and DX Gateway attach to it

**Transit Gateway ECMP (Equal-Cost Multi-Path)**
- Route strategy to forward packets over multiple best paths
- VPN to VGW: 1 VPN connection = 1.25 Gbps (2 tunnels)
- VPN to TGW with ECMP: 1 VPN = 2.5 Gbps, 2 VPNs = 5 Gbps, 3 VPNs = 7.5 Gbps
- Use case: increase VPN bandwidth to AWS by adding multiple S2S VPN connections
- Share Direct Connect between multiple accounts via TGW + RAM

### VPC Traffic Mirroring
- Capture and inspect network traffic in VPC without disrupting flow
- Source: ENIs; Target: ENI or Network Load Balancer
- Can filter (capture all or specific packets); can truncate packets
- Source and Target can be in same VPC or different VPCs (via VPC Peering)
- Use cases: content inspection, threat monitoring, troubleshooting

### IPv6 in VPC
- IPv6 addresses in AWS are ALL public and Internet-routable (no private range)
- IPv4 CANNOT be disabled for VPC/subnets — dual-stack mode only
- Enable IPv6 → EC2 gets private IPv4 + public IPv6
- IPv6 pool: 3.4 × 10^38 unique addresses; format x.x.x.x.x.x.x.x (hexadecimal)

**Egress-Only Internet Gateway**
- Used for IPv6 only (equivalent of NAT Gateway for IPv6)
- Allows outbound IPv6 connections; prevents Internet from initiating inbound IPv6 connections
- Must update Route Tables: ::/0 → Egress-only IGW (private subnet)

**IPv6 Routing**
- Public subnet route table: 0.0.0.0/0 → igw, ::/0 → igw
- Private subnet route table: 0.0.0.0/0 → nat-gateway, ::/0 → egress-only-igw

### AWS Network Firewall
- Protect entire VPC from Layer 3 to Layer 7
- Inspects traffic in any direction: VPC-to-VPC, outbound/inbound Internet, Direct Connect, S2S VPN
- Uses AWS Gateway Load Balancer internally
- Rules centrally managed cross-account via AWS Firewall Manager

**Fine-Grained Controls**
- IP & port filtering (up to 10,000s of IPs)
- Protocol filtering (e.g., block SMB outbound)
- Stateful domain list rules (e.g., only allow *.mycorp.com)
- Pattern matching with regex
- Traffic actions: Allow, Drop, or Alert
- Active flow inspection with intrusion-prevention capabilities
- Logs to S3, CloudWatch Logs, Kinesis Data Firehose

---

## Key Configurations

- **VPC per region**: 5 (soft limit)
- **CIDRs per VPC**: 5 max
- **Subnet CIDR min/max**: /28 to /16
- **Reserved IPs per subnet**: 5 (first 4 + last 1)
- **IGW per VPC**: 1 (1:1 relationship)
- **Default VPC**: 1 per region per account; CIDR 172.31.0.0/16; all subnets are public
- **NATGW bandwidth**: starts at 5 Gbps, auto-scales to 100 Gbps
- **NACL rules range**: 1–32766; add in increments of 100
- **Default NACL**: allows all traffic; do not modify, create custom instead
- **New custom NACL**: denies all traffic by default
- **NAT Instance**: must disable Source/Destination Check; needs Elastic IP
- **Route Propagation**: must enable for VGW in route tables for S2S VPN

---

## Architectural Patterns

### Standard 3-Tier VPC
- Public subnet: ALB, Bastion Host, NAT Gateway
- Private subnet (app tier): EC2 in Auto Scaling Group, Security Groups
- Private subnet (DB tier): RDS, ElastiCache
- NACLs on each subnet; Security Groups on each instance/service
- IGW at VPC boundary; Route tables route public subnet to IGW, private to NATGW

### High-Availability NAT Gateway
- Create one NAT Gateway per AZ (each in its own public subnet)
- Each AZ's private subnet routes to its local NATGW
- No cross-AZ failover needed: if AZ fails, no NAT needed for that AZ

### Hybrid Connectivity (On-Premises to AWS)
- **Option A: Site-to-Site VPN** — fast setup, over public Internet, encrypted, lower bandwidth
- **Option B: Direct Connect** — private dedicated line, consistent latency, higher bandwidth, >1 month setup
- **Option C: DX + VPN backup** — primary DX, failover S2S VPN connection
- **Option D: DX + VPN encryption** — use S2S VPN over DX for IPsec encryption

### Private Access to AWS Services
- **From within VPC**: Gateway Endpoint for S3/DynamoDB (free); Interface Endpoint for others
- **From on-premises via DX/VPN**: Interface Endpoint preferred (Gateway Endpoint not accessible from on-prem)
- **Lambda in VPC accessing DynamoDB**: Use Gateway Endpoint (free, better than NATGW + IGW)

### Multi-VPC Connectivity
- 2-3 VPCs: VPC Peering (non-transitive, individual connections)
- Many VPCs or on-prem: Transit Gateway (hub-and-spoke, transitive, supports thousands of VPCs)

### VPC Flow Log Analysis
- Security/threat analysis: Flow Logs → CloudWatch Logs → CW Contributor Insights
- Real-time alerting: Flow Logs → CW Logs → Metric Filter → CW Alarm → SNS
- Ad-hoc SQL analysis: Flow Logs → S3 → Athena → QuickSight

---

## Important Numbers & Limits

| Item | Value |
|------|-------|
| VPCs per region | 5 (soft limit) |
| CIDRs per VPC | 5 max |
| Min CIDR size | /28 (16 IPs) |
| Max CIDR size | /16 (65,536 IPs) |
| Reserved IPs per subnet | 5 (first 4 + last 1) |
| IGW per VPC | 1 |
| NATGW starting bandwidth | 5 Gbps |
| NATGW max bandwidth | 100 Gbps (auto-scaling) |
| NACL rule number range | 1–32,766 |
| NACL rule increment (recommended) | 100 |
| Ephemeral ports (Windows/IANA) | 49,152–65,535 |
| Ephemeral ports (Linux) | 32,768–60,999 |
| DX Dedicated connection speed | 1 Gbps – 400 Gbps |
| DX Hosted connection speed | 50 Mbps – 25 Gbps |
| DX setup lead time | > 1 month |
| VPN to VGW bandwidth | 1.25 Gbps per connection |
| VPN to TGW (ECMP) bandwidth | 2.5 Gbps per VPN connection |
| IPv4 addresses (total) | 4.3 Billion |
| IPv6 addresses (total) | 3.4 × 10^38 |

### Data Transfer Costs (Simplified)
| Traffic | Cost |
|---------|------|
| Inbound (ingress) | Free |
| Same AZ via private IP | Free |
| Cross-AZ via private IP | $0.01/GB |
| Cross-AZ via public/Elastic IP | $0.02/GB |
| Inter-region | $0.02/GB |
| S3 ingress | Free |
| S3 to Internet | $0.09/GB |
| S3 to CloudFront | $0.00/GB |
| CloudFront to Internet | $0.085/GB |
| S3 Cross-Region Replication | $0.02/GB |
| S3 Transfer Acceleration | +$0.04–$0.08/GB |
| NATGW per hour | $0.045 |
| NATGW data processed | $0.045/GB |
| Gateway VPC Endpoint | Free |
| S3 via Gateway Endpoint (same-region) | $0.01/GB in/out |

---

## Diagram Descriptions

### VPC Components Diagram (Full Architecture)
- Outermost: AWS Region containing VPC
- VPC contains: Internet Gateway (attached at VPC level), Router, Public Subnet (with NACL), Private Subnet (with NACL)
- Public Subnet: NAT Gateway (with Elastic IP), Route Table, EC2 instances in Security Groups
- Private Subnet: Route Table, EC2 instances in Security Groups
- Outside VPC: VPC Peering Connections, Transit Gateway, VPN/DX connections
- Right side: VPC Flow Logs → CloudWatch/S3; VPC Endpoint → S3/DynamoDB; VPN Gateway → Customer Gateway → Corporate Data Center → DX Location

### Bastion Host Diagram
- Users SSH to EC2 Bastion Host (public subnet, BastionHost-SG)
- Bastion Host SSH to multiple private EC2 instances (private subnet, LinuxInstance-SG)
- SG of private instances: allow SSH from Bastion's SG or Bastion's private IP

### NAT Gateway High Availability Diagram
- Two AZs: AZ-A has public subnet (NATGW) + private subnet (EC2); AZ-B same structure
- Both route through single Internet Gateway at top
- Private subnet in AZ-A routes to NATGW in AZ-A; AZ-B routes to its own NATGW
- If AZ-A fails (lightning bolt icon), AZ-B is unaffected

### Security Groups & NACLs Flow Diagram
- Incoming request: NACL inbound rules checked (stateless) → SG inbound rules → EC2 → SG outbound (stateful, auto-allow) → NACL outbound (stateless, must explicitly allow)
- Shows NACL is checked twice (in and out); SG return traffic automatically passes

### NACL with Ephemeral Ports Diagram
- Web subnet (public) ↔ DB subnet (private) via NACLs
- Web-NACL outbound: allow TCP port 3306 to DB subnet CIDR
- DB-NACL inbound: allow TCP port 3306 from Web subnet CIDR
- DB-NACL outbound: allow TCP ports 1024–65535 to Web subnet CIDR (ephemeral)
- Web-NACL inbound: allow TCP ports 1024–65535 from DB subnet CIDR (ephemeral)

### Direct Connect Diagram
- Corporate data center → Customer router/firewall → Customer or partner cage (VLAN) → AWS Direct Connect Endpoint (AWS Cage) → Virtual Private Gateway → VPC Private Subnet
- Blue line = Private virtual interface (to EC2/VPC)
- Green line = Public virtual interface (to S3, Glacier)

### Transit Gateway ECMP Throughput Diagram
- VPN to VGW: 1 VPN connection (2 tunnels) = 1.25 Gbps; connects to 1 VPC only
- VPN to TGW: 1 VPN = 2.5 Gbps, 2 VPNs = 5 Gbps, 3 VPNs = 7.5 Gbps; connects to multiple VPCs; + data processing cost per GB

### IPv6 Routing Diagram
- VPC with dual-stack (IPv4 10.0.0.0/16 + IPv6 2001:db8:1234:1a00::/56)
- Public subnet: web server with private IPv4 + EIP + IPv6; routes 0.0.0.0/0 and ::/0 to IGW
- Private subnet: server with private IPv4 + IPv6; routes 0.0.0.0/0 to NAT Gateway, ::/0 to Egress-only IGW

### NAT Gateway vs Interface Endpoint for S3
- Option 1 (expensive): Private EC2 → NATGW (public subnet) → IGW → Internet → S3
- Option 2 (free): Private EC2 → Gateway VPC Endpoint → S3 (stays within AWS network)

---

## Exam-Relevant Details

### Critical Distinctions

**NACL vs Security Group — common trap**
- NACL = stateless (must allow ephemeral ports explicitly for return traffic), subnet level, allow + deny
- SG = stateful (return traffic auto-allowed), instance level, allow only
- "Block a specific IP" → use NACL (SGs cannot deny, only allow)
- "Allow traffic from other SG" → use Security Group rules (not NACL)

**NAT Gateway vs NAT Instance**
- Exam prefers NAT Gateway for managed, scalable, HA solution
- NAT Instance: must disable source/dest check, needs Elastic IP, you manage SG, can be Bastion Host
- NAT Gateway: no SG management, cannot use as Bastion Host, HA within AZ, 5–100 Gbps

**Gateway Endpoint vs Interface Endpoint**
- Gateway = S3 or DynamoDB only; FREE; uses route table entry; preferred for in-VPC access
- Interface = most services; costs money; uses ENI; preferred for on-prem/cross-region access
- Exam almost always prefers Gateway Endpoint for S3/DynamoDB from within VPC

**Direct Connect vs Site-to-Site VPN**
- DX: private, dedicated, consistent, high bandwidth, >1 month setup, NOT encrypted by default
- S2S VPN: encrypted, over public Internet, quick setup, lower bandwidth
- DX + VPN = IPsec encrypted private connection (best of both)
- For DX failover → use S2S VPN as backup (cheaper than second DX)

**VPC Peering vs Transit Gateway**
- Peering: non-transitive, 1:1, works across accounts/regions, simpler for few VPCs
- TGW: transitive, hub-and-spoke, thousands of VPCs, supports IP Multicast (unique to TGW)
- "Transitive routing" keyword → Transit Gateway

**Egress-Only IGW vs NAT Gateway**
- Egress-Only IGW = IPv6 outbound only (like NAT for IPv6)
- NAT Gateway = IPv4 outbound only
- IPv6 addresses are all public — no concept of private IPv6 in AWS

### Important "Gotchas"

- IGW alone does NOT enable internet access — route table must have 0.0.0.0/0 → IGW
- NAT Gateway cannot be used by instances in the SAME subnet
- VPC Peering is NOT transitive (A↔B + B↔C ≠ A↔C)
- New NACL = deny all; Default NACL = allow all
- IPv4 CANNOT be disabled in VPC — dual-stack only
- If EC2 can't launch in subnet: cause is no available IPv4 (NOT IPv6); fix = add new IPv4 CIDR
- Direct Connect is private but NOT encrypted
- NATGW is resilient within one AZ only — need one NATGW per AZ for full HA
- Route Propagation must be enabled for S2S VPN to work with VGW
- Default VPC uses 172.31.0.0/16 range

### Keywords → Services
- "Private access to S3/DynamoDB from VPC" → Gateway VPC Endpoint (free)
- "Private access from on-premises to S3" → Interface VPC Endpoint
- "Block specific IP at subnet level" → NACL
- "Hub-and-spoke for many VPCs" → Transit Gateway
- "IP Multicast" → Transit Gateway (only service supporting it)
- "Dedicated private connection, consistent latency" → Direct Connect
- "Encrypted connection over private line" → Direct Connect + VPN
- "Connect multiple sites via VPN" → VPN CloudHub
- "SSH into private instances" → Bastion Host
- "IPv6 outbound only" → Egress-Only Internet Gateway
- "Capture and inspect VPC traffic" → Traffic Mirroring
- "Monitor IP traffic, troubleshoot connectivity" → VPC Flow Logs
- "Protect entire VPC, Layer 3-7" → AWS Network Firewall
- "Manage firewall rules across accounts" → AWS Firewall Manager
- "Transitive VPC peering" → Transit Gateway
- "NAT for private subnet, managed by AWS" → NAT Gateway
