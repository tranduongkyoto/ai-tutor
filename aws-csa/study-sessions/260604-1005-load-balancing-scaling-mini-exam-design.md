# Load Balancing & Scaling — Mini Exam: Design (Phase 3)
**Date:** 2026-06-04 10:05
**Score:** 7/10 (70%)
**Scope:** design — Architecture design decisions and trade-offs

---

## Questions & Results

### Q1 ✅ — Static IP whitelisting for TCP workload (nlb-static-ip)
**Question:** A financial services company runs a trading platform that requires ultra-low latency TCP connections. Their compliance team mandates that all clients must connect to specific, pre-approved IP addresses for firewall whitelisting. The platform also needs to handle millions of concurrent connections. The solutions architect must choose a load balancing approach that meets both the performance and compliance requirements. Which solution best meets these requirements?

A) Deploy an Application Load Balancer (ALB) across multiple Availability Zones (AZs) and use the ALB's DNS hostname for client connections, with Route 53 health checks for failover
B) Deploy a Network Load Balancer (NLB) across multiple AZs and assign an Elastic IP address per AZ to provide static IP addresses for client whitelisting
C) Deploy a Classic Load Balancer (CLB) with cross-zone load balancing enabled, and use Route 53 weighted routing to distribute traffic across multiple CLBs
D) Deploy an Application Load Balancer (ALB) behind a Global Accelerator to obtain static IP addresses, using path-based routing rules for the trading protocol

**Your answer: B** — Correct. NLB operates at Layer 4 (TCP/UDP), handles millions of requests/second with ultra-low latency, and provides one static IP per AZ with Elastic IP support.

---

### Q2 ✅ — Cross-zone load balancing for uneven AZ distribution (cross-zone-load-balancing)
**Question:** A media streaming company serves video content across three AZs. AZ-1 has 2 backend instances, AZ-2 has 8, AZ-3 has 2. Instances in AZ-1 and AZ-3 are overwhelmed while AZ-2 is underutilized. Which configuration resolves the uneven distribution most cost-effectively?

A) Replace with NLB and enable cross-zone load balancing, accepting inter-AZ data transfer charges
B) Keep the ALB and verify cross-zone load balancing is enabled at the target group level, as ALB has this enabled by default at no additional charge
C) Add more instances to AZ-1 and AZ-3 to match AZ-2's capacity, keeping cross-zone disabled
D) Enable cross-zone on GWLB and route all traffic through a centralized inspection fleet

**Your answer: B** — Correct. ALB has cross-zone load balancing enabled by default with no additional inter-AZ charges. Each ALB node distributes evenly across all instances in all AZs.

---

### Q3 ✅ — Multi-domain SSL on single ALB (ssl-sni)
**Question:** A SaaS company needs to add a partner-facing API serving 5 different partner domains, each with its own SSL/TLS certificate managed through ACM. A junior engineer suggests 5 separate load balancers. What is the most cost-effective alternative?

A) Use a single ALB with multiple HTTPS listeners and SNI to route to the correct certificate based on hostname
B) Use a single NLB with TLS listeners and SNI, routing each domain to separate target groups
C) Deploy a single ALB with one wildcard certificate covering all 5 partner domains
D) Place CloudFront in front of the ALB, associating all 5 ACM certificates with CloudFront

**Your answer: A** — Correct. ALB supports multiple SSL certificates via Server Name Indication (SNI). Client indicates hostname in TLS handshake; ALB selects correct ACM certificate.

---

### Q4 ✗ — Scaling strategies for predictable + unpredictable traffic (asg-scaling-policies | asg-cooldown)
**Question:** An e-commerce company has predictable lunch-hour spikes and unpredictable flash-sale surges (10x in 5 minutes). ASG with Target Tracking at 60% CPU scales too slowly during flash sales (10-15 min degraded performance). Which combination of scaling strategies best addresses both? (Select TWO)

A) Add Scheduled Scaling for lunch-hour traffic
B) Replace Target Tracking with Simple Scaling at 50% and 80% CPU thresholds
C) Add Predictive Scaling to analyze historical patterns and pre-provision capacity
D) Use a pre-baked AMI and smaller cooldown period to accelerate instance readiness

**Your answer: A, C** — Incorrect. Correct answers: C, D. The problem is instance readiness time (10-15 min), not when to scale. Pre-baked AMI eliminates setup time; shorter cooldown allows faster consecutive scaling. A is redundant with C; Predictive Scaling already covers known patterns.

---

### Q5 ✅ — Network intrusion detection with transparent inspection (gwlb)
**Question:** A healthcare company deploying third-party IDS virtual appliances needs transparent inspection of all VPC traffic without changing application routing. Which LB solution?

A) NLB in front of IDS fleet with TCP listeners
B) GWLB integrated with IDS fleet using GENEVE protocol on port 6081 for transparent inspection
C) ALB with path-based routing to IDS appliances
D) NLB in front of ALB for transparent network inspection

**Your answer: B** — Correct. GWLB operates at Layer 3 (IP packets), provides transparent network gateway + load balancer for third-party appliances, uses GENEVE on port 6081.

---

### Q6 ✅ — NLB + ALB stacking for mixed traffic (nlb-alb-stacking | compute:ecs-dynamic-port-mapping)
**Question:** ECS Fargate microservices with dynamic ports need both public HTTP/HTTPS and internal gRPC with static IPs for on-premises firewalls. Which architecture?

A) Single ALB with HTTP and gRPC listeners
B) NLB with ALB as target group — NLB provides static IPs for gRPC, ALB handles HTTP routing with ECS dynamic port mapping
C) Two separate ALBs with Route 53 weighted routing
D) Single NLB with TCP listeners for both services

**Your answer: B** — Correct. NLB + ALB stacking: NLB provides static IPs per AZ for whitelisting, ALB provides Layer 7 HTTP routing with ECS dynamic port mapping.

---

### Q7 ✗ — Instance warm-up and health check gating (alb-health-checks | connection-draining)
**Question:** ASG instances take 8 minutes to warm cache from Redis. ALB sends traffic to instances that return HTTP 200 but serve degraded responses during warm-up. How to prevent?

A) Increase ASG cooldown to 600 seconds
B) Configure ALB target group health check to use custom `/ready` endpoint that returns 200 only after cache is fully populated
C) Enable ALB sticky sessions
D) Switch to Step Scaling with higher CPU threshold

**Your answer: A** — Incorrect. Correct answer: B. ALB health checks at target group level gate traffic — custom `/ready` endpoint blocks traffic until instance is ready. Cooldown controls scaling action frequency, not traffic routing.

---

### Q8 ✗ — Route 53 health check vs weight for maintenance (dns:route53-health-checks | weighted-routing)
**Question:** Weighted routing (70/30 US-East-1/EU-West-1). Need to redirect all traffic to EU-West-1 during US-East-1 maintenance without DNS propagation delays. Which approach?

A) Change weight to 0/100, wait for TTL expiration
B) Scale US-East-1 ASG to 0, triggering health check failure
C) Associate health checks with US-East-1 ALB and deliberately fail the health check — Route 53 immediately stops returning unhealthy record
D) Switch to failover routing policy

**Your answer: A** — Incorrect. Correct answer: C. Route 53 health check failure immediately removes the record from responses — no TTL wait needed. Weight changes still depend on clients' cached DNS expiring.

---

### Q9 ✅ — Client IP behind ALB (alb-x-forwarded-for)
**Question:** Application logs show ALB's private IP instead of real client IP, breaking rate limiting. How to get real client IP?

A) Enable cross-zone load balancing to preserve connection metadata
B) Replace ALB with NLB which preserves client source IP natively
C) Configure backend to read `X-Forwarded-For` header added by ALB
D) Enable ALB access logs to S3 and query in real-time

**Your answer: C** — Correct. ALB terminates client connection; adds `X-Forwarded-For` header with original client IP. Backend reads this header.

---

### Q10 ✗ — Accelerating scale-in after traffic drops (connection-draining | asg-cooldown)
**Question:** After tournament events, scale-in takes 15+ minutes with 300s cooldown and 300s Deregistration Delay. Short-lived WebSocket connections. Which TWO changes accelerate scale-in?

A) Reduce Deregistration Delay from 300s to 30s for short-lived connections
B) Switch to Predictive Scaling for ML-based scale-in forecasting
C) Reduce ASG cooldown from 300s to 60s for faster metric evaluation
D) Replace custom AMI with pre-baked AMI for faster boot

**Your answer: C, D** — Incorrect. Correct answers: A, C. Deregistration Delay is the key scale-in bottleneck — each instance waits 5 min to drain before termination. Shorter delay = faster termination. Faster boot (D) helps scale-out speed, not scale-in.

---

## Summary
- **Score:** 7/10 (70%)
- **Missed topics:** asg-scaling-policies, asg-cooldown, alb-health-checks, connection-draining, dns:route53-health-checks
- **Strong areas:** nlb-static-ip, cross-zone-load-balancing, ssl-sni, gwlb, nlb-alb-stacking, alb-x-forwarded-for
- **Key lessons:**
  - Predictive Scaling + pre-baked AMI addresses slow scale-out (instance readiness), not when to trigger scaling
  - ALB health checks gate traffic routing — custom `/ready` endpoint prevents sending traffic to unready instances. Cooldown only affects scaling action frequency.
  - Route 53 health check failure immediately removes record from DNS responses — faster than weight changes which depend on TTL expiration
  - Deregistration Delay is the primary bottleneck for scale-in speed — instances can't terminate until drain period expires. Boot time affects scale-out, not scale-in.
