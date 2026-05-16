# Networking — Mini Exam: Comprehensive Final (Phase 6)
**Date:** 2026-05-15 22:38
**Score:** 9/10 (90%)
**Scope:** comprehensive — all networking topics

---

## Questions & Results

### Q1 ✓ — Custom NACL Default Deny (nacl-vs-sg)
**Question:** A company has a Virtual Private Cloud (VPC) with multiple private subnets across two Availability Zones (AZs). Developers report that EC2 instances in AZ-B's private subnet can reach the internet, but instances in AZ-A's private subnet cannot. The Network Address Translation (NAT) Gateway in AZ-A's public subnet is running, and the route table for AZ-A's private subnet has a route `0.0.0.0/0 → nat-gateway-a`. What is the MOST likely cause?

A) The Internet Gateway (IGW) is not attached to the VPC, so no subnet can reach the internet
B) The NAT Gateway in AZ-A does not have an Elastic IP address associated with it
C) The Network Access Control List (NACL) on AZ-A's private subnet is a new custom NACL that denies all traffic by default
D) The Security Group (SG) on the EC2 instances in AZ-A does not allow outbound traffic on port 443

**Your answer: C** — Correct. A new custom NACL denies all traffic by default. AZ-B works so IGW is attached (A wrong). NATGW requires EIP at creation (B implausible). Default SGs allow all outbound (D wrong).

---

### Q2 ✓ — DX + VPN Encryption (direct-connect)
**Question:** A solutions architect needs to connect an on-premises data center to a Virtual Private Cloud (VPC) with a dedicated private connection that provides consistent network performance for a latency-sensitive financial trading application. The connection must also encrypt data in transit. Which solution meets these requirements?

A) Set up an AWS Site-to-Site VPN connection using a Virtual Private Gateway (VGW) on the VPC
B) Establish an AWS Direct Connect (DX) connection and configure a Site-to-Site VPN over the Direct Connect connection for IPsec encryption
C) Create a VPC peering connection between the on-premises network and the VPC using AWS Transit Gateway
D) Set up AWS VPN CloudHub to connect the data center to the VPC with multiple VPN connections for redundancy

**Your answer: B** — Correct. DX provides consistent latency; DX + VPN adds IPsec encryption. VPN alone uses public internet (A). VPC peering doesn't connect on-prem (C). CloudHub is for multi-site VPN hub-and-spoke (D).

---

### Q3 ✓ — NACL Ephemeral Ports (nacl-ephemeral-ports)
**Question:** A company runs a three-tier application in a Virtual Private Cloud (VPC). The web tier in public subnets needs to communicate with the database tier in private subnets. A Network Access Control List (NACL) protects each subnet. After deploying new NACL rules, the web servers can send requests to the database on port 3306, but never receive responses. Which change fixes this issue?

A) Add an outbound rule to the database subnet NACL allowing TCP ports 1024-65535 to the web subnet CIDR
B) Add an inbound rule to the web subnet Security Group (SG) allowing TCP port 3306 from the database subnet CIDR
C) Modify the database subnet NACL to be stateful so return traffic is automatically allowed
D) Add an inbound rule to the web subnet NACL allowing TCP port 3306 from the database subnet CIDR

**Your answer: A** — Correct. NACLs are stateless; return traffic on ephemeral ports must be explicitly allowed. SGs are stateful so B is irrelevant. NACLs cannot be made stateful (C). Responses use ephemeral ports, not 3306 (D).

---

### Q4 ✓ — Transit Gateway Route Tables (transit-gateway)
**Question:** A company has 15 Virtual Private Clouds (VPCs) across three AWS accounts and needs to establish connectivity between all VPCs. They also need to connect their on-premises data center via an existing AWS Direct Connect (DX) connection. Some VPCs should be isolated from each other for compliance. Which solution meets all requirements with the LEAST operational overhead?

A) Create VPC peering connections between all 15 VPCs and attach the Direct Connect to a Virtual Private Gateway (VGW) in one VPC
B) Deploy an AWS Transit Gateway (TGW), attach all 15 VPCs and the Direct Connect Gateway, and use TGW route tables to isolate specific VPCs
C) Set up a hub VPC with VPN connections to all other VPCs and route on-premises traffic through the hub using a NAT Gateway
D) Create an AWS Transit Gateway with a single default route table and use Network Access Control Lists (NACLs) in each VPC to control inter-VPC traffic

**Your answer: B** — Correct. TGW provides hub-and-spoke with transitive routing, DX Gateway integration, cross-account via RAM, and route table isolation. Peering requires 105 connections (A). NAT Gateway doesn't route VPC-to-VPC (C). Single route table doesn't isolate VPCs (D).

---

### Q5 ✓ — Gateway VPC Endpoint for S3 (vpc-endpoints)
**Question:** A solutions architect needs to provide private access to Amazon Simple Storage Service (S3) from EC2 instances in a private subnet. The company wants to minimize costs and the instances do not need to access any other AWS services privately. Which solution is MOST cost-effective?

A) Deploy a NAT Gateway in the public subnet and route S3 traffic through the Internet Gateway (IGW)
B) Create a Gateway VPC Endpoint for S3 and add a route in the private subnet's route table
C) Create an Interface VPC Endpoint (AWS PrivateLink) for S3 and attach a Security Group (SG)
D) Set up a VPC peering connection to the AWS-managed S3 VPC in the same region

**Your answer: B** — Correct. Gateway Endpoints for S3 are FREE. NATGW costs $0.045/hr + $0.045/GB (A). Interface Endpoints cost per hour + GB (C). Cannot peer with AWS-managed S3 VPC (D).

---

### Q6 ✓ — Flow Log Troubleshooting (flow-logs-troubleshooting)
**Question:** A company uses VPC Flow Logs to monitor network traffic. The security team notices that certain EC2 instances show inbound requests with `action=ACCEPT` but the corresponding outbound responses show `action=REJECT`. What is the MOST likely explanation?

A) The Security Group (SG) is blocking the outbound response traffic because it lacks an outbound allow rule
B) The Network Access Control List (NACL) is rejecting the outbound return traffic because NACLs are stateless
C) The Internet Gateway (IGW) is throttling outbound traffic due to bandwidth limits being exceeded
D) The VPC Flow Logs are misconfigured and showing false REJECT entries for valid return traffic

**Your answer: B** — Correct. Inbound ACCEPT + Outbound REJECT = NACL issue (stateless). SGs are stateful so return traffic auto-allowed (A). IGWs don't throttle (C). Flow Logs accurately capture actions (D).

---

### Q7 ✗ — Direct Connect Gateway (direct-connect-gateway)
**Question:** A multinational company needs to connect Virtual Private Clouds (VPCs) in us-east-1 and eu-west-1 to a single AWS Direct Connect (DX) connection at a co-location facility in the US. Which component enables this architecture?

A) Create a Virtual Private Gateway (VGW) in each region and attach both to the same Direct Connect connection
B) Use a Direct Connect Gateway to associate the single DX connection with VPCs across multiple regions
C) Set up VPC peering between the two regional VPCs and route Direct Connect traffic through the peered connection
D) Deploy an AWS Transit Gateway in each region and connect them directly to the Direct Connect connection

**Your answer: C** — Incorrect. Correct answer: B. Direct Connect Gateway connects one DX to VPCs in multiple regions. VPC peering handles VPC-to-VPC traffic, not DX routing (C). VGW is regional, can't attach two from different regions to same DX (A). TGW requires DX Gateway as intermediary (D).

---

### Q8 ✓ — Block Malicious IP (nacl-vs-sg, waf)
**Question:** A company needs to block a specific IP address that is sending malicious requests to their web application running in a Virtual Private Cloud (VPC). The application uses an Application Load Balancer (ALB) in a public subnet. Which approach effectively blocks this IP address? (Select TWO)

A) Add a DENY rule in the Network Access Control List (NACL) for the public subnet with the malicious IP as the source
B) Add a rule in the Security Group (SG) attached to the ALB to deny inbound traffic from the malicious IP
C) Create a rule in AWS Web Application Firewall (WAF) associated with the ALB to block the malicious IP address
D) Remove the route to the malicious IP from the public subnet's route table to prevent traffic from reaching the ALB

**Your answer: A, C** — Correct. NACLs support DENY rules at subnet level. WAF can block IPs via IP set rules on ALB. SGs only support ALLOW rules, no DENY (B). Route tables route by destination, not source IP (D).

---

### Q9 ✓ — DX Backup with VPN (direct-connect-backup)
**Question:** A company is setting up a disaster recovery solution. Their primary AWS Direct Connect (DX) connection takes 6 weeks to provision. They need a backup connectivity solution that can be deployed quickly and is cost-effective. Which solution provides the BEST backup for the Direct Connect connection?

A) Provision a second AWS Direct Connect connection at a different Direct Connect location for maximum resiliency
B) Set up an AWS Site-to-Site VPN connection as a backup that can be established within hours
C) Use AWS VPN CloudHub to connect multiple office locations and route traffic through the hub as backup
D) Deploy a NAT Gateway in the public subnet to provide internet-based backup connectivity to on-premises

**Your answer: B** — Correct. S2S VPN deploys in hours, cost-effective DX backup. Second DX takes weeks and is expensive (A). CloudHub is multi-site, not DX backup (C). NAT Gateway is for outbound internet, not on-prem connectivity (D).

---

### Q10 ✓ — Transit Gateway ECMP (transit-gateway-ecmp)
**Question:** A company wants to increase the bandwidth of their VPN connection to AWS beyond the 1.25 Gbps limit of a single Site-to-Site VPN connection. They currently have 8 Virtual Private Clouds (VPCs) that need to be accessible. Which architecture achieves higher VPN throughput while maintaining connectivity to all VPCs?

A) Create multiple Site-to-Site VPN connections to the same Virtual Private Gateway (VGW) and configure Equal-Cost Multi-Path (ECMP) routing
B) Attach multiple VPN connections to an AWS Transit Gateway (TGW) and enable ECMP routing to aggregate bandwidth
C) Replace the VPN connection with a Hosted Direct Connect connection at 10 Gbps for higher bandwidth
D) Deploy a NAT Gateway in each VPC to split VPN traffic across multiple internet paths for higher throughput

**Your answer: B** — Correct. TGW supports ECMP: each VPN = 2.5 Gbps, multiple VPNs aggregate. ECMP is NOT supported with VGW (A). DX doesn't address VPN throughput question (C). NAT Gateways don't split VPN traffic (D).

---

## Summary
- **Score:** 9/10 (90%)
- **Missed topics:** direct-connect-gateway
- **Strong areas:** nacl-vs-sg, transit-gateway, vpc-endpoints, flow-logs, direct-connect-backup, transit-gateway-ecmp
- **Key lessons:**
  - Direct Connect Gateway is required to connect a single DX connection to VPCs in multiple regions. VPC peering handles VPC-to-VPC traffic only, not DX routing. Remember: DX → DX Gateway → VPCs in any region.
