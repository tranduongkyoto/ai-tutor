# Networking — Mini Exam: Design (Phase 5)
**Date:** 2026-05-15 16:43
**Score:** 6/10 (60%)
**Scope:** design — Architecture design decisions and trade-offs

---

## Questions & Results

### Q1 ✓ — Global Multi-Region DX Connectivity (direct-connect)
**Question:** A global financial services company has offices in New York and London. They need to connect both offices to their Virtual Private Cloud (VPC) in us-east-1 with consistent low-latency performance for trading applications. The London office also needs access to a VPC in eu-west-1. They require encrypted data in transit and can tolerate up to 2 months for setup. What architecture provides the MOST reliable and secure connectivity?

A) Establish an AWS Direct Connect (DX) connection from each office to its nearest AWS Region, use a Direct Connect Gateway to connect both VPCs, and layer AWS Site-to-Site VPN over each DX connection for encryption
B) Set up two AWS Site-to-Site VPN connections from each office to each VPC, using AWS VPN CloudHub for inter-office communication and Internet Protocol Security (IPsec) encryption
C) Establish a single AWS Direct Connect (DX) connection from the New York office with a Direct Connect Gateway to both VPCs, and use Virtual Private Cloud (VPC) peering between the two regions for the London office
D) Create AWS Transit Gateways in each region peered together, connect both offices via Site-to-Site VPN to the nearest Transit Gateway, and use Equal-Cost Multi-Path (ECMP) routing for bandwidth

**Your answer: A** — Correct. DX from each office provides consistent low-latency, Direct Connect Gateway enables multi-region VPC access, and VPN over DX provides IPsec encryption since DX alone is private but NOT encrypted.

---

### Q2 ✗ — Defense-in-Depth Against Route Table Misconfiguration (nacl-vs-sg)
**Question:** A healthcare company runs a three-tier application in a single Virtual Private Cloud (VPC). Compliance requires that the database tier NEVER be accessible from the Internet, even if a misconfiguration occurs in route tables. The application tier in private subnets needs outbound Internet access for software updates. A recent audit found that a junior engineer accidentally added a route to an Internet Gateway (IGW) in a private subnet's route table. Which combination of controls provides the STRONGEST defense-in-depth against this type of misconfiguration? (Select TWO)

A) Deploy a Network Access Control List (NACL) on the database subnet that explicitly DENYs all inbound traffic from 0.0.0.0/0 with a low rule number, and allow only the application subnet CIDR range on required database ports
B) Use Security Groups on the database instances to allow inbound traffic only from the application tier Security Group on the database port, and deny all other traffic
C) Enable Amazon VPC Flow Logs on the database subnet's ENI and create a CloudWatch alarm to alert when any Internet-routable source IP is detected
D) Use AWS Organizations Service Control Policy (SCP) to deny the ec2:CreateRoute action for routes targeting Internet Gateways on database subnet route tables, restricting this to only the network team's IAM role

**Your answer: A, B** — Incorrect. Correct answers: A, D. SCP (preventive) prevents misconfiguration at the organizational level; NACL (blocking) catches traffic at subnet level. SGs only allow (no deny) and don't address the root cause of route table misconfiguration. Flow Logs are detective only, not preventive.

---

### Q3 ✗ — DX Burst Capacity and Fast Failover (direct-connect)
**Question:** A media company streams live video to millions of viewers. Their on-premises data center connects to AWS via a 10 Gbps AWS Direct Connect (DX) connection. During peak events, they need to burst to 25 Gbps. The current DX connection is at a single DX location. They also need a failover path that can be established within hours, not months. What is the MOST cost-effective architecture that meets both the bandwidth and failover requirements?

A) Order a second 10 Gbps Dedicated Direct Connect (DX) connection at a different DX location for maximum resiliency, giving 20 Gbps total with full redundancy
B) Add a Hosted Direct Connect (DX) connection at 25 Gbps through an AWS Direct Connect Partner for bursting, and configure an AWS Site-to-Site VPN as the failover path
C) Upgrade the existing Dedicated Direct Connect (DX) to 25 Gbps and establish multiple AWS Site-to-Site VPN connections through an AWS Transit Gateway with ECMP routing as a failover mechanism
D) Create a Link Aggregation Group (LAG) by adding two more 10 Gbps Dedicated Direct Connect (DX) connections at the same location, bundling all three into a 30 Gbps LAG for burst capacity

**Your answer: C** — Incorrect. Correct answer: B. Hosted DX via partner provides on-demand capacity without >1 month Dedicated DX lead time. S2S VPN as failover can be established within hours. Upgrading Dedicated DX (option C) also requires new physical connection (>1 month).

---

### Q4 ✓ — Multi-VPC Connectivity with Selective S3 Access (transit-gateway)
**Question:** A SaaS company has 150 microservices running across 12 VPCs in the same AWS Region. Each VPC needs to communicate with every other VPC, and all traffic must stay on the AWS private network. A subset of 3 VPCs also needs access to S3 for data lake operations, while the remaining VPCs should be blocked from S3. The company wants to minimize networking resources to manage. What architecture achieves this with the LEAST operational overhead?

A) Create an AWS Transit Gateway (TGW) with a single route table for all 12 VPCs, and deploy Gateway VPC Endpoints for S3 only in the 3 VPCs that need S3 access
B) Create full-mesh VPC Peering connections between all 12 VPCs, and use Interface VPC Endpoints for S3 in the 3 VPCs with Security Groups limiting access
C) Create an AWS Transit Gateway with two route tables and deploy Gateway VPC Endpoints in the 3 VPCs
D) Create an AWS Transit Gateway with a single route table, deploy Gateway VPC Endpoints in all 12 VPCs, and use S3 bucket policies to deny access from 9 non-authorized VPCs

**Your answer: A** — Correct. TGW with single route table provides transitive routing. Gateway Endpoints only in 3 VPCs inherently blocks the other 9 from private S3 access. Least management overhead.

---

### Q5 ✓ — Cost Optimization: NATGW to Gateway Endpoint (vpc-endpoints)
**Question:** A logistics company processes shipment tracking data from 500 IoT devices. The tracking application needs to query a shared DynamoDB table. Currently, traffic routes through a NAT Gateway costing $2,000/month. The security team requires DynamoDB traffic never traverse the public Internet. What change reduces cost the MOST while meeting the security requirement?

A) Replace the NAT Gateway with a NAT Instance using a smaller EC2 instance type
B) Create a Gateway VPC Endpoint for DynamoDB in Warehouse A's VPC, and update private subnet route tables
C) Create an Interface VPC Endpoint (PrivateLink) for DynamoDB with a Security Group
D) Deploy a Transit Gateway with a single Gateway Endpoint shared across VPCs

**Your answer: B** — Correct. Gateway VPC Endpoint for DynamoDB is FREE — eliminates the $2K/month NATGW cost. Traffic stays on AWS private network.

---

### Q6 ✗ — DX Encryption and Capacity Upgrade (direct-connect)
**Question:** A multinational bank runs a trading platform with a 5 Gbps DX connection through a Direct Connect Gateway. Compliance mandates ALL data be encrypted in transit. They're using 4.5 Gbps and anticipate 30% growth. Which architecture addresses BOTH encryption and capacity with LEAST disruption?

A) Add S2S VPN over DX for encryption + second 5 Gbps Dedicated DX
B) Enable MACsec on existing DX for Layer 2 encryption + upgrade to 10 Gbps
C) Replace DX with multiple S2S VPNs through TGW with ECMP
D) Add Hosted DX 5 Gbps + CloudHSM for app-layer encryption

**Your answer: A** — Incorrect. Correct answer: B. MACsec provides native Layer 2 encryption on DX without throughput bottleneck. VPN over DX limits throughput to ~1.25 Gbps per tunnel, which would bottleneck 4.5+ Gbps traffic. Upgrading to 10 Gbps handles growth.

---

### Q7 ✓ — NAT Gateway High Availability (nat-gateway)
**Question:** A company's single NAT Gateway in one AZ caused all 3 AZs to lose Internet connectivity during an AZ failure. What is the MOST highly available and cost-efficient solution?

A) NAT Instance in Auto Scaling Group across 3 AZs
B) One NAT Gateway per AZ with local route tables
C) NAT Gateway in 2 of 3 AZs with cross-AZ failover for third
D) Single Regional NAT Gateway

**Your answer: B** — Correct. One NATGW per AZ is the AWS-recommended HA pattern. Each AZ routes to its own NATGW. If an AZ fails, only that AZ is affected.

---

### Q8 ✓ — Multi-Account Private Connectivity (transit-gateway)
**Question:** 8 accounts under AWS Organizations need private connectivity to a shared services VPC with OpenSearch. No traffic should traverse the public Internet. What is the MOST scalable architecture?

A) Transit Gateway shared via RAM with route tables to shared services VPC
B) 8 VPC Peering connections to shared services VPC
C) PrivateLink endpoint service exposing OpenSearch + Interface Endpoints in each account
D) Internet-facing ALB with HTTPS + IP allowlisting

**Your answer: A** — Correct. TGW shared via RAM is most scalable. Transitive hub-and-spoke model. Adding accounts is simple — just attach VPC to TGW.

---

### Q9 ✗ — Large Data Migration Over DX (direct-connect)
**Question:** 50 TB initial migration within 2 weeks + ongoing 100 GB/day sync over a 1 Gbps DX connection (600 Mbps production traffic during business hours). What is the MOST efficient approach?

A) Snowball Edge for 50 TB + DataSync over DX for daily 100 GB
B) Transfer 50 TB over DX during off-peak hours + same for daily sync
C) S2S VPN parallel path for migration + DX for daily sync
D) Second 1 Gbps Dedicated DX for migration

**Your answer: B** — Incorrect. Correct answer: A. Off-peak only ~12 hours × 400 Mbps = ~2.16 TB/day = ~23 days for 50 TB (exceeds 2-week deadline). Snowball completes in ~1 week without impacting production DX. DataSync over DX handles 100 GB/day easily.

---

### Q10 ✓ — Isolated VPC with S3 and SSM Access (vpc-endpoints)
**Question:** Isolated VPC (no IGW, no NAT, no VPN) needs EC2 to write to S3 and read from SSM Parameter Store. Must enforce only specific S3 buckets accessible. What architecture meets ALL requirements?

A) Gateway Endpoint for S3 (with endpoint policy for bucket ARNs) + Interface Endpoint for SSM (with Security Group)
B) Interface Endpoints for both S3 and SSM
C) NAT Gateway for outbound S3/SSM + bucket policies
D) Gateway Endpoints for both S3 and SSM

**Your answer: A** — Correct. Gateway Endpoint for S3 (free, endpoint policy restricts to specific buckets). Interface Endpoint for SSM (required — Gateway doesn't support SSM). All traffic stays private.

---

## Summary
- **Score:** 6/10 (60%)
- **Missed topics:** direct-connect, nacl-vs-sg
- **Strong areas:** transit-gateway, vpc-endpoints, nat-gateway
- **Key lessons:**
  - MACsec is native Layer 2 encryption for DX — prefer over VPN overlay when DX throughput must be preserved. VPN over DX limits to ~1.25 Gbps per tunnel.
  - Hosted DX via partners provides on-demand capacity without >1 month Dedicated DX lead time. Use for burst scenarios.
  - For large one-time migrations over bandwidth-constrained DX, Snowball is the answer. Calculate actual available off-peak bandwidth vs. deadline.
  - Defense-in-depth: SCP (preventive at org level) + NACL (blocking at subnet level) is stronger than SG (instance-level allow-only). SCPs prevent misconfigurations before they happen.
