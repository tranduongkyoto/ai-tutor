# Load Balancing & Scaling — Scenario Generator (Phase 3)
**Date:** 2026-05-19 14:21
**Domain:** Load Balancing & Scaling
**Scenarios:** 8 (path-based-vs-host-based-routing, alb-vs-nlb-decision, ultra-low-latency-tcp-scenarios, third-party-appliance-integration, scaling-policies-target-vs-step-vs-simple, predictive-scaling, session-affinity-trade-offs, cross-az-traffic-distribution, multi-domain-ssl-on-single-alb, graceful-deregistration-scenarios)

---

## Scenarios

### Scenario 1: Path-Based vs Host-Based Routing / ALB vs NLB Decision

**Context:** SaaS company migrating to microservices with 3 HTTP services (`/api/users`, `/api/orders`, WebSocket feed) plus a TCP-based gRPC service requiring IP whitelisting.

**Requirements:** Single entry point for HTTP microservices with path-based routing, WebSocket support, static IP for gRPC.

**Question:** Which architecture?

A) One ALB for all four services with TCP listener for gRPC
B) One ALB for HTTP/WebSocket + one NLB with Elastic IPs for gRPC
C) Four separate CLBs with Route 53 weighted routing
D) One NLB for all services with path-based routing

**Answer: B** — ALB handles Layer 7 (path routing, WebSocket). NLB handles Layer 4 TCP (gRPC, static IP for whitelisting). ALB can't do raw TCP; NLB can't do path routing.

**Why others wrong:**
- A) ALB cannot handle raw TCP/gRPC — Layer 7 HTTP only
- C) CLBs are legacy, no path-based routing, operationally complex
- D) NLB doesn't support path-based routing — Layer 4 only

**Key Concept:** ALB = L7 HTTP routing. NLB = L4 TCP/UDP + static IPs. Use both when you need both.

---

### Scenario 2: Ultra-Low Latency TCP Scenarios

**Context:** High-frequency trading firm, millions of transactions/sec over raw TCP, sub-millisecond latency required, IP whitelisting for partner exchanges, 3 AZs.

**Question:** Which load balancer configuration?

A) ALB with HTTPS listeners
B) NLB with TCP listeners, one Elastic IP per AZ, Security Group IP restrictions
C) GWLB with TCP passthrough
D) CLB with TCP listeners and NACLs

**Answer: B** — NLB: millions req/sec, ultra-low latency L4, static IP per AZ (3 EIPs), SG for IP whitelisting.

**Why others wrong:**
- A) ALB adds L7 processing overhead, higher latency for raw TCP
- C) GWLB for traffic inspection via 3rd-party appliances, not app load balancing
- D) CLB legacy, lower performance than NLB; NACLs have rule limits

**Key Concept:** NLB = millions req/sec + ultra-low latency + static IP per AZ for high-performance TCP.

---

### Scenario 3: Third-Party Appliance Integration

**Context:** Government agency must inspect ALL traffic through Palo Alto firewall fleet before reaching web app. Transparent, auto-scaling, no app changes.

**Question:** Which architecture?

A) Palo Alto as EC2 in public subnet with route table manipulation
B) GWLB as transparent gateway → Palo Alto fleet target group → route tables through GWLB
C) AWS Network Firewall in front of ALB
D) ALB with WAF rules replicating Palo Alto

**Answer: B** — GWLB = transparent network gateway + load balancer for 3rd-party appliances. GENEVE port 6081. Route tables direct traffic through GWLB.

**Why others wrong:**
- A) Manual EC2 firewalls don't auto-scale, single point of failure
- C) Network Firewall is AWS-managed, not 3rd-party Palo Alto
- D) WAF is L7 HTTP only, can't replicate full L3-7 inspection

**Key Concept:** GWLB = transparent gateway for 3rd-party network virtual appliances. GENEVE on port 6081.

---

### Scenario 4: Scaling Policies — Target Tracking vs Step vs Simple

**Context:** E-commerce with 3 needs: (1) maintain 50% CPU normally, (2) add 5 instances at 85% CPU during flash sales, (3) pre-scale to 20 instances every Friday 4 PM.

**Question:** Which combination?

A) Three Target Tracking policies
B) Target Tracking (50% CPU) + Step Scaling (+5 at >85%) + Scheduled Scaling (Fri 4 PM, min=20)
C) Predictive Scaling for all three
D) Simple Scaling (50% CPU) + Step Scaling (85%) + Predictive Scaling (Friday)

**Answer: B** — Each scaling type for its strength: Target Tracking (maintain metric), Step (alarm + specific count), Scheduled (known recurring time). Can combine on one ASG.

**Why others wrong:**
- A) Target Tracking can't add specific instance count or schedule
- C) Predictive can't do immediate flash sale response
- D) Simple has cooldown issues; Predictive doesn't replace Scheduled for fixed known events

**Key Concept:** Combine scaling policies: Target Tracking (maintain), Step (alarm response), Scheduled (known events), Predictive (ML forecast).

---

### Scenario 5: Predictive Scaling

**Context:** Streaming platform with daily evening surges (7-11 PM) and weekend peaks. 5-minute instance warm-up causes slow responses during ramp-up.

**Question:** Which scaling approach?

A) Lower Target Tracking to 30% CPU
B) Predictive Scaling — ML analyzes historical patterns, pre-launches before surge
C) 14 Scheduled Scaling actions (daily start/end)
D) Simple Scaling with lower CPU alarm threshold

**Answer: B** — Predictive Scaling uses ML to forecast from historical data, launches instances BEFORE traffic arrives. Eliminates 5-min warm-up impact. Adapts to changing patterns.

**Why others wrong:**
- A) Still reactive; wastes resources off-peak
- C) Operationally heavy (14 manual actions), doesn't adapt
- D) Still reactive; cooldown period adds delay

**Key Concept:** Predictive Scaling = ML proactive scaling for recurring patterns. Combine with Target Tracking as backup.

---

### Scenario 6: Session Affinity Trade-offs

**Context:** Legacy app stores sessions in local server memory behind ALB with 6 instances. Users randomly logged out on subsequent requests.

**Question:** Fix and trade-off?

A) Enable sticky sessions (AWSALB cookie); trade-off: load imbalance
B) Enable cross-zone LB; trade-off: inter-AZ charges
C) NLB in front of ALB for client IP; trade-off: lose L7 routing
D) Connection draining 3600s; trade-off: instances can't terminate

**Answer: A** — Sticky sessions route same client to same instance via AWSALB cookie. Fixes in-memory session issue. Trade-off: uneven load distribution.

**Why others wrong:**
- B) Cross-zone distributes NEW connections evenly, doesn't maintain session affinity
- C) NLB client IP doesn't map to server-side sessions
- D) Connection draining only during de-registration, not normal operations

**Key Concept:** Sticky sessions: AWSALB (duration, set by LB), AWSALBAPP (application, set by app). Trade-off: load imbalance. Better fix: externalize sessions to ElastiCache/DynamoDB.

---

### Scenario 7: Cross-AZ Traffic Distribution

**Context:** ALB across 2 AZs. AZ-a: 2 instances (25 req each). AZ-b: 8 instances (6.25 req each). Total 100 requests. Imbalanced.

**Question:** Cause and fix?

A) ALB bug — recreate
B) Cross-zone LB disabled — each AZ node only routes within its AZ. Enable it.
C) Change algorithm to least-connections
D) AZ-b health checks failing

**Answer: B** — Without cross-zone: 50/50 AZ split → 25 each in AZ-a, 6.25 each in AZ-b. With cross-zone: all 10 instances get 10 each. ALB defaults enabled, but can be disabled at TG level.

**Why others wrong:**
- A) Expected behavior when cross-zone disabled, not a bug
- C) ALB doesn't offer least-connections algorithm
- D) Failing health checks → 0 traffic, not 6.25

**Key Concept:** Cross-zone LB distributes across ALL instances in ALL AZs. ALB: enabled/free. NLB/GWLB: disabled/charged. CLB: disabled/free.

---

### Scenario 8: Multi-Domain SSL + Graceful Deregistration

**Context:** 3 brands (news/sports/entertainment.example.com) on one ALB, each with own ACM cert. 502 errors during deployments from terminated 5-min video uploads.

**Question:** SSL config and deployment fix?

A) Three separate ALBs; Deregistration Delay 300s
B) ALB with SNI for 3 certs; Deregistration Delay ≥ 300s for in-flight uploads
C) Wildcard cert; disable Deregistration Delay for fast deploys
D) NLB with TLS listeners; Connection Draining 5 min

**Answer: B** — SNI on ALB supports multiple SSL certs per LB. Deregistration Delay (default 300s) lets in-flight uploads complete before instance removal. Set ≥ longest request duration.

**Why others wrong:**
- A) Three ALBs unnecessarily expensive; SNI solves multi-cert on one ALB
- C) Disabling Deregistration Delay worsens 502s (immediate termination)
- D) NLB can't do host-based routing; Connection Draining is CLB terminology

**Key Concept:** SNI on ALB = multiple SSL certs. Deregistration Delay (ALB/NLB) = Connection Draining (CLB). Default 300s, range 1-3600s. Set ≥ longest request.
