---
certification: aws-csa
exam_code: SAA-C03
total_domains: 12
pdf_base_path: sections/
---

# AWS CSA (SAA-C03) - Domain Configuration

## Domains

### compute
- name: Compute
- pdfs: [03-amazon-ec2-basics.pdf, 04-amazon-ec2-associate.pdf, 16-containers-on-aws.pdf]
- topics: [instance-types, security-groups, purchasing, placement-groups, eni, hibernate, ecs, eks, fargate]

### storage
- name: Storage
- pdfs: [05-amazon-ec2-instance-storage.pdf, 10-amazon-s3.pdf, 11-amazon-s3-advanced.pdf, 12-amazon-s3-security.pdf, 14-aws-storage-extras.pdf]
- topics: [ebs-types, ebs-snapshots, efs, s3-classes, s3-lifecycle, s3-security, fsx, snow-family, storage-gateway]

### databases
- name: Databases
- pdfs: [07-rds-aurora-elasticache.pdf, 19-databases-in-aws.pdf]
- topics: [rds, aurora, elasticache, dynamodb, rds-proxy, documentdb, neptune, keyspaces, qldb, timestream]

### networking
- name: Networking
- pdfs: [25-amazon-vpc.pdf]
- topics: [vpc, subnets, nacl-vs-sg, nat-gateway, vpc-peering, vpc-endpoints, dx, transit-gateway, flow-logs]

### security-identity
- name: Security & Identity
- pdfs: [02-aws-iam.pdf, 23-advanced-identity-in-aws.pdf, 24-aws-security-and-encryption.pdf]
- topics: [iam, organizations, scp, kms, ssm-params, waf, shield, guardduty, inspector, macie, cognito]

### load-balancing-scaling
- name: Load Balancing & Scaling
- pdfs: [06-high-availability-and-scalability.pdf]
- topics: [alb, nlb, gwlb, asg, sticky-sessions, cross-zone, ssl-sni, connection-draining]

### dns
- name: DNS
- pdfs: [08-amazon-route-53.pdf]
- topics: [route53-records, routing-policies, health-checks, alias-vs-cname, hybrid-dns]

### integration-messaging
- name: Integration & Messaging
- pdfs: [15-aws-integration-and-messaging.pdf]
- topics: [sqs, sns, kinesis-streams, kinesis-firehose, fan-out, amazon-mq]

### serverless
- name: Serverless
- pdfs: [17-serverless-overview.pdf, 18-serverless-architectures.pdf]
- topics: [lambda, api-gateway, step-functions, cognito, lambda-edge, cloudfront-functions]

### monitoring-audit
- name: Monitoring & Audit
- pdfs: [22-aws-monitoring-audit-performance.pdf]
- topics: [cloudwatch, cloudtrail, config, eventbridge, insights]

### data-analytics
- name: Data & Analytics
- pdfs: [20-data-and-analytics.pdf, 21-machine-learning.pdf]
- topics: [athena, redshift, glue, emr, quicksight, lake-formation, msk, ml-services]

### dr-architecture
- name: DR & Architecture
- pdfs: [09-classic-solutions-architecture.pdf, 26-disaster-recovery-and-migrations.pdf, 27-more-solutions-architecture.pdf, 28-other-services.pdf, 29-white-papers-and-architectures.pdf]
- topics: [dr-strategies, dms, backup, beanstalk, cloudformation, hpc, well-architected]
