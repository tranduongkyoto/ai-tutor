---
started: 2026-05-11
last_session: 2026-05-26
total_sessions: 34
domains:
  security-identity:
    sessions_count: 6
    modes_completed: [concept-mapper, mini-exam:concepts, scenario-generator, mini-exam:scenarios, mini-exam:design, mini-exam:comprehensive]
    last_studied: 2026-05-19
    current_phase: 6
    completed: true
    exams: [{scope: concepts, score: 9, total: 10, pct: 90, date: 2026-05-18}, {scope: scenarios, score: 8, total: 10, pct: 80, date: 2026-05-18}, {scope: design, score: 7, total: 10, pct: 70, date: 2026-05-19}, {scope: comprehensive, score: 9, total: 10, pct: 90, date: 2026-05-19}]
    phase_scores: {p2: 90, p4: 80, p5: 70, p6: 90}
    weak_topics: [iam]
  storage:
    sessions_count: 6
    modes_completed: [concept-mapper, mini-exam:concepts, scenario-generator, mini-exam:scenarios, mini-exam:design, mini-exam:comprehensive]
    last_studied: 2026-05-18
    current_phase: 6
    completed: true
    exams: [{scope: concepts, score: 8, total: 10, pct: 80, date: 2026-05-16}, {scope: scenarios, score: 6, total: 10, pct: 60, date: 2026-05-16}, {scope: design, score: 6, total: 10, pct: 60, date: 2026-05-17}, {scope: comprehensive, score: 9, total: 10, pct: 90, date: 2026-05-18}]
    phase_scores: {p2: 80, p4: 60, p5: 60, p6: 90}
    weak_topics: [s3-encryption]
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
  load-balancing-scaling:
    sessions_count: 4
    modes_completed: [concept-mapper, mini-exam:concepts, scenario-generator, mini-exam:scenarios]
    last_studied: 2026-05-19
    current_phase: 2
    exams: [{scope: concepts, score: 9, total: 10, pct: 90, date: 2026-05-19}, {scope: scenarios, score: 9, total: 10, pct: 90, date: 2026-05-19}]
    phase_scores: {p1: 90, p2: 90}
    weak_topics: [connection-draining]
  databases:
    sessions_count: 1
    modes_completed: [concept-mapper]
    last_studied: 2026-05-26
    current_phase: 1
    exams: []
    phase_scores: {}
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

### 2026-05-16 01:14 | Storage | Mini Exam (Phase 2: Concepts)
- Score: 8/10 (80%)
- Missed: storage-gateway (Tape Gateway for tape workflows), ebs-multi-attach (io1/io2 only)
- Output: study-sessions/260516-0114-storage-mini-exam-concepts.md

### 2026-05-16 04:06 | Storage | Scenario Generator (Phase 3)
- Scenarios: 12 (gp3-vs-io2-vs-st1, provisioned-iops-sizing, cross-region-copy-lifecycle, efs-vs-ebs-vs-fsx, standard-vs-ia-vs-glacier, intelligent-tiering, transition-rules-expiration, bucket-policy-vs-acl-vs-iam, encryption-sse-s3-vs-sse-kms, fsx-lustre-vs-windows-vs-efs, snowcone-vs-snowball-vs-snowmobile, file-vs-volume-vs-tape-gateway)
- Key concepts: EBS type matching, io2 Block Express for >64K IOPS, Snapshot Archive lifecycle, FSx Lustre for HPC, S3 class selection by access pattern, Intelligent-Tiering for unpredictable patterns, lifecycle chain with minimum periods, BPA must be OFF for public access, SSE-KMS+CMK for audit/rotation/revocation, Snow Family sizing, Storage Gateway type mapping
- Output: study-sessions/260516-0406-storage-scenario-generator.md

### 2026-05-16 05:31 | Storage | Mini Exam (Phase 4: Scenarios)
- Score: 6/10 (60%)
- Missed: s3-security (Object Lock Compliance vs Governance, SSE-C vs SSE-KMS key storage), s3-performance (prefix hot spots, small files problem), s3-lifecycle (minimum storage period penalties)
- Output: study-sessions/260516-0531-storage-mini-exam-scenarios.md

### 2026-05-17 01:13 | Storage | Mini Exam (Phase 5: Design)
- Score: 6/10 (60%)
- Missed: s3-performance (Firehose inline conversion), s3-lifecycle (Glacier Instant 90d min vs Standard-IA 30d), s3-security (bucket policy VPC condition + cross-account exception), snow-family (Snowcone limits vs Snowball Edge)
- Output: study-sessions/260517-0113-storage-mini-exam-design.md

### 2026-05-18 11:54 | Storage | Mini Exam (Phase 6: Comprehensive Final)
- Score: 9/10 (90%)
- Missed: s3-encryption (S3 Bucket Keys for reducing KMS ThrottlingException)
- Output: study-sessions/260518-1154-storage-mini-exam-comprehensive.md

### 2026-05-18 17:38 | Security & Identity | Concept Mapper (Phase 1)
- Topics: iam, organizations, scp, iam-identity-center, control-tower, kms, cloudhsm, acm, ssm-parameter-store, secrets-manager, waf, shield, firewall-manager, guardduty, inspector, macie
- Output: study-sessions/260518-1738-security-identity-concept-mapper.md

### 2026-05-18 11:42 | Security & Identity | Mini Exam (Phase 2: Concepts)
- Score: 9/10 (90%)
- Missed: acm (ACM imported certs no auto-renewal, Edge-Optimized API GW requires us-east-1)
- Output: study-sessions/260518-1142-security-identity-mini-exam-concepts.md

### 2026-05-18 11:45 | Security & Identity | Scenario Generator (Phase 3)
- Scenarios: 11 (cross-account-access, permission-boundaries, scp-inheritance-and-ou-design, deny-vs-allow-strategy, cmk-vs-aws-managed-keys, key-rotation, parameter-store-vs-secrets-manager, waf-rules-for-common-attacks, shield-standard-vs-advanced, threat-detection-and-response, user-pools-vs-identity-pools)
- Key concepts: resource-based policy for simultaneous cross-account access, Permission Boundaries for delegated admin, SCP allowlist vs blocklist per OU, CMK for full key control, Secrets Manager+SSM hybrid, WAF on ALB not NLB, Shield Advanced for L7 DDoS, GuardDuty for crypto mining, Cognito User Pools+Identity Pools
- Output: study-sessions/260518-1145-security-identity-scenario-generator.md

### 2026-05-18 12:54 | Security & Identity | Mini Exam (Phase 4: Scenarios)
- Score: 8/10 (80%)
- Missed: acm (ALB cert same region, Edge API GW us-east-1 vs Regional API GW same region), shield (Standard L3/4 free vs Advanced L7+DRT+cost-protection $3K/month)
- Output: study-sessions/260518-1254-security-identity-mini-exam-scenarios.md

### 2026-05-19 09:53 | Security & Identity | Mini Exam (Phase 5: Design)
- Score: 7/10 (70%)
- Missed: kms-multi-region-keys (DynamoDB Encryption Client + MRK for client-side field-level encryption), waf (CloudFront origin restriction via managed prefix list + custom header), firewall-manager (multi-account WAF/Shield policy orchestrator vs Control Tower governance)
- Output: study-sessions/260519-0953-security-identity-mini-exam-design.md

### 2026-05-19 11:33 | Security & Identity | Mini Exam (Phase 6: Comprehensive Final)
- Score: 9/10 (90%)
- Missed: iam (Lambda resource-based policy vs execution role — resource-based controls invocation, execution role controls access)
- Output: study-sessions/260519-1133-security-identity-mini-exam-comprehensive.md

### 2026-05-19 11:43 | Load Balancing & Scaling | Concept Mapper (Phase 1)
- Topics: application-load-balancer (ALB), network-load-balancer (NLB), gateway-load-balancer (GWLB), classic-load-balancer (CLB), auto-scaling-group (ASG), sticky-sessions, cross-zone-load-balancing, ssl-server-name-indication (SNI), connection-draining
- Output: study-sessions/260519-1143-load-balancing-scaling-concept-mapper.md

### 2026-05-19 14:18 | Load Balancing & Scaling | Mini Exam (Phase 2: Concepts)
- Score: 9/10 (90%)
- Missed: connection-draining (Connection Draining vs Deregistration Delay — same feature, different names, both default 300s)
- Output: study-sessions/260519-1418-load-balancing-scaling-mini-exam-concepts.md

### 2026-05-19 14:21 | Load Balancing & Scaling | Scenario Generator (Phase 3)
- Scenarios: 8 (path-based-vs-host-based-routing, alb-vs-nlb-decision, ultra-low-latency-tcp, third-party-appliance-integration, scaling-policies-target-vs-step-vs-simple, predictive-scaling, session-affinity-trade-offs, cross-az-traffic-distribution, multi-domain-ssl-on-single-alb, graceful-deregistration)
- Key concepts: ALB L7 vs NLB L4 split, NLB static IP for whitelisting, GWLB transparent gateway GENEVE 6081, combine scaling policies (Target Tracking + Step + Scheduled + Predictive), sticky sessions AWSALB cookie trade-off, cross-zone defaults per LB type, SNI multi-cert on ALB, Deregistration Delay ≥ longest request
- Output: study-sessions/260519-1421-load-balancing-scaling-scenario-generator.md

### 2026-05-19 15:36 | Load Balancing & Scaling | Mini Exam (Phase 4: Scenarios)
- Score: 9/10 (90%)
- Missed: sticky-sessions/connection-draining (Deregistration Delay protects in-flight sessions during scale-in; NLB client IP doesn't solve server-side session loss)
- Output: study-sessions/260519-1536-load-balancing-scaling-mini-exam-scenarios.md

### 2026-05-26 16:54 | Databases | Concept Mapper (Phase 1)
- Topics: rds, aurora, elasticache, dynamodb, documentdb, neptune, keyspaces, timestream, rds-proxy, rds-custom, aurora-serverless, aurora-global, babelfish
- Output: study-sessions/260526-1654-databases-concept-mapper.md
