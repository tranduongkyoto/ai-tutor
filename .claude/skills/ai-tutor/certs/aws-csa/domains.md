---
certification: aws-csa
exam_code: SAA-C03
total_domains: 12
pdf_base_path: sections/
---

# AWS CSA (SAA-C03) - Domain Configuration

## Cheat Sheet

cheat-sheet:
  name: "SAA-C03 Master Cheat Sheet"
  pdf: sections/AWS-SAA-Master-Cheat-Sheet.pdf
  description: "Cross-domain exam-focused decision frameworks, organized by SAA-C03 exam domains (Secure 30%, Resilient 26%, High-Performing 24%, Cost-Optimized 20%)"

## Domains

### compute
- name: Compute
- pdfs: [03-amazon-ec2-basics.pdf, 04-amazon-ec2-associate.pdf, 16-containers-on-aws.pdf]
- topics: [instance-types, security-groups, purchasing-options, placement-groups, elastic-network-interface (ENI), hibernate, elastic-container-service (ECS), elastic-kubernetes-service (EKS), fargate]

### storage
- name: Storage
- pdfs: [05-amazon-ec2-instance-storage.pdf, 10-amazon-s3.pdf, 11-amazon-s3-advanced.pdf, 12-amazon-s3-security.pdf, 14-aws-storage-extras.pdf]
- topics: [elastic-block-store (EBS) types, elastic-block-store (EBS) snapshots, elastic-file-system (EFS), simple-storage-service (S3) classes, simple-storage-service (S3) lifecycle, simple-storage-service (S3) security, FSx, snow-family, storage-gateway]

### databases
- name: Databases
- pdfs: [07-rds-aurora-elasticache.pdf, 19-databases-in-aws.pdf]
- topics: [relational-database-service (RDS), aurora, elasticache, dynamodb, relational-database-service (RDS) proxy, documentdb, neptune, keyspaces, quantum-ledger-database (QLDB), timestream]

### networking
- name: Networking
- pdfs: [25-amazon-vpc.pdf]
- topics: [virtual-private-cloud (VPC), subnets, network-access-control-list (NACL) vs security-group (SG), network-address-translation (NAT) gateway, virtual-private-cloud (VPC) peering, virtual-private-cloud (VPC) endpoints, direct-connect (DX), transit-gateway, flow-logs]

### security-identity
- name: Security & Identity
- pdfs: [02-aws-iam.pdf, 23-advanced-identity-in-aws.pdf, 24-aws-security-and-encryption.pdf]
- topics: [identity-and-access-management (IAM), organizations, service-control-policy (SCP), key-management-service (KMS), systems-manager (SSM) parameter-store, web-application-firewall (WAF), shield, guardduty, inspector, macie, cognito]

### load-balancing-scaling
- name: Load Balancing & Scaling
- pdfs: [06-high-availability-and-scalability.pdf]
- topics: [application-load-balancer (ALB), network-load-balancer (NLB), gateway-load-balancer (GWLB), auto-scaling-group (ASG), sticky-sessions, cross-zone-load-balancing, ssl-server-name-indication (SNI), connection-draining]

### dns
- name: DNS
- pdfs: [08-amazon-route-53.pdf]
- topics: [route-53-records, routing-policies, health-checks, alias-vs-cname, hybrid-dns]

### integration-messaging
- name: Integration & Messaging
- pdfs: [15-aws-integration-and-messaging.pdf]
- topics: [simple-queue-service (SQS), simple-notification-service (SNS), kinesis-data-streams, kinesis-data-firehose, fan-out-pattern, amazon-mq]

### serverless
- name: Serverless
- pdfs: [17-serverless-overview.pdf, 18-serverless-architectures.pdf]
- topics: [lambda, api-gateway, step-functions, cognito, lambda-at-edge, cloudfront-functions]

### monitoring-audit
- name: Monitoring & Audit
- pdfs: [22-aws-monitoring-audit-performance.pdf]
- topics: [cloudwatch, cloudtrail, aws-config, eventbridge, cloudwatch-insights]

### data-analytics
- name: Data & Analytics
- pdfs: [20-data-and-analytics.pdf, 21-machine-learning.pdf]
- topics: [athena, redshift, glue, elastic-mapreduce (EMR), quicksight, lake-formation, managed-streaming-for-kafka (MSK), machine-learning-services]

### dr-architecture
- name: Disaster Recovery & Architecture
- pdfs: [09-classic-solutions-architecture.pdf, 26-disaster-recovery-and-migrations.pdf, 27-more-solutions-architecture.pdf, 28-other-services.pdf, 29-white-papers-and-architectures.pdf]
- topics: [disaster-recovery (DR) strategies, database-migration-service (DMS), aws-backup, elastic-beanstalk, cloudformation, high-performance-computing (HPC), well-architected-framework]
