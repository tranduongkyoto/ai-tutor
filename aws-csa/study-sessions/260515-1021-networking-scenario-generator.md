# Networking — Phase 3: Scenario Generator

*9 real-world scenarios mapped to SAA-C03 exam topics*
*Generated: 2026-05-15 10:21*

---

## Scenario 1: Multi-VPC Design

**Context:** A financial services company operates three business units — trading, compliance, and customer portal. Each requires network isolation for regulatory reasons, but all need access to a shared logging and monitoring Virtual Private Cloud (VPC). The company expects to add 5 more business-unit VPCs over the next 2 years.

**Requirements:** Strong network isolation between business units. Shared services accessible from all VPCs. Scalable to 8+ VPCs without exponential peering complexity. Minimize operational overhead.

**Question:** Which architecture meets these requirements?

A) Create individual VPC Peering connections between each business-unit VPC and the shared-services VPC, plus peering between each business-unit pair for cross-unit communication.

B) Deploy all business units in a single VPC using separate subnets and Network Access Control Lists (NACLs) for isolation. Route shared services through a dedicated subnet.

C) Use AWS Transit Gateway (TGW) as a central hub. Attach each business-unit VPC and the shared-services VPC. Use TGW route tables to allow shared-services access while blocking inter-business-unit traffic.

D) Deploy each business unit in a separate VPC and use AWS PrivateLink Interface Endpoints in each VPC to connect to services hosted in the shared-services VPC.

**Answer: C**
Transit Gateway provides hub-and-spoke connectivity with route table isolation. Each business-unit VPC attaches to TGW, and route tables are configured to allow routes only to the shared-services VPC — not between business units. Adding new VPCs requires only a new TGW attachment, scaling linearly.

**Why others are wrong:**
- A) VPC Peering is non-transitive and doesn't scale — with 8 VPCs you'd need 28 peering connections. Also, peering between business units violates the isolation requirement.
- B) A single VPC with NACLs provides weaker isolation than separate VPCs. NACLs can be misconfigured. Regulatory requirements typically mandate VPC-level separation for financial workloads.
- D) PrivateLink is for service-to-service connections, not general network connectivity. It would require creating endpoints for every service in the shared VPC and doesn't support arbitrary IP traffic between VPCs.

**Key Concept:** Transit Gateway hub-and-spoke with route table isolation for scalable multi-VPC architectures.

---

## Scenario 2: CIDR Planning

**Context:** A media company is designing a new VPC for their video processing platform. Their corporate network uses 10.0.0.0/16. They already have an existing AWS VPC using 10.1.0.0/16 that needs peering with the new VPC. The new VPC must support at least 3 Availability Zones (AZs), each with a public and private subnet. The private subnets need at least 250 usable IP addresses each for Auto Scaling Group (ASG) instances.

**Requirements:** No CIDR overlap with corporate (10.0.0.0/16) or existing VPC (10.1.0.0/16). Support 6 subnets across 3 AZs. Private subnets need 250+ usable IPs each. Leave room for future subnet expansion.

**Question:** Which VPC CIDR and subnet design meets these requirements?

A) VPC CIDR 10.2.0.0/16 with six /24 subnets (251 usable IPs each for private, /24 for public).

B) VPC CIDR 172.16.0.0/20 with six /28 subnets (11 usable IPs each).

C) VPC CIDR 10.1.0.0/20 with six /23 subnets (507 usable IPs each).

D) VPC CIDR 10.2.0.0/24 with six /27 subnets (27 usable IPs each).

**Answer: A**
10.2.0.0/16 doesn't overlap with corporate (10.0.0.0/16) or existing VPC (10.1.0.0/16). Each /24 subnet provides 256 - 5 = 251 usable IPs, meeting the 250+ requirement. A /16 VPC has ample room for future subnet expansion.

**Why others are wrong:**
- B) /28 subnets give only 16 - 5 = 11 usable IPs — far below 250 required.
- C) 10.1.0.0/20 overlaps with the existing VPC at 10.1.0.0/16. VPC peering requires non-overlapping CIDRs.
- D) A /24 VPC only has 256 total IPs. Six /27 subnets consume 192 IPs with only 27 usable each — insufficient for the 250 requirement.

**Key Concept:** CIDR planning must avoid overlaps with peered networks and corporate ranges while sizing subnets for workload requirements (remember 5 reserved IPs per subnet).

---

## Scenario 3: Public vs Private Subnet Architecture

**Context:** A healthcare SaaS company is deploying a HIPAA-compliant application. The architecture includes an Application Load Balancer (ALB), application servers running on Amazon Elastic Compute Cloud (EC2), a Relational Database Service (RDS) PostgreSQL database, and a bastion host for emergency SSH access. Application servers need to download software updates from the internet. The database must never be internet-accessible.

**Requirements:** HIPAA compliance — minimize internet exposure. Application servers need outbound internet only. Database fully isolated from internet. Bastion host for SSH access to app servers. All components in the same VPC.

**Question:** Which subnet placement is correct?

A) Public subnet: ALB, app servers, bastion host. Private subnet: RDS. Network Address Translation (NAT) Gateway in public subnet for app servers.

B) Public subnet: ALB, bastion host, NAT Gateway. Private subnet: app servers, RDS. App servers route outbound through NAT Gateway.

C) Public subnet: ALB, app servers, bastion host, NAT Gateway. Private subnet: RDS. Security Groups (SGs) on app servers restrict inbound to ALB only.

D) Private subnet: ALB, app servers, RDS. No public subnets. Use AWS PrivateLink for all traffic.

**Answer: B**
ALB and bastion host need public subnet for internet-facing access. NAT Gateway in public subnet allows app servers (private subnet) to reach the internet for updates without being directly reachable. RDS in private subnet with no internet route satisfies HIPAA isolation.

**Why others are wrong:**
- A) Placing app servers in a public subnet gives them public IPs and direct internet exposure — violates HIPAA's minimize-exposure principle. NAT Gateway is unnecessary if servers are already in a public subnet.
- C) Same problem — app servers in public subnet are internet-exposed. SGs restrict inbound, but HIPAA best practice is private subnet placement, not relying solely on SGs.
- D) An internet-facing ALB must be in a public subnet. You cannot place an internet-facing ALB in a private subnet — it needs an Internet Gateway (IGW) route.

**Key Concept:** Bastion and ALB go in public subnets; app and DB tiers go in private subnets with NAT Gateway for outbound-only internet access.

---

## Scenario 4: Stateless vs Stateful Filtering (NACL vs SG)

**Context:** A government agency detects suspicious traffic from IP range 203.0.113.0/24 targeting their web application. The application runs on EC2 instances in private subnets behind an ALB in public subnets. The security team needs to immediately block all traffic from this CIDR while maintaining normal operations for all other users. They also want to ensure internal services in a separate DB subnet can still communicate with the app subnet.

**Requirements:** Block specific IP range 203.0.113.0/24. No disruption to legitimate traffic. Solution must take effect at the subnet level, before traffic reaches instances. DB-to-app communication unaffected.

**Question:** Which approach blocks the malicious traffic? (Select TWO)

A) Add a DENY rule in the public subnet's NACL for inbound traffic from 203.0.113.0/24 with a lower rule number than existing ALLOW rules.

B) Add a DENY rule in the app subnet's Security Group for inbound traffic from 203.0.113.0/24.

C) Modify the ALB Security Group to remove 0.0.0.0/0 and add only trusted IP ranges.

D) Add a DENY rule in the public subnet's NACL for outbound traffic to 203.0.113.0/24 (ephemeral port range) with a lower rule number than existing ALLOW rules.

**Answer: A, D**
NACLs support DENY rules and operate at the subnet level. Since NACLs are **stateless**, you must block both directions: inbound (to prevent the request) AND outbound (to prevent responses on ephemeral ports). The rule number must be lower than existing ALLOW rules because NACLs evaluate rules in order — first match wins.

**Why others are wrong:**
- B) Security Groups do NOT support DENY rules — only ALLOW. You cannot block a specific IP with a Security Group.
- C) Removing 0.0.0.0/0 from the ALB SG would break access for all users, not just the malicious range. This is disruptive and doesn't meet the "no disruption" requirement.

**Key Concept:** Block specific IPs → NACL (supports DENY). NACLs are stateless → must handle both inbound AND outbound (ephemeral ports). Lower rule number = higher priority.

---

## Scenario 5: NAT Gateway vs NAT Instance / HA NAT Design

**Context:** A retail company runs a multi-AZ e-commerce platform. EC2 instances in private subnets across 3 AZs need outbound internet to call third-party payment APIs and download security patches. Peak traffic reaches 40 Gbps of outbound data. The company previously used a NAT Instance but experienced downtime when the instance failed. They need a highly available, managed solution.

**Requirements:** High availability across all 3 AZs. Handle 40 Gbps peak outbound throughput. Managed service — no instance maintenance. Cost-effective — minimize cross-AZ data transfer charges.

**Question:** Which architecture meets these requirements?

A) Deploy one NAT Gateway in a single public subnet. Route all 3 AZs' private subnets through this single NAT Gateway. It auto-scales to 100 Gbps.

B) Deploy one NAT Gateway per AZ (3 total), each in its AZ's public subnet. Each AZ's private subnet routes to its local NAT Gateway.

C) Replace the NAT Instance with a larger EC2 instance type (c5n.18xlarge) with enhanced networking. Place it behind an Auto Scaling Group for HA.

D) Use VPC Endpoints (Interface type) for all third-party API calls, eliminating the need for NAT entirely.

**Answer: B**
One NAT Gateway per AZ ensures that if an AZ fails, the other AZs continue operating independently — no cross-AZ failover needed. Each NAT Gateway auto-scales up to 100 Gbps, handling the 40 Gbps peak. Routing to the local AZ NAT Gateway avoids cross-AZ data transfer charges ($0.01/GB).

**Why others are wrong:**
- A) A single NAT Gateway in one AZ is a single point of failure — if that AZ goes down, all 3 AZs lose outbound internet. Also incurs cross-AZ charges for 2 of 3 AZs.
- C) NAT Instances require manual management (patching, monitoring, scaling). An ASG adds complexity but still depends on instance types with bandwidth limits. This violates the "managed service" requirement.
- D) Interface Endpoints only work for AWS services, not third-party external APIs. Payment APIs are on the public internet and require NAT or IGW.

**Key Concept:** HA NAT design = one NAT Gateway per AZ. NAT Gateway is AZ-resilient only, not region-resilient. Avoids cross-AZ charges by routing to local NAT Gateway.

---

## Scenario 6: VPC Peering vs Transit Gateway Decision

**Context:** A global logistics company has 15 VPCs across 3 AWS regions — 8 in us-east-1, 4 in eu-west-1, and 3 in ap-southeast-1. All VPCs in the same region need full mesh connectivity. On-premises data centers in New York and Frankfurt connect via AWS Direct Connect (DX). A new compliance requirement mandates that EU VPCs cannot communicate with APAC VPCs, but both can reach US VPCs.

**Requirements:** Full mesh within each region. Cross-region connectivity US↔EU and US↔APAC (but not EU↔APAC). On-premises DX integration. Route-level traffic isolation for compliance. Minimize connection management overhead.

**Question:** Which architecture meets these requirements?

A) Create VPC Peering between all VPCs within each region for intra-region mesh. Use VPC Peering across regions for cross-region connectivity. Use separate peering connections for DX integration.

B) Deploy one Transit Gateway per region. Peer TGWs cross-region: us-east-1↔eu-west-1 and us-east-1↔ap-southeast-1 (no EU↔APAC peering). Attach DX Gateway to US TGW. Use TGW route tables for isolation.

C) Use a single Transit Gateway in us-east-1 and attach all 15 VPCs (including cross-region) to it. Attach DX connections to this central TGW.

D) Deploy AWS Cloud WAN to build a global network. Connect all VPCs via Core Network. Use network policies for EU↔APAC isolation.

**Answer: B**
One TGW per region handles intra-region full mesh. Cross-region TGW peering (US↔EU, US↔APAC) provides the required connectivity while omitting EU↔APAC peering enforces compliance. DX Gateway attaches to the US TGW. TGW route tables provide granular traffic control with minimal overhead compared to managing 100+ peering connections.

**Why others are wrong:**
- A) Full mesh peering for 8 VPCs in us-east-1 alone requires 28 connections. Across 15 VPCs = massive overhead. VPC Peering doesn't support transitive routing, and DX cannot connect via peering.
- C) Transit Gateway is a regional resource — you cannot attach VPCs from other regions directly to a single TGW. Cross-region requires TGW peering.
- D) Cloud WAN is a valid global networking service, but it's more complex and costly than TGW peering for this scenario. The question asks to minimize overhead — TGW peering is simpler for 3 regions.

**Key Concept:** Transit Gateway for hub-and-spoke at scale. TGW peering for cross-region. Route tables for traffic isolation. VPC Peering doesn't scale beyond a handful of VPCs.

---

## Scenario 7: Gateway vs Interface Endpoints

**Context:** A data analytics company runs Apache Spark jobs on EC2 instances in a private subnet. The jobs read input from Amazon Simple Storage Service (S3), write results back to S3, and store metadata in Amazon DynamoDB. The instances also call AWS Systems Manager (SSM) for configuration. The security team mandates that NO traffic leaves the AWS network — all AWS service access must stay private. Currently, a NAT Gateway handles all outbound traffic, costing $3,200/month in data processing fees.

**Requirements:** All AWS service traffic stays on private network (no internet path). Reduce NAT Gateway costs. Access S3, DynamoDB, and SSM from private subnet. Maintain security compliance.

**Question:** Which combination reduces cost while meeting security requirements?

A) Create Gateway VPC Endpoints for S3, DynamoDB, and SSM. Remove the NAT Gateway entirely.

B) Create Gateway VPC Endpoints for S3 and DynamoDB (free). Create an Interface Endpoint for SSM. Remove NAT Gateway only if no other internet-bound traffic exists.

C) Create Interface Endpoints for S3, DynamoDB, and SSM. Remove the NAT Gateway.

D) Enable VPC Endpoint policies on the existing NAT Gateway to restrict traffic to AWS service IPs only.

**Answer: B**
Gateway Endpoints are free and support only S3 and DynamoDB — perfect for the bulk data traffic. SSM requires an Interface Endpoint (ENI-based, costs per hour + per GB but far less than NAT Gateway at this volume). This combo eliminates the $3,200/month NAT Gateway cost for AWS service traffic. NAT Gateway is only needed if instances still require general internet access.

**Why others are wrong:**
- A) Gateway Endpoints support ONLY S3 and DynamoDB. SSM is not supported as a Gateway Endpoint — it requires an Interface Endpoint.
- C) Using Interface Endpoints for S3 and DynamoDB works but costs money per hour and per GB. Gateway Endpoints for S3/DynamoDB are free — unnecessary cost when Gateway Endpoints exist.
- D) NAT Gateway doesn't have "VPC Endpoint policies." NAT Gateway routes traffic through the internet — it does not provide private network paths to AWS services.

**Key Concept:** Gateway Endpoint = S3 + DynamoDB only, FREE, route-table-based. Interface Endpoint = most other services, costs money, ENI-based. Always prefer Gateway Endpoint for S3/DynamoDB from within VPC.

---

## Scenario 8: Hub-and-Spoke Network Design with Transit Gateway

**Context:** A multinational bank is consolidating network architecture. They have 50 VPCs across 4 AWS accounts (shared via AWS Resource Access Manager), 2 on-premises data centers connected via Direct Connect, and a requirement for IP Multicast for their real-time trading floor data feeds. Current architecture uses a mesh of VPC Peering (1,200+ connections) that is unmanageable.

**Requirements:** Replace 1,200+ peering connections with a manageable solution. Support IP Multicast. Integrate DX connections. Share across 4 AWS accounts. Increase VPN bandwidth beyond 1.25 Gbps to data centers.

**Question:** Which architecture meets ALL requirements?

A) Deploy Transit Gateway. Attach all 50 VPCs and DX Gateway. Enable IP Multicast on TGW. Share TGW via Resource Access Manager (RAM). Use Equal-Cost Multi-Path (ECMP) with multiple Site-to-Site VPN connections to TGW for higher bandwidth.

B) Deploy Transit Gateway for VPC connectivity. Use a separate dedicated Multicast service on EC2 for trading data. Connect DX directly to each VPC that needs on-premises access.

C) Use AWS Cloud WAN with IP Multicast support. Attach all VPCs and DX connections. Share via RAM.

D) Keep VPC Peering for VPC-to-VPC traffic but add Transit Gateway only for DX and VPN connectivity. Use Application-level Multicast (SNS) for trading data.

**Answer: A**
Transit Gateway is the **only AWS service supporting IP Multicast**. It replaces 1,200+ peering connections with 50 attachments. TGW shares cross-account via RAM. DX Gateway attaches to TGW. ECMP with multiple S2S VPN connections to TGW increases bandwidth (1 VPN = 2.5 Gbps with TGW vs 1.25 Gbps with VGW; 3 VPNs = 7.5 Gbps).

**Why others are wrong:**
- B) DX doesn't connect directly to individual VPCs at this scale — DX Gateway + TGW is the pattern. Running Multicast on EC2 is complex and doesn't leverage AWS-managed IP Multicast.
- C) Cloud WAN does not support IP Multicast. Transit Gateway is the only AWS service with this capability.
- D) Keeping 1,200+ peering connections defeats the purpose. SNS is application-level pub/sub, not IP Multicast for network-level trading feeds.

**Key Concept:** Transit Gateway = only service supporting IP Multicast. ECMP with TGW doubles VPN throughput (2.5 Gbps vs 1.25 Gbps per connection). RAM shares TGW cross-account.

---

## Scenario 9: Troubleshooting with VPC Flow Logs

**Context:** A SaaS company reports intermittent connectivity issues between their web tier (public subnet) and database tier (private subnet). The application works sometimes but randomly drops connections. Security groups allow the correct ports. The operations team needs to identify whether the issue is at the Security Group or NACL level and set up ongoing monitoring to detect future anomalies.

**Requirements:** Determine if traffic is blocked at SG or NACL level. Set up alerting for rejected traffic patterns. Enable ad-hoc querying for historical analysis. Minimize cost for log storage.

**Question:** Which approach correctly diagnoses and monitors the issue?

A) Enable VPC Flow Logs at the VPC level, send to CloudWatch Logs. If logs show inbound ACCEPT + outbound REJECT → NACL issue (stateless, return traffic blocked). Set up CloudWatch Metric Filter on REJECT actions → CloudWatch Alarm → Amazon Simple Notification Service (SNS) alert.

B) Enable VPC Flow Logs at the Elastic Network Interface (ENI) level, send to S3. If logs show inbound REJECT → Security Group issue. Use Amazon Athena for querying. No alerting needed.

C) Enable AWS CloudTrail for network API calls. Check for SG/NACL modifications that may have caused the issue. Send to CloudWatch for alerting.

D) Use VPC Traffic Mirroring to capture full packets between web and DB subnets. Analyze with a third-party IDS tool.

**Answer: A**
VPC Flow Logs capture the ACTION field (ACCEPT/REJECT) per packet. The key diagnostic: **Inbound ACCEPT + Outbound REJECT = NACL issue** (NACLs are stateless, so return traffic on ephemeral ports must be explicitly allowed). **Inbound REJECT = could be SG or NACL.** CloudWatch Logs + Metric Filter on REJECT → Alarm → SNS provides real-time alerting. Flow Logs → S3 + Athena can be added later for historical ad-hoc queries.

**Why others are wrong:**
- B) ENI-level logs work but sending only to S3 misses the real-time alerting requirement. Also, inbound REJECT alone doesn't distinguish SG from NACL — you need both inbound and outbound ACTION fields.
- C) CloudTrail logs API calls (who changed what), not network traffic flows. It can show if someone modified a NACL/SG but cannot diagnose packet-level ACCEPT/REJECT patterns.
- D) Traffic Mirroring captures full packets — massive overkill and cost for diagnosing ACCEPT/REJECT patterns. Flow Logs are purpose-built for this and far cheaper.

**Key Concept:** Flow Log diagnosis: Inbound ACCEPT + Outbound REJECT = NACL (stateless, ephemeral ports not allowed). Inbound REJECT = SG or NACL. Use CloudWatch Metric Filters for alerting, Athena for ad-hoc SQL analysis.

---

## Key Takeaways

1. **Transit Gateway** scales where VPC Peering breaks down — hub-and-spoke, transitive routing, IP Multicast, ECMP
2. **CIDR planning** — avoid overlaps, remember 5 reserved IPs/subnet, size for growth
3. **NACL vs SG** — "block IP" = NACL; NACLs are stateless (handle ephemeral ports); SGs can't DENY
4. **NAT HA** = one NAT Gateway per AZ; single NAT Gateway = SPOF
5. **Gateway Endpoint** = S3 + DynamoDB, free; **Interface Endpoint** = everything else, costs money
6. **DX vs VPN** — DX is private but NOT encrypted; DX + VPN = encrypted private
7. **Flow Logs** — Inbound ACCEPT + Outbound REJECT = NACL blocking return traffic
