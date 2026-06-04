# Load Balancing & Scaling — Mini Exam: Comprehensive Final (Phase 4 Retry)
**Date:** 2026-06-04 11:35
**Score:** 9/10 (90%) — PASSED (improved from 60%)
**Scope:** comprehensive — Full domain exam with cross-domain integration
**Weak topic review before retry:** asg-scaling-policies, alb-weighted-target-groups, nlb-health-checks, alb-health-checks

---

## Questions & Results

### Q1 ✅ — Canary deployment with ALB weighted target groups (alb-weighted-target-groups)
**Question:** Company wants 5% canary traffic to new API version on same ALB. Fastest traffic shift, no DNS dependency?

A) Two ALBs with Route 53 weighted routing
B) ALB listener weighted target groups — 95% v1.0, 5% v2.0
C) Path-based routing with custom X-Canary header
D) Same target group with port-based round-robin

**Your answer: B** — Correct. ALB weighted target groups shift traffic instantly within a single listener.

---

### Q2 ✅ — Target Tracking warm-up prevents premature scale-in (asg-scaling-policies)
**Question:** After scale-out, average CPU drops because new instances at 0%. Why doesn't ASG scale in?

A) Cooldown period blocks all scaling
B) Target Tracking built-in logic ignores scale-in during warm-up
C) ALB health check grace period excludes new instances from metrics
D) CloudWatch 5-minute aggregation delay

**Your answer: B** — Correct. Target Tracking has built-in warm-up intelligence that suppresses scale-in while instances are warming.

---

### Q3 ✅ — NLB HTTP health check support (nlb-health-checks)
**Question:** NLB with TCP service on 5000 + HTTP /ready on 8080. Need application-level health verification.

A) TCP on 5000 verifies both connectivity and readiness
B) HTTP on 8080 with /ready — NLB supports TCP, HTTP, HTTPS health checks
C) NLB only supports TCP — need separate ALB for HTTP health checking
D) Two simultaneous health checks on same target group

**Your answer: B** — Correct. NLB health checks support TCP, HTTP, and HTTPS despite operating at Layer 4.

---

### Q4 ✅ — Health check failure detection timing (alb-health-checks)
**Question:** ALB health check: interval=10s, timeout=5s, unhealthy threshold=3, healthy threshold=2. Instance returns 503. How long to detect?

A) 5 seconds (timeout)
B) 10 seconds (one interval)
C) 20 seconds (healthy threshold × interval)
D) 30 seconds (unhealthy threshold × interval)

**Your answer: D** — Correct. Failure detection = unhealthy threshold (3) × interval (10s) = ~30 seconds.

---

### Q5 ✅ — Custom /ready health check gates traffic during warm-up (alb-health-checks)
**Question:** New instances take 6 min to warm cache. Return 200 but degraded results during warm-up. How to prevent routing?

A) Increase ASG cooldown to 360s
B) Custom /ready endpoint returns 200 only after cache populated, health check interval × healthy threshold ≈ 6 min
C) Sticky sessions to avoid cold instances
D) Over-provision by 20% for warm spares

**Your answer: B** — Correct. Health checks gate traffic routing. Custom /ready endpoint blocks traffic until instance is ready.

---

### Q6 ✅ — Multiple SSL certs via SNI (ssl-sni)
**Question:** Two domains (api.internal.com + www.company.com) each with own ACM cert on single ALB.

A) Wildcard cert covering both
B) Single listener with default cert + additional cert via SNI + host-based routing
C) Two listeners on different ports
D) ALB can't serve two certs — need two ALBs

**Your answer: B** — Correct. ALB supports multiple SSL certificates via SNI. Client indicates hostname in TLS handshake.

---

### Q7 ✅ — Cross-zone LB with NLB charges (cross-zone-load-balancing)
**Question:** NLB with uneven instances across AZs (2-6-2). Cross-zone disabled. AZ-A users have higher latency. Trade-off of enabling?

A) Without cross-zone, each NLB node sends to own AZ only. Enabling distributes evenly but NLB incurs inter-AZ charges.
B) Static IPs saturated — cross-zone adds more Elastic IPs
C) Cross-zone switches to least-connections algorithm at no cost
D) Redistribute instances evenly instead

**Your answer: A** — Correct. NLB cross-zone distributes evenly across all 10 instances but charges for inter-AZ data transfer.

---

### Q8 ✅ — Connection Draining = Deregistration Delay (connection-draining)
**Question:** Migrating from CLB "Connection Draining" 120s to ALB equivalent.

A) ALB "Connection Draining" on listener
B) ALB "Deregistration Delay" on target group — set to 120s
C) ALB "Idle Timeout" on ALB itself
D) ALB doesn't support this — use sticky sessions

**Your answer: B** — Correct. Same feature, different name. Configured at target group level. Default 300s, range 0-3600s.

---

### Q9 ✗ — Route 53 health check immediate removal vs weight change (dns:route53-health-checks)
**Question:** Route 53 weighted 80/20. Planned maintenance on US-East-1. Fastest failover to EU-West-1.

A) Set weight to 0/100 — clients stop after TTL
B) Route 53 health check failure — immediately stops returning unhealthy record
C) Scale ASG to 0 — ALB returns 503 triggering health check
D) Delete US-East-1 record

**Your answer: A** — Incorrect. Correct: B. Health check failure = immediate removal from DNS responses. Weight change = depends on TTL expiration. Health check is faster.

---

### Q10 ✅ — ECS canary with ALB weighted target groups (alb-weighted-target-groups | compute:ecs-fargate)
**Question:** ECS Fargate canary: 10% to new version, validate, then 100%. Which ALB feature?

A) Path-based routing to /payments/canary/*
B) ALB weighted target groups — 90/10 split between old and new TGs
C) Host-based routing to canary.payments.internal
D) ECS deployment config maximumPercent/minimumHealthyPercent

**Your answer: B** — Correct. ALB weighted target groups for percentage-based canary. ECS services register to separate TGs.

---

## Summary
- **Score:** 9/10 (90%) — PASSED
- **Missed topics:** dns:route53-health-checks
- **Mastered from previous miss:** asg-scaling-policies, alb-weighted-target-groups, nlb-health-checks, alb-health-checks
- **Key lesson:** Route 53 health check failure immediately removes record from DNS responses — faster than weight changes which depend on client TTL cache expiration. This is a persistent weak spot across P3 and P4.
