# Load Balancing & Scaling — Mini Exam: Scenarios (Phase 4)
**Date:** 2026-05-19 15:36
**Score:** 9/10 (90%)
**Scope:** scenarios — architecture decisions and trade-offs

---

## Questions & Results

### Q1 ✓ — ALB + NLB Split Architecture (alb-vs-nlb-decision)
**Question:** Gaming company needs raw TCP with IP whitelisting + web portal with path-based routing across 3 AZs.

A) Single ALB with TCP and HTTPS listeners
B) NLB (Elastic IPs) for game server + ALB (path routing) for web portal
C) Single NLB with path-based routing for all services
D) GWLB for game server + ALB for web portal

**Your answer: B** — Correct. NLB for TCP/static IP, ALB for HTTP path routing. ALB can't do raw TCP; NLB can't do path routing.

---

### Q2 ✓ — Deregistration Delay for Long Requests (connection-draining)
**Question:** Rolling deployments cause 502 errors on 10-minute data exports. Default Deregistration Delay (300s) too short.

A) Increase Deregistration Delay to ≥ 600 seconds
B) Decrease to 0 for faster replacement
C) Enable Connection Draining (separate feature)
D) Switch to NLB

**Your answer: A** — Correct. Increase to ≥ 600s (longest request duration). Connection Draining and Deregistration Delay are the SAME feature (different names for CLB vs ALB/NLB).

---

### Q3 ✓ — GWLB for 3rd-Party Firewalls (gateway-load-balancer)
**Question:** Government agency needs transparent traffic inspection through CheckPoint firewall fleet.

A) AWS Network Firewall (managed service)
B) NLB with TCP to CheckPoint EC2
C) GWLB as transparent gateway with CheckPoint target group
D) ALB + WAF matching CheckPoint policies

**Your answer: C** — Correct. GWLB = transparent gateway + LB for 3rd-party appliances. GENEVE port 6081.

---

### Q4 ✓ — Predictive Scaling for Evening Spikes (auto-scaling-group)
**Question:** Streaming platform with predictable 8 PM-midnight spikes. 4-min warm-up causes buffering. Least operational overhead?

A) Scheduled Scaling at 7:55 PM
B) Predictive Scaling (ML-based pre-launch)
C) Lower Target Tracking target to 30%
D) Pre-bake AMI with current Target Tracking

**Your answer: B** — Correct. Predictive Scaling uses ML for proactive scaling before demand. Adapts automatically, least overhead vs Scheduled.

---

### Q5 ✓ — Cross-Zone LB Disabled Impact (cross-zone-load-balancing)
**Question:** 10 instances (8 in AZ-a, 2 in AZ-b) currently evenly distributed. What happens if cross-zone is disabled?

A) No change — cross-zone mandatory on ALB
B) AZ-a: 6.25 each, AZ-b: 25 each (50/50 AZ split)
C) All traffic routes to AZ-a (more instances)
D) ALB migrates instances to rebalance

**Your answer: B** — Correct. Without cross-zone: 50/50 AZ split → AZ-a 6.25 each, AZ-b 25 each. Cross-zone can be disabled at TG level on ALB.

---

### Q6 ✓ — SNI Multi-Domain on Single ALB (ssl-server-name-indication)
**Question:** Two domains (portal/admin) each with own ACM cert. Minimize cost.

A) Two ALBs, one per domain
B) One ALB with SNI for both certs, hostname routing
C) One CLB with two SSL certs
D) One NLB with TLS + SNI + hostname routing

**Your answer: B** — Correct. ALB + SNI = multiple certs on one LB with hostname-based routing. CLB doesn't support SNI; NLB can't do hostname routing.

---

### Q7 ✓ — ASG Cooldown Over-provisioning (auto-scaling-group)
**Question:** Flash sale causes CPU spike → ASG adds instances → adds MORE before first batch stabilizes. Root cause?

A) Target too low at 50%
B) Cooldown period too short — increase to let new instances stabilize
C) Replace Target Tracking with Step Scaling
D) Reduce maximum capacity

**Your answer: B** — Correct. Cooldown (default 300s) prevents duplicate scaling while metrics stabilize. Increase cooldown or use pre-baked AMI for faster readiness.

---

### Q8 ✗ — Sticky Sessions + Deregistration Delay for Session Persistence (sticky-sessions / connection-draining)
**Question:** Legacy app with server-side sessions. Scale-in = cart loss. Scale-out = wrong instance. Select TWO fixes.

A) Enable sticky sessions (AWSALB cookie)
B) Increase Deregistration Delay for scale-in session completion
C) Enable cross-zone LB
D) Switch to NLB for client IP preservation

**Your answer: A, D** — Incorrect. Correct: A, B. Sticky sessions fix scale-out routing. Deregistration Delay protects in-flight sessions during scale-in. NLB client IP doesn't solve server-side session storage.

---

### Q9 ✓ — NLB+ALB Stack for WAF + Fixed IP (network-load-balancer)
**Question:** Need WAF (SQL injection) AND fixed IP for whitelisting.

A) ALB with WAF + Elastic IP
B) NLB (Elastic IP) → ALB (WAF attached)
C) NLB with WAF attached
D) Global Accelerator → ALB + WAF

**Your answer: B** — Correct. NLB+ALB stacking: NLB for static IP, ALB for WAF. ALB can't have Elastic IP; WAF can't attach to NLB.

---

### Q10 ✓ — ASG Max Capacity Ceiling (auto-scaling-group)
**Question:** ASG never scales out despite RequestCountPerTarget > 1000 threshold. Instances healthy.

A) Max capacity = desired capacity (no headroom)
B) Health checks failing
C) Cooldown just ended
D) Target Tracking only works with CPU

**Your answer: A** — Correct. Max = desired means no room to scale out. Target Tracking works with RequestCountPerTarget, CPU, Network — not CPU-only.

---

## Summary
- **Score:** 9/10 (90%)
- **Missed topics:** sticky-sessions/connection-draining (Deregistration Delay for scale-in protection)
- **Strong areas:** alb-vs-nlb, gateway-load-balancer, predictive-scaling, cross-zone-load-balancing, sni, cooldown, max-capacity, nlb+alb stacking
- **Key lessons:**
  - During scale-in, Deregistration Delay protects in-flight sessions. NLB client IP preservation does NOT solve server-side session loss — sessions are in server memory, not tied to IP.
  - Better long-term fix for session issues: externalize to ElastiCache or DynamoDB.
