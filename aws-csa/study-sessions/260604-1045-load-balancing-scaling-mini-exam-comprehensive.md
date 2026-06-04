# Load Balancing & Scaling — Mini Exam: Comprehensive Final (Phase 4)
**Date:** 2026-06-04 10:45
**Score:** 6/10 (60%)
**Scope:** comprehensive — Full domain exam with cross-domain integration

---

## Questions & Results

### Q1 ✅ — Deregistration Delay for rolling deployments (connection-draining)
**Question:** ALB target group Deregistration Delay 300s. Rolling deployment of 6 instances takes 30+ min. Stateless REST API completing in 100ms. How to speed up?

A) Disable Deregistration Delay (set to 0)
B) Reduce Deregistration Delay from 300s to 5s since stateless requests complete in 100ms
C) Switch to NLB which has no Deregistration Delay
D) Increase ASG capacity to 12 for simultaneous replacement

**Your answer: B** — Correct. For stateless short-lived requests, 5s drain window is sufficient. Saves ~295s per instance replacement.

---

### Q2 ✅ — Transparent network inspection with GWLB (gwlb)
**Question:** Third-party WAF appliances need to see original source/destination IPs in all packets. Transparent routing without modifying application subnets.

A) ALB at Layer 7 using HTTP headers
B) NLB at Layer 4 preserving client source IP
C) GWLB at Layer 3 using GENEVE on port 6081 as transparent gateway
D) CLB with proxy protocol

**Your answer: C** — Correct. GWLB operates at Layer 3, provides transparent network gateway preserving original IP packets, uses GENEVE on port 6081.

---

### Q3 ✗ — Target Tracking warm-up prevention (asg-scaling-policies | asg-cooldown)
**Question:** ASG scales out 5 instances. Average CPU drops to 33% across 15 instances (new ones at 0%). What prevents premature scale-in?

A) Default cooldown period of 300s prevents any scaling activity
B) Target Tracking has built-in logic ignoring scale-in during scale-out/warm-up
C) ALB health check grace period excludes new instances from metric calculation
D) Cross-zone LB distributes traffic immediately so CPU equalizes within seconds

**Your answer: A** — Incorrect. Correct: B. Target Tracking has built-in warm-up intelligence that specifically prevents premature scale-in — more targeted than blunt cooldown.

---

### Q4 ✅ — Sticky sessions causing uneven ECS Fargate distribution (sticky-sessions | compute:ecs-fargate)
**Question:** ECS Fargate with ALB dynamic port mapping. Cross-zone enabled but some tasks get significantly more traffic. Most likely cause?

A) Cross-zone not supported with Fargate
B) Sticky sessions enabled, causing returning customers to pin to specific tasks
C) Round-robin vs least-outstanding-requests algorithm
D) ECS minimum healthy percentage preventing new task launches

**Your answer: B** — Correct. Sticky sessions cause load imbalance — returning clients pinned to same task via AWSALB cookie.

---

### Q5 ✗ — Blue/green deployment with ALB weighted target groups (alb-weighted-target-groups | dns:route53-weighted)
**Question:** Blue (port 8080) and green (port 9090) environments behind same ALB. Need traffic shifting between versions.

A) Route 53 weighted routing between two separate ALBs
B) ALB weighted target groups — two TGs under same listener, shift weight 100/0 to 0/100
C) Two ALB listeners on different ports with Route 53 failover
D) Switch to NLB for TCP port-based routing

**Your answer: C** — Incorrect. Correct: B. ALB supports weighted target groups under a single listener for instant traffic shifting — no DNS changes or separate LBs needed.

---

### Q6 ✅ — Security Group pattern for LB-to-EC2 (security-group-pattern)
**Question:** Ensure EC2 in private subnets only reachable through ALB. Which SG configuration?

A) EC2 SG allows HTTP from 0.0.0.0/0, relying on private subnet routing
B) EC2 SG allows HTTP from ALB's Elastic IP
C) EC2 SG allows HTTP only from ALB's Security Group ID as source
D) EC2 SG with no inbound rules, ALB bypasses SG checks

**Your answer: C** — Correct. Reference ALB's SG ID, not IPs. ALBs don't have Elastic IPs; their private IPs change.

---

### Q7 ✅ — Cost optimization with Spot + right-sizing (asg-spot-instances | asg-right-sizing)
**Question:** 4 t3.large instances at 15% CPU (business hours), 3% overnight. Stateless, fault-tolerant. Which TWO changes optimize cost? (Select TWO)

A) Switch to Spot Instances (up to 90% discount, fault-tolerant app)
B) Scheduled Scaling to reduce to 1 instance overnight
C) Right-size to t3.medium + Target Tracking at 40% CPU
D) Enable ASG hibernation for 2 instances overnight

**Your answer: A, C** — Correct. Spot for fault-tolerant workloads; right-sizing from t3.large to t3.medium doubles effective CPU utilization.

---

### Q8 ✗ — NLB health check protocol support (nlb-health-checks)
**Question:** NLB needs TCP and HTTP health checks for custom service on port 5000 + HTTP /status on port 8080.

A) NLB only supports TCP health checks — need separate ALB for HTTP
B) Configure NLB TG health check to use HTTP on port 8080 with /status — NLB supports TCP, HTTP, HTTPS
C) NLB health checks are Layer 4 only — use TCP + separate CloudWatch alarm
D) Configure two simultaneous health checks on same TG

**Your answer: A** — Incorrect. Correct: B. NLB health checks support TCP, HTTP, and HTTPS protocols despite forwarding at Layer 4. Health check protocol ≠ forwarding protocol.

---

### Q9 ✅ — Spot fleet diversification strategy (compute:spot-fleet-diversification)
**Question:** Spot ASG with c5.large, c5a.large, m5.large across 3 AZs. Why does multiple instance types improve availability?

A) Different types have different On-Demand prices, ASG selects cheapest
B) Each type × AZ = separate Spot capacity pool; diversification reduces risk of simultaneous reclamation
C) ASG assigns different bid prices per type
D) Multiple types enable Cluster Placement Groups for fault tolerance

**Your answer: B** — Correct. 3 types × 3 AZs = 9 capacity pools. If one pool reclaims, other pools still available.

---

### Q10 ✗ — Health check thresholds and failure detection speed (alb-health-checks)
**Question:** ALB health check: 30s interval, 5s timeout, healthy threshold 3, unhealthy threshold 2. Buggy deploy returns 500. ~2 min before ALB stops routing. What explains delay and how to detect faster?

A) 30s × 2 = 60s detection + Deregistration Delay 300s. Reduce Deregistration Delay.
B) 30s × 2 = ~60s detection + draining. Reduce interval to 10s + keep unhealthy threshold 2 = ~20s detection.
C) Healthy threshold of 3 requires 3 healthy responses. Reduce healthy threshold.
D) ASG cooldown 300s prevents terminating unhealthy instances. Reduce cooldown.

**Your answer: C** — Incorrect. Correct: B. Healthy threshold controls unhealthy→healthy transition, NOT failure detection. Unhealthy threshold × interval = detection speed. Reduce interval (30→10s) for faster detection.

---

## Summary
- **Score:** 6/10 (60%)
- **Missed topics:** asg-scaling-policies, alb-weighted-target-groups, nlb-health-checks, alb-health-checks
- **Strong areas:** connection-draining, gwlb, sticky-sessions, security-group-pattern, spot-instances, right-sizing
- **Key lessons:**
  - Target Tracking has built-in warm-up logic preventing premature scale-in — more sophisticated than cooldown timer
  - ALB weighted target groups enable instant blue/green traffic shifting within a single listener — no DNS changes needed
  - NLB health checks support TCP, HTTP, and HTTPS — Layer 4 forwarding doesn't limit health check protocol
  - Healthy threshold = unhealthy→healthy transition. Unhealthy threshold × interval = failure detection speed. Different directions.
