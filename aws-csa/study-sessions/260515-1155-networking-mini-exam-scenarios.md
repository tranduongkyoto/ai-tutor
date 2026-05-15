# Networking — Mini Exam: Scenarios (Phase 4)
**Date:** 2026-05-15 11:55
**Score:** 9/10 (90%)
**Scope:** scenarios — 80% scenario-based, 20% fact-based. Focus on architecture decisions, trade-offs.

---

## Questions & Results

### Q1 ✓ — HA NAT Gateway Design (nat-gateway)
**Question:** A startup is deploying a microservices application across 3 AZs. Each AZ has a private subnet running EC2 application servers that need to pull container images from Docker Hub. The company wants a managed, highly available solution with no single point of failure and minimal cross-AZ data transfer costs. Which architecture meets these requirements?

A) Deploy a single NAT Gateway in one public subnet. Update all 3 private subnet route tables to point 0.0.0.0/0 to this NAT Gateway.
B) Deploy a NAT Instance in each AZ's public subnet with Source/Destination Check disabled. Place each behind an Auto Scaling Group for failover.
C) Deploy one NAT Gateway per AZ in each AZ's public subnet. Each private subnet's route table points 0.0.0.0/0 to its local AZ's NAT Gateway.
D) Deploy a single NAT Gateway and configure cross-AZ failover using Amazon Route 53 health checks to redirect traffic if the NAT Gateway's AZ fails.

**Your answer: C** — Correct. One NAT Gateway per AZ eliminates cross-AZ SPOF. Local routing avoids cross-AZ data transfer charges. NAT Gateway is managed and auto-scales to 100 Gbps.

---

### Q2 ✓ — NACL IP Blocking (nacl-vs-sg)
**Question:** A company's security team discovers a botnet at IP range 198.51.100.0/24. They need to block this IP range immediately at the subnet level without disrupting legitimate users. NACLs are stateless. Which TWO actions are required? (Select TWO)

A) Add a DENY rule in the public subnet's NACL for inbound traffic from 198.51.100.0/24, with a rule number lower than existing ALLOW rules.
B) Add a DENY rule in the ALB's Security Group for inbound traffic from 198.51.100.0/24.
C) Add a DENY rule in the public subnet's NACL for outbound traffic to 198.51.100.0/24 on the ephemeral port range, with a rule number lower than existing ALLOW rules.
D) Enable AWS Shield Advanced on the ALB to automatically block the IP range.

**Your answer: A, C** — Correct. NACLs are stateless — must block both inbound AND outbound (ephemeral ports). SGs don't support DENY rules (B wrong). Shield doesn't replace NACL blocking (D).

---

### Q3 ✓ — Gateway vs Interface Endpoints Cost (vpc-endpoints)
**Question:** EC2 instances in private subnets process data in S3, write to DynamoDB, and reach SSM. Compliance requires no public internet traversal. NAT Gateway costs $4,500/month. Which combination provides private access at lowest cost?

A) Create Interface VPC Endpoints for S3, DynamoDB, and SSM. Remove the NAT Gateway.
B) Create Gateway VPC Endpoints for S3 and DynamoDB. Create an Interface Endpoint for SSM. Remove the NAT Gateway if no other internet-bound traffic exists.
C) Create Gateway VPC Endpoints for S3, DynamoDB, and SSM. Remove the NAT Gateway.
D) Keep the NAT Gateway but add VPC Endpoint policies to route only S3 traffic through a Gateway Endpoint.

**Your answer: B** — Correct. Gateway Endpoints (free) for S3/DynamoDB. Interface Endpoint for SSM. Gateway doesn't support SSM (C wrong). Interface for S3/DynamoDB costs money unnecessarily (A wrong).

---

### Q4 ✗ — DX Backup + Encryption (direct-connect)
**Question:** A company has 1 Gbps DX. Needs backup path operational within minutes (not months) + DX encryption. Which TWO solutions? (Select TWO)

A) Establish a Site-to-Site VPN connection as a backup path over the public internet — activates in minutes when DX fails.
B) Order a second Direct Connect connection from a different DX location for redundancy.
C) Configure a Site-to-Site VPN over the existing Direct Connect connection to add IPsec encryption.
D) Enable TLS on the Direct Connect virtual interface to encrypt traffic natively.

**Your answer: B, C** — Incorrect. Correct answers: **A, C**. Second DX (B) takes >1 month to establish — doesn't meet "within minutes" requirement. S2S VPN over internet (A) provides fast backup. VPN over DX (C) adds encryption. DX has no native TLS (D wrong).

---

### Q5 ✓ — Transit Gateway Cross-Region (transit-gateway)
**Question:** 20 VPCs in us-east-1, 10 in eu-west-1, 5 in ap-southeast-1. All need full mesh within region. 3 on-premises offices via DX. Need transitive routing and minimal management. Which architecture?

A) VPC Peering mesh + DX Gateway per VPC.
B) One TGW per region. Peer TGWs cross-region. Attach DX Gateway. Use route tables.
C) Single central TGW in us-east-1 for all regions.
D) AWS Cloud WAN as global backbone.

**Your answer: B** — Correct. TGW is regional — one per region for intra-region mesh. Cross-region TGW peering connects regions. Can't attach cross-region VPCs to single TGW (C wrong). Peering requires 190+ connections for 20 VPCs (A wrong).

---

### Q6 ✓ — CIDR Overlap Avoidance (subnets)
**Question:** New VPC must peer with existing VPC (10.0.0.0/16) and connect to corporate (172.16.0.0/12). Needs 4 subnets with 500+ usable IPs each. Which CIDR?

A) 10.1.0.0/16 — 65K IPs.
B) 192.168.0.0/20 — 4K IPs, 4 × /22 subnets (1,019 usable each).
C) 172.20.0.0/16 — 65K IPs.
D) 192.168.0.0/24 — 256 IPs.

**Your answer: B** — Correct. No overlap with 10.0.0.0/16 or 172.16.0.0/12. /22 subnets = 1,019 usable IPs. A overlaps (10.1.x.x within 10.0.0.0/16). C overlaps (172.20.x.x within 172.16.0.0/12). D too small.

---

### Q7 ✓ — NAT Instance Source/Dest Check (nat-instance)
**Question:** NAT Instance fails after Source/Destination Check re-enabled. Why must it be disabled?

A) NAT Instance forwards traffic not destined for itself — check blocks such forwarding.
B) Check blocks SSH connections.
C) Check prevents Elastic IP attachment.
D) Check conflicts with Security Group rules.

**Your answer: A** — Correct. NAT Instance receives packets where it's neither source nor destination. Check must be disabled for forwarding to work.

---

### Q8 ✓ — Flow Log NACL Diagnosis (flow-logs)
**Question:** Intermittent DB failures. Flow Logs: inbound to RDS = ACCEPT, outbound from RDS = REJECT. Root cause?

A) SG missing outbound rule for 3306.
B) NACL missing outbound ALLOW for ephemeral ports (1024-65535).
C) Web NACL missing inbound 3306 rule.
D) RDS needs public subnet.

**Your answer: B** — Correct. Inbound ACCEPT + Outbound REJECT = NACL issue (stateless). Return traffic on ephemeral ports not explicitly allowed. SGs are stateful (A wrong).

---

### Q9 ✓ — TGW Multicast + ECMP (transit-gateway)
**Question:** Need IP Multicast for 50 VPCs + increased VPN throughput beyond 1.25 Gbps. Which service?

A) Transit Gateway — Multicast + ECMP (2.5 Gbps per VPN).
B) Cloud WAN — native Multicast + VPN.
C) VPC Peering + multicast SGs.
D) DX with Multicast + VPN overlay.

**Your answer: A** — Correct. TGW is the ONLY AWS service supporting IP Multicast. ECMP doubles VPN throughput. Cloud WAN doesn't support Multicast (B wrong).

---

### Q10 ✓ — VPC Peering Non-Transitive (vpc-peering)
**Question:** VPC-A↔VPC-B and VPC-B↔VPC-C peered. VPC-A can't reach VPC-C despite VPC-B route tables configured. Cause?

A) Cross-account SG references not supported.
B) VPC Peering is non-transitive — no routing through VPC-B.
C) VPC-B NACL blocks forwarded traffic.
D) Route table can't point to 2 peerings.

**Your answer: B** — Correct. VPC Peering is fundamentally non-transitive. A↔B + B↔C ≠ A↔C regardless of routes. Need direct A↔C peering or Transit Gateway.

---

## Summary
- **Score:** 9/10 (90%)
- **Missed topics:** direct-connect
- **Strong areas:** nat-gateway, nacl-vs-sg, vpc-endpoints, transit-gateway, subnets, nat-instance, flow-logs, vpc-peering
- **Key lessons:**
  - Direct Connect takes >1 month to establish — for quick backup, use S2S VPN over public internet (minutes to set up). DX is private but NOT encrypted; overlay VPN over DX for IPsec encryption. Don't confuse "maximum resiliency" (second DX) with "fast failover" (S2S VPN backup).
