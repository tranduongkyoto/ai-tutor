# Networking — Concept Mapper (Phase 1)
**Date:** 2026-05-15 | **Domain:** Networking | **Mode:** concept-mapper

---

## 1. Service Overview

**Amazon Virtual Private Cloud (VPC)**
- Isolated virtual network you define within AWS — IP ranges, subnets, route tables, gateways
- Every AWS account gets a **Default VPC** per region (172.31.0.0/16) with internet connectivity out of the box
- Max 5 VPCs per region (soft limit); up to 5 CIDR blocks per VPC (/28 min, /16 max)
- Only private IPv4 ranges: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16

**Subnets**
- Tied to a single Availability Zone (AZ); defined as a CIDR range within the VPC CIDR
- **Public subnet**: has a route to an Internet Gateway (IGW)
- **Private subnet**: no direct internet route — traffic exits via Network Address Translation (NAT) Gateway
- AWS reserves 5 IPs per subnet (first 4 + last 1) — so a /24 gives 251 usable IPs, not 256

**Internet Gateway (IGW)**
- Enables VPC resources to reach the Internet — horizontally scaled, HA, managed by AWS
- 1:1 relationship with VPC; IGW alone isn't enough — route table must have `0.0.0.0/0 → IGW`

**NAT Gateway (NATGW)**
- AWS-managed NAT for private subnet outbound Internet access (IPv4)
- Created per AZ with an Elastic IP; starts at 5 Gbps, auto-scales to 100 Gbps
- For full HA: deploy one NATGW per AZ — no cross-AZ failover needed
- Cannot be used by instances in the **same** subnet

**NAT Instance** (legacy, still on exam)
- Self-managed EC2 performing NAT; must disable Source/Destination Check
- You manage Security Groups (SGs), bandwidth depends on instance type, not HA by default

**Network Access Control List (NACL)**
- **Stateless** firewall at subnet level; supports ALLOW + DENY rules
- Rules numbered 1–32,766 (lower number = higher priority, first match wins)
- Default NACL: allows all. New custom NACL: denies all
- Must explicitly allow ephemeral ports for return traffic

**Security Groups (SGs)**
- **Stateful** firewall at instance level; ALLOW rules only (no DENY)
- Return traffic is automatically allowed; all rules evaluated before decision

**Virtual Private Cloud (VPC) Peering**
- Private connection between two VPCs — must not have overlapping CIDRs
- **NOT transitive** (A↔B + B↔C ≠ A↔C)
- Works cross-account, cross-region; must update route tables in both VPCs

**VPC Endpoints (AWS PrivateLink)**
- Access AWS services via private network — no IGW/NATGW needed

| Type | Services | Cost | Mechanism | Best For |
|------|----------|------|-----------|----------|
| **Gateway Endpoint** | S3, DynamoDB only | Free | Route table entry | In-VPC access (exam default) |
| **Interface Endpoint** | Most AWS services | $/hr + $/GB | ENI with SG | On-premises / cross-region access |

**VPC Flow Logs**
- Capture IP traffic info at VPC, Subnet, or Elastic Network Interface (ENI) level
- Destinations: Amazon Simple Storage Service (S3), CloudWatch Logs, Kinesis Data Firehose
- Key field: `ACTION` — REJECT on inbound = NACL or SG; ACCEPT in + REJECT out = NACL (stateless)

**AWS Site-to-Site VPN**
- Encrypted connection over public Internet between on-premises and VPC
- Components: Virtual Private Gateway (VGW) on AWS side + Customer Gateway (CGW) on customer side
- Must enable Route Propagation for VGW in route tables

**AWS Direct Connect (DX)**
- Dedicated **private** physical connection from on-premises to AWS
- 1 Gbps–400 Gbps (Dedicated) or 50 Mbps–25 Gbps (Hosted)
- Lead time: >1 month; **NOT encrypted** by default — add VPN overlay for encryption

**Direct Connect Gateway**
- Connect a single DX connection to VPCs in multiple regions

**AWS VPN CloudHub**
- Hub-and-spoke model connecting multiple on-premises sites via VPN through a single VGW
- Traffic over public Internet (encrypted); low-cost multi-site connectivity

**Transit Gateway (TGW)**
- Hub-and-spoke for **thousands** of VPCs + on-premises connections — **transitive** routing
- Regional resource; share cross-account via Resource Access Manager (RAM)
- Only AWS service supporting **IP Multicast**
- ECMP: multiply VPN bandwidth (1 VPN = 2.5 Gbps via TGW vs 1.25 Gbps via VGW)

**Egress-Only Internet Gateway**
- NAT equivalent for **IPv6 only** — allows outbound, blocks inbound
- All IPv6 addresses in AWS are public; IPv4 cannot be disabled (dual-stack only)

**AWS Network Firewall**
- Managed Layer 3–7 firewall protecting entire VPC
- IP/port filtering, domain-based rules, regex matching, intrusion prevention
- Centrally managed cross-account via AWS Firewall Manager

---

## 2. Real-World Use Cases

- **Startup needs internet-facing web servers + private databases** → Standard 3-tier VPC: public subnet (ALB + Bastion), private app tier, private DB tier
- **Private EC2 needs to download OS updates** → NAT Gateway in public subnet; route private subnet 0.0.0.0/0 → NATGW
- **Block a malicious IP hitting your subnet** → NACL DENY rule (SGs can't deny)
- **Lambda in VPC needs DynamoDB access** → Gateway VPC Endpoint (free, no NATGW cost)
- **On-premises data center needs private S3 access via Direct Connect** → Interface VPC Endpoint (Gateway Endpoints not accessible from on-prem)
- **Company has 50 VPCs that need to talk** → Transit Gateway (Peering = 1,225 connections vs 1 TGW)
- **Need encrypted private connection to AWS** → Direct Connect + Site-to-Site VPN overlay
- **Multiple branch offices connecting to AWS** → VPN CloudHub via single VGW
- **SSH into private EC2 for maintenance** → Bastion Host in public subnet; restrict SSH source CIDR

---

## 3. Service Integrations

```
Internet ← IGW ← Public Subnet (ALB, Bastion, NATGW)
                        ↓
               Private Subnet (EC2, Lambda)
                   ↓              ↓
             NATGW → IGW     Gateway Endpoint → S3/DynamoDB
                              Interface Endpoint → Other AWS services

On-Premises ← Customer Gateway ← S2S VPN ← VGW ← VPC
On-Premises ← DX Location ← Direct Connect ← VGW ← VPC
On-Premises ← DX → DX Gateway → VPCs (multi-region)

VPC A ↔ VPC Peering ↔ VPC B  (non-transitive, 1:1)
VPC A ↔ Transit Gateway ↔ VPC B/C/D...  (transitive, hub-and-spoke)

Flow Logs → CloudWatch Logs → Metric Filter → Alarm → SNS
Flow Logs → S3 → Athena → QuickSight
```

---

## 4. Architectural Patterns

**Standard 3-Tier VPC**
- Public: ALB + Bastion + NATGW | Private App: EC2/ASG | Private DB: RDS/ElastiCache
- NACLs per subnet, SGs per instance, IGW at VPC boundary

**HA NAT Gateway**
- One NATGW per AZ in its own public subnet → each AZ's private subnet routes to its local NATGW
- AZ failure = no NAT needed for that AZ (self-contained)

**Hybrid Connectivity Decision Tree**

| Need | Solution | Setup Time | Encrypted? | Bandwidth |
|------|----------|------------|-----------|-----------|
| Quick connection | Site-to-Site VPN | Minutes | Yes | ~1.25 Gbps |
| Consistent high bandwidth | Direct Connect | >1 month | No | Up to 400 Gbps |
| Encrypted private line | DX + VPN | >1 month | Yes | DX speed |
| DX failover | DX primary + VPN backup | Mix | Mix | Mix |
| Multi-site offices | VPN CloudHub | Minutes | Yes | ~1.25 Gbps |
| Increase VPN throughput | TGW + ECMP | Minutes | Yes | 2.5 Gbps × N |

**Multi-VPC Connectivity Decision**
- 2–3 VPCs → VPC Peering (simpler, non-transitive)
- Many VPCs + on-prem → Transit Gateway (transitive, centralized routing)

---

## 5. Cost Implications

| Resource | Pricing Model | Optimization Tip |
|----------|--------------|------------------|
| NATGW | $0.045/hr + $0.045/GB | Use Gateway Endpoint for S3/DynamoDB instead |
| Gateway Endpoint | **Free** | Always prefer for S3/DynamoDB access |
| Interface Endpoint | $/hr + $/GB | Only use when needed (on-prem, cross-region) |
| Same-AZ traffic (private IP) | **Free** | Keep communicating services in same AZ |
| Cross-AZ (private IP) | $0.01/GB | Acceptable for HA tradeoff |
| Cross-AZ (public/Elastic IP) | $0.02/GB | Avoid — use private IPs |
| S3 → CloudFront | **Free** | Always front S3 with CloudFront for distribution |
| Direct Connect | Port hours + data out | Higher upfront but lower per-GB than Internet |

---

## 6. Security Considerations

- **Defense in depth**: NACL (subnet) + Security Group (instance) — both should be configured
- **Bastion Host SG**: restrict SSH (port 22) to corporate CIDR only — never 0.0.0.0/0
- **Private instances SG**: allow SSH only from Bastion SG (reference SG, not IP)
- **VPC Endpoints**: eliminate public Internet exposure for AWS service access
- **Direct Connect**: private but NOT encrypted — add VPN for encryption
- **Flow Logs**: enable for audit trail and threat detection; analyze with Athena or CloudWatch
- **Network Firewall**: Layer 3–7 inspection, IPS, domain filtering for egress control
- **NACLs for IP blocking**: only NACLs can DENY — use to block known malicious IPs
- **IPv6 awareness**: all IPv6 in AWS is public — use Egress-Only IGW for private subnet IPv6 outbound

---

## 7. Exam Tips — Keywords & Signals

| Keyword in Question | Answer Signal |
|---------------------|---------------|
| "Block specific IP" | NACL (SGs can't deny) |
| "Private access to S3/DynamoDB from VPC" | Gateway VPC Endpoint (free) |
| "Private access from on-premises" | Interface VPC Endpoint |
| "Hub-and-spoke, many VPCs" | Transit Gateway |
| "IP Multicast" | Transit Gateway (only service) |
| "Transitive routing/peering" | Transit Gateway (peering is non-transitive) |
| "Dedicated private connection" | Direct Connect |
| "Encrypted private connection" | DX + VPN |
| "Multiple office sites connect" | VPN CloudHub |
| "SSH into private instances" | Bastion Host |
| "IPv6 outbound only" | Egress-Only Internet Gateway |
| "Capture/inspect traffic" | Traffic Mirroring |
| "Monitor/troubleshoot IP traffic" | VPC Flow Logs |
| "Layer 3–7 VPC protection" | AWS Network Firewall |
| "NAT managed by AWS" | NAT Gateway |
| "Least operational overhead for NAT" | NAT Gateway (not NAT Instance) |

---

## Key Takeaways

- **VPC = your private network in AWS** — subnets, route tables, gateways, firewalls all compose it
- **SG vs NACL**: stateful/allow-only/instance vs stateless/allow+deny/subnet — know which to use when
- **Gateway Endpoint = free S3/DynamoDB access** from within VPC — exam almost always prefers this
- **NAT Gateway per AZ** for HA — don't rely on cross-AZ failover
- **Direct Connect = private but NOT encrypted** — combine with VPN for encryption
- **Transit Gateway = transitive hub-and-spoke** for many VPCs; VPC Peering = non-transitive 1:1
- **5 reserved IPs per subnet** — remember when calculating usable addresses
