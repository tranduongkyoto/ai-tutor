# Load Balancing & Scaling — Mini Exam: Concepts (Phase 2)
**Date:** 2026-05-19 14:18
**Score:** 9/10 (90%)
**Scope:** concepts — service features, limits, comparisons

---

## Questions & Results

### Q1 ✓ — ALB Content-Based Routing (application-load-balancer)
**Question:** Which Elastic Load Balancer (ELB) type supports routing requests based on URL path, hostname, and query string parameters?

A) Classic Load Balancer (CLB)
B) Application Load Balancer (ALB)
C) Network Load Balancer (NLB)
D) Gateway Load Balancer (GWLB)

**Your answer: B** — Correct. ALB operates at Layer 7 (HTTP) and supports content-based routing: URL path, hostname, query strings, HTTP headers.

---

### Q2 ✓ — NLB Static IP (network-load-balancer)
**Question:** Which load balancer type provides one static IP address per Availability Zone (AZ) and supports assigning Elastic IPs for IP whitelisting?

A) Application Load Balancer (ALB)
B) Classic Load Balancer (CLB)
C) Network Load Balancer (NLB)
D) Gateway Load Balancer (GWLB)

**Your answer: C** — Correct. NLB provides one static IP per AZ and supports Elastic IP assignment.

---

### Q3 ✓ — Cross-Zone Load Balancing Defaults (cross-zone-load-balancing)
**Question:** What is the default cross-zone load balancing setting for each ELB type? (Select TWO)

A) ALB: enabled by default, no inter-AZ data charges
B) NLB: enabled by default, no inter-AZ data charges
C) CLB: disabled by default, charges apply if enabled
D) NLB: disabled by default, charges apply if enabled

**Your answer: A, D** — Correct. ALB = enabled/free. NLB = disabled/charged. CLB = disabled/free.

---

### Q4 ✓ — GWLB Protocol (gateway-load-balancer)
**Question:** Which protocol and port does GWLB use?

A) HTTP on port 80
B) TCP on port 443
C) GENEVE on port 6081
D) GRE on port 47

**Your answer: C** — Correct. GWLB uses GENEVE protocol on port 6081.

---

### Q5 ✓ — Client IP Behind ALB (application-load-balancer)
**Question:** Backend EC2 instances behind ALB need to log client's real IP. How?

A) Configure ALB transparent mode
B) Read X-Forwarded-For HTTP header
C) Enable NLB mode on ALB
D) Configure proxy_protocol_v2

**Your answer: B** — Correct. ALB terminates connections; original client IP is in the X-Forwarded-For header.

---

### Q6 ✓ — NLB Target Group: ALB (network-load-balancer)
**Question:** Which is a valid NLB target group configuration?

A) Lambda functions
B) Application Load Balancer (ALB)
C) ECS tasks
D) CloudFront distributions

**Your answer: B** — Correct. NLB can target ALB (stacking pattern for static IP + HTTP routing). Lambda and ECS are ALB-only targets.

---

### Q7 ✗ — Connection Draining vs Deregistration Delay (connection-draining)
**Question:** What is the difference between Connection Draining and Deregistration Delay?

A) Connection Draining for terminating instances, Deregistration Delay for adding
B) Same feature, different names — Connection Draining for CLB, Deregistration Delay for ALB/NLB
C) Connection Draining defaults 60s, Deregistration Delay defaults 300s
D) Connection Draining stops new requests only, Deregistration Delay terminates in-flight

**Your answer: C** — Incorrect. Correct answer: B. They are the SAME feature with different names. Both default to 300 seconds (range 1-3600, disable with 0). CLB uses "Connection Draining," ALB/NLB use "Deregistration Delay."

---

### Q8 ✓ — Predictive Scaling (auto-scaling-group)
**Question:** Which ASG scaling policy uses ML to analyze historical patterns and schedule scaling ahead of demand?

A) Target Tracking Scaling
B) Simple / Step Scaling
C) Scheduled Scaling
D) Predictive Scaling

**Your answer: D** — Correct. Predictive Scaling uses ML to forecast from historical data and proactively schedule scaling.

---

### Q9 ✓ — ASG Cooldown Period (auto-scaling-group)
**Question:** What happens during the ASG cooldown period?

A) Terminates recently launched instances
B) Pauses all scaling, letting metrics stabilize
C) Scales at reduced rate (50%)
D) Disables CloudWatch alarms temporarily

**Your answer: B** — Correct. During cooldown (default 300s), ASG ignores scaling requests to let metrics stabilize.

---

### Q10 ✓ — SNI Support Matrix (ssl-server-name-indication)
**Question:** Which statement about SNI support is correct?

A) All ELB types support SNI
B) Only ALB supports SNI
C) ALB and NLB support SNI; CLB does NOT
D) Only NLB supports SNI

**Your answer: C** — Correct. ALB and NLB support SNI (multiple SSL certs). CLB requires one CLB per certificate.

---

## Summary
- **Score:** 9/10 (90%)
- **Missed topics:** connection-draining
- **Strong areas:** application-load-balancer, network-load-balancer, gateway-load-balancer, cross-zone-load-balancing, auto-scaling-group, ssl-server-name-indication
- **Key lessons:**
  - Connection Draining (CLB) and Deregistration Delay (ALB/NLB) are the SAME feature with different names. Both default to 300 seconds.
