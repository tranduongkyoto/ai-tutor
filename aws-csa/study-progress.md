---
started: 2026-05-11
last_session: 2026-05-15
total_sessions: 18
domains:
  storage:
    sessions_count: 1
    modes_completed: [concept-mapper]
    last_studied: 2026-05-15
    current_phase: 1
    exams: []
    phase_scores: {}
    weak_topics: []
  networking:
    sessions_count: 6
    modes_completed: [concept-mapper, mini-exam:concepts, scenario-generator, mini-exam:scenarios, mini-exam:design, mini-exam:comprehensive]
    last_studied: 2026-05-15
    current_phase: 6
    completed: true
    exams: [{scope: concepts, score: 9, total: 10, pct: 90, date: 2026-05-15}, {scope: scenarios, score: 9, total: 10, pct: 90, date: 2026-05-15}, {scope: design, score: 6, total: 10, pct: 60, date: 2026-05-15}, {scope: comprehensive, score: 9, total: 10, pct: 90, date: 2026-05-15}]
    phase_scores: {p2: 90, p4: 90, p5: 60, p6: 90}
    weak_topics: [direct-connect-gateway]
  compute:
    sessions_count: 11
    modes_completed: [concept-mapper, mini-exam:concepts, scenario-generator, mini-exam:scenarios, hands-on-lab, mini-exam:design, mini-exam:comprehensive]
    last_studied: 2026-05-14
    current_phase: 6
    completed: true
    exams: [{scope: concepts, score: 7, total: 10, pct: 70, date: 2026-05-12}, {scope: scenarios, score: 9, total: 10, pct: 90, date: 2026-05-12}, {scope: design, score: 8, total: 10, pct: 80, date: 2026-05-14}, {scope: comprehensive, score: 10, total: 10, pct: 100, date: 2026-05-14}]
    phase_scores: {p2: 70, p4: 90, p5: 80, p6: 100}
    weak_topics: []
---

# AWS CSA (SAA-C03) — Study Progress

## Session History

### 2026-05-11 16:13 | Compute | Concept Mapper
- Topics: instance-types, security-groups, purchasing, placement-groups, eni, hibernate, ecs, eks, fargate, ecr, app-runner, app2container
- Output: study-sessions/260511-1613-compute-concept-mapper.md

### 2026-05-11 17:13 | Compute | Concept Mapper (Repeat)
- Topics: instance-types, security-groups, purchasing, placement-groups, eni, hibernate, ecs, eks, fargate, ecr, app-runner, app2container
- Output: study-sessions/260511-1713-compute-concept-mapper.md

### 2026-05-11 18:17 | Compute | Concept Mapper (Repeat)
- Topics: instance-types, security-groups, purchasing, placement-groups, eni, hibernate, ecs, eks, fargate, ecr, app-runner, app2container
- Output: study-sessions/260511-1817-compute-concept-mapper.md

### 2026-05-12 08:21 | Compute | Concept Mapper (Repeat)
- Topics: instance-types, security-groups, purchasing, placement-groups, eni, hibernate, ecs, eks, fargate, ecr, app-runner, app2container
- Output: study-sessions/260512-0821-compute-concept-mapper.md

### 2026-05-12 08:58 | Compute | Mini Exam (Phase 2: Concepts)
- Score: 7/10 (70%)
- Missed: placement-groups, hibernate, security-groups
- Output: study-sessions/260512-0858-compute-mini-exam.md

### 2026-05-12 12:35 | Compute | Scenario Generator (Phase 3)
- Scenarios: 5 (batch processing, HA placement, container migration, BYOL licensing, event-driven pipeline)
- Key concepts: Spot Fleet strategies, Cluster PG limits, ECS vs EKS, Dedicated Hosts vs Instances, S3→EventBridge→Fargate
- Output: study-sessions/260512-1235-compute-scenario-generator.md

### 2026-05-12 15:55 | Compute | Scenario Generator (Phase 3 Repeat)
- Scenarios: 14 (full scenario map coverage)
- Key concepts: instance families, GPU/memory selection, T-instance credits, Spot vs Reserved, Savings Plans vs RIs, Dedicated Hosts vs Instances, Placement Groups, cross-SG references, ENI failover, Hibernate requirements, ECS EC2 vs Fargate, Task Role vs Instance Profile, EKS vs ECS, Fargate sizing/cost
- Output: study-sessions/260512-1555-compute-scenario-generator.md

### 2026-05-12 15:55 | Compute | Mini Exam (Phase 4: Scenarios)
- Score: 9/10 (90%)
- Missed: elastic-container-service (ECS) — Cluster Capacity Provider vs Service Auto Scaling
- Output: (inline session)

### 2026-05-14 12:37 | Compute | Mini Exam (Phase 5: Design)
- Score: 8/10 (80%)
- Missed: purchasing-options (Dedicated Hosts vs Instances), elastic-container-service (ECS) (App Runner)
- Output: study-sessions/260514-1237-compute-mini-exam-design.md

### 2026-05-14 12:55 | Compute | Mini Exam (Phase 6: Comprehensive Final)
- Score: 10/10 (100%)
- Missed: none
- Output: study-sessions/260514-1255-compute-mini-exam-comprehensive.md

### 2026-05-15 08:51 | Networking | Concept Mapper (Phase 1)
- Topics: vpc, subnets, igw, nat-gateway, nat-instance, nacl, security-groups, vpc-peering, vpc-endpoints, flow-logs, site-to-site-vpn, direct-connect, transit-gateway, egress-only-igw, network-firewall
- Output: study-sessions/260515-0851-networking-concept-mapper.md

### 2026-05-15 10:16 | Networking | Mini Exam (Phase 2: Concepts)
- Score: 9/10 (90%)
- Missed: nat-instance (Source/Destination Check)
- Output: study-sessions/260515-1016-networking-mini-exam.md

### 2026-05-15 10:21 | Networking | Scenario Generator (Phase 3)
- Scenarios: 9 (multi-vpc-design, cidr-planning, public-vs-private-subnet, nacl-vs-sg-filtering, nat-gateway-ha, peering-vs-tgw, gateway-vs-interface-endpoints, tgw-hub-spoke-multicast-ecmp, flow-log-troubleshooting)
- Key concepts: TGW route table isolation, CIDR overlap avoidance, 3-tier subnet placement, NACL stateless DENY rules, NAT GW per-AZ HA, TGW peering cross-region, Gateway Endpoint free for S3/DynamoDB, IP Multicast only on TGW, Flow Log ACCEPT+REJECT diagnosis
- Output: study-sessions/260515-1021-networking-scenario-generator.md

### 2026-05-15 11:55 | Networking | Mini Exam (Phase 4: Scenarios)
- Score: 9/10 (90%)
- Missed: direct-connect (DX backup timing — second DX >1 month, S2S VPN is fast backup)
- Output: study-sessions/260515-1155-networking-mini-exam-scenarios.md

### 2026-05-15 16:43 | Networking | Mini Exam (Phase 5: Design)
- Score: 6/10 (60%)
- Missed: direct-connect (MACsec encryption, Hosted DX burst, Snowball for large migration), nacl-vs-sg (SCP preventive control > SG for defense-in-depth)
- Output: study-sessions/260515-1643-networking-mini-exam-design.md

### 2026-05-15 22:38 | Networking | Mini Exam (Phase 6: Comprehensive Final)
- Score: 9/10 (90%)
- Missed: direct-connect-gateway (DX Gateway for multi-region VPC connectivity)
- Output: study-sessions/260515-2238-networking-mini-exam-comprehensive.md

### 2026-05-15 23:42 | Storage | Concept Mapper (Phase 1)
- Topics: ebs-types, ebs-snapshots, instance-store, efs, s3-classes, s3-security, s3-versioning, s3-replication, s3-lifecycle, s3-performance, s3-event-notifications, s3-analytics, s3-access-points, s3-object-lambda, fsx, snow-family, storage-gateway
- Output: study-sessions/260515-2342-storage-concept-mapper.md
