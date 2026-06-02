# Scenario Map — AWS CSA (SAA-C03)

Each array item = one scenario to generate. Scenario generator iterates this list per domain.

## compute
- instance-types: [families-and-sizing, gpu-compute-memory-optimized-selection, burstable-t-instances-credit-system]
- purchasing-options: [spot-vs-reserved-decision, savings-plans-vs-reserved, dedicated-hosts-vs-dedicated-instances]
- placement-groups: [cluster-vs-spread-vs-partition-selection]
- security-groups: [stateful-rules-and-cross-sg-references]
- elastic-network-interface (ENI): [multi-homed-instances-and-failover]
- hibernate: [requirements-limitations-and-use-cases]
- elastic-container-service (ECS): [ec2-vs-fargate-launch-type, task-role-vs-instance-profile]
- elastic-kubernetes-service (EKS): [eks-vs-ecs-decision-criteria]
- fargate: [serverless-container-sizing-and-cost]

### cross-domain-topics
- from: load-balancing-scaling
  topics: [alb-asg-private-subnet-pattern, nlb-static-ip-with-ec2, ecs-dynamic-port-mapping-alb, asg-spot-mixed-instances]
  cheat-sheet-ref: "§3.2 Decoupling Workloads, §3.2 Auto Scaling Metrics"
- from: serverless
  topics: [lambda-vs-fargate-decision, api-gateway-lambda-vs-alb-ec2]
  cheat-sheet-ref: "§2.1 Serverless Technologies, §Quick Ref: Compute"
- from: security-identity
  topics: [iam-instance-profiles, systems-manager-session-manager]
  cheat-sheet-ref: "§1.1 IAM Authorization Model, §1.2 Key Security Services"

## storage
- elastic-block-store (EBS) types: [gp3-vs-io2-vs-st1-selection, provisioned-iops-sizing]
- elastic-block-store (EBS) snapshots: [cross-region-copy-and-lifecycle]
- elastic-file-system (EFS): [efs-vs-ebs-vs-fsx-decision]
- simple-storage-service (S3) classes: [standard-vs-ia-vs-glacier-selection, intelligent-tiering]
- simple-storage-service (S3) lifecycle: [transition-rules-and-expiration]
- simple-storage-service (S3) security: [bucket-policy-vs-acl-vs-iam, encryption-sse-s3-vs-sse-kms]
- FSx: [fsx-lustre-vs-fsx-windows-vs-efs]
- snow-family: [snowcone-vs-snowball-vs-snowmobile]
- storage-gateway: [file-vs-volume-vs-tape-gateway]

### cross-domain-topics
- from: security-identity
  topics: [s3-encryption-sse-s3-vs-kms-vs-c, s3-bucket-policy-vpc-endpoints, kms-key-policies-cross-account]
  cheat-sheet-ref: "§1.3 Encrypting Data at Rest, §1.3 Key Management Considerations"
- from: networking
  topics: [cloudfront-s3-oai-oac, s3-gateway-endpoint-vs-interface, vpc-endpoint-for-s3]
  cheat-sheet-ref: "§3.4 Scalable Network Configurations, §4.4 CDN and Edge Caching"
- from: data-analytics
  topics: [athena-s3-query, glue-etl-s3-pipeline, s3-data-lake-formation]
  cheat-sheet-ref: "§3.5 Building Data Lakes, §Quick Ref: Storage"

## databases
- relational-database-service (RDS): [multi-az-vs-read-replicas, engine-selection]
- aurora: [aurora-vs-rds-decision, aurora-serverless-use-cases, aurora-global-database]
- elasticache: [redis-vs-memcached, caching-strategies]
- dynamodb: [partition-key-design, capacity-modes, dax-acceleration, global-tables]
- relational-database-service (RDS) proxy: [connection-pooling-and-iam-auth]
- documentdb: [documentdb-vs-dynamodb-decision]
- neptune: [graph-database-use-cases]
- keyspaces: [cassandra-migration-scenarios]
- quantum-ledger-database (QLDB): [immutable-ledger-use-cases]
- timestream: [time-series-data-scenarios]

### cross-domain-topics
- from: integration-messaging
  topics: [sqs-write-buffer-for-dynamodb, sns-lambda-rds-event-processing, kinesis-to-dynamodb-ingestion]
  cheat-sheet-ref: "§2.1 Services for Loose Coupling, §Quick Ref: Messaging"
- from: compute
  topics: [elasticache-ec2-session-caching, aurora-lambda-event-triggers, rds-proxy-lambda-connection-pooling]
  cheat-sheet-ref: "§3.3 Caching Strategies, §3.3 Database Engine Selection"
- from: serverless
  topics: [dynamodb-lambda-streams-processing, aurora-serverless-v2-scaling]
  cheat-sheet-ref: "§2.1 Serverless Technologies, §Quick Ref: Database"

## networking
- virtual-private-cloud (VPC): [multi-vpc-design, cidr-planning]
- subnets: [public-vs-private-subnet-architecture]
- network-access-control-list (NACL) vs security-group (SG): [stateless-vs-stateful-filtering]
- network-address-translation (NAT) gateway: [nat-gateway-vs-nat-instance, ha-nat-design]
- virtual-private-cloud (VPC) peering: [peering-vs-transit-gateway-decision]
- virtual-private-cloud (VPC) endpoints: [gateway-vs-interface-endpoints]
- direct-connect (DX): [dx-vs-vpn-decision, dx-gateway-multi-vpc]
- transit-gateway: [hub-and-spoke-network-design]
- flow-logs: [troubleshooting-with-flow-logs]

### cross-domain-topics
- from: security-identity
  topics: [vpc-endpoint-iam-policy, nacl-waf-layering, security-group-cross-vpc-peering]
  cheat-sheet-ref: "§1.2 VPC Architecture with Security Components, §1.2 Network Segmentation"
- from: load-balancing-scaling
  topics: [alb-nlb-subnet-placement, cross-az-load-balancing-cost]
  cheat-sheet-ref: "§4.4 NAT Gateway Cost, §Quick Ref: Load Balancer"
- from: dns
  topics: [route53-private-hosted-zones, hybrid-dns-resolver-endpoints]
  cheat-sheet-ref: "§3.4 Network Topologies"

## security-identity
- identity-and-access-management (IAM): [cross-account-access, permission-boundaries]
- organizations: [scp-inheritance-and-ou-design]
- service-control-policy (SCP): [deny-vs-allow-strategy]
- key-management-service (KMS): [cmk-vs-aws-managed-keys, key-rotation]
- systems-manager (SSM) parameter-store: [parameter-store-vs-secrets-manager]
- web-application-firewall (WAF): [waf-rules-for-common-attacks]
- shield: [shield-standard-vs-advanced]
- guardduty: [threat-detection-and-response]
- inspector: [vulnerability-assessment-automation]
- macie: [sensitive-data-discovery]
- cognito: [user-pools-vs-identity-pools]

### cross-domain-topics
- from: monitoring-audit
  topics: [guardduty-eventbridge-lambda-remediation, cloudtrail-config-compliance, config-rules-security-automation]
  cheat-sheet-ref: "§1.1 Compliance and Governance Services, §2.2 Automation Strategies"
- from: networking
  topics: [vpc-endpoint-iam-policy-restriction, private-link-service-exposure, waf-cloudfront-api-gateway]
  cheat-sheet-ref: "§1.2 VPC Architecture with Security Components"
- from: storage
  topics: [s3-bucket-policy-encryption-enforcement, kms-cross-account-key-sharing]
  cheat-sheet-ref: "§1.3 Encrypting Data at Rest, §1.3 Data Access Policies"

## load-balancing-scaling
- application-load-balancer (ALB): [path-based-vs-host-based-routing, alb-vs-nlb-decision]
- network-load-balancer (NLB): [ultra-low-latency-tcp-scenarios]
- gateway-load-balancer (GWLB): [third-party-appliance-integration]
- auto-scaling-group (ASG): [scaling-policies-target-vs-step-vs-simple, predictive-scaling]
- sticky-sessions: [session-affinity-trade-offs]
- cross-zone-load-balancing: [cross-az-traffic-distribution]
- ssl-server-name-indication (SNI): [multi-domain-ssl-on-single-alb]
- connection-draining: [graceful-deregistration-scenarios]

### cross-domain-topics
- from: compute
  topics: [ecs-dynamic-port-mapping-alb, asg-spot-fleet-mixed-instances, ec2-placement-group-cluster-nlb]
  cheat-sheet-ref: "§3.2 Auto Scaling Metrics, §4.2 Scaling Methods"
- from: networking
  topics: [cross-az-data-transfer-cost, alb-subnet-requirements]
  cheat-sheet-ref: "§4.4 NAT Gateway Cost, §Quick Ref: Load Balancer"
- from: dns
  topics: [route53-weighted-blue-green-deployment, route53-failover-with-health-checks]
  cheat-sheet-ref: "§2.2 Services for High Availability, §Quick Ref: DR Strategy"

## dns
- route-53-records: [alias-vs-cname-selection]
- routing-policies: [weighted-vs-latency-vs-failover-vs-geolocation]
- health-checks: [active-passive-failover-design]
- alias-vs-cname: [zone-apex-routing]
- hybrid-dns: [on-premises-dns-resolution]

### cross-domain-topics
- from: serverless
  topics: [route53-latency-routing-multi-region-serverless, cloudfront-api-gateway-custom-domain]
  cheat-sheet-ref: "§3.4 Network Topologies for Global Architectures"
- from: dr-architecture
  topics: [route53-failover-dr-strategies, multi-region-active-active-routing]
  cheat-sheet-ref: "§2.2 Strategies for HA and Fault Tolerance, §Quick Ref: DR Strategy"
- from: load-balancing-scaling
  topics: [route53-weighted-blue-green-deployment, route53-alb-multi-region]
  cheat-sheet-ref: "§2.2 Services for High Availability"

## integration-messaging
- simple-queue-service (SQS): [standard-vs-fifo-queue, dead-letter-queue-design]
- simple-notification-service (SNS): [sns-fanout-pattern, message-filtering]
- kinesis-data-streams: [shard-capacity-planning, kinesis-vs-sqs-decision]
- kinesis-data-firehose: [real-time-etl-to-s3-redshift]
- fan-out-pattern: [sns-sqs-fanout-architecture]
- amazon-mq: [mq-migration-from-on-premises]

### cross-domain-topics
- from: serverless
  topics: [sqs-lambda-async-processing, sns-lambda-fan-out, eventbridge-lambda-event-routing]
  cheat-sheet-ref: "§2.1 Services for Loose Coupling, §2.1 Serverless Technologies"
- from: databases
  topics: [sqs-write-buffer-dynamodb-throttling, kinesis-dynamodb-real-time-ingestion]
  cheat-sheet-ref: "§2.1 Architecture Patterns, §Quick Ref: Messaging"
- from: compute
  topics: [sqs-asg-scaling-based-on-queue-depth, kinesis-ecs-consumer-scaling]
  cheat-sheet-ref: "§3.2 Auto Scaling Metrics, §2.1 Scaling Strategies"

## serverless
- lambda: [cold-start-optimization, concurrency-limits, lambda-in-vpc]
- api-gateway: [rest-vs-http-vs-websocket-api]
- step-functions: [orchestration-vs-choreography]
- cognito: [serverless-auth-flow]
- lambda-at-edge: [edge-compute-vs-cloudfront-functions]
- cloudfront-functions: [lightweight-edge-processing]

### cross-domain-topics
- from: integration-messaging
  topics: [sqs-write-buffer-pattern, sqs-lambda-async-decoupling, sns-fan-out-to-lambda]
  cheat-sheet-ref: "§2.1 Services for Loose Coupling, §Quick Ref: Messaging"
- from: dns
  topics: [route53-latency-routing-multi-region-serverless, multi-region-api-gateway-lambda-deployment]
  cheat-sheet-ref: "§3.4 Network Topologies for Global Architectures"
- from: security-identity
  topics: [kms-lambda-environment-encryption, cognito-api-gateway-authorizer, iam-lambda-execution-role]
  cheat-sheet-ref: "§1.2 Key Security Services, §1.3 Encrypting Data at Rest"
- from: monitoring-audit
  topics: [cloudwatch-lambda-custom-metrics, xray-step-functions-tracing, cloudtrail-api-gateway-logging]
  cheat-sheet-ref: "§2.2 Automation Strategies"

## monitoring-audit
- cloudwatch: [custom-metrics-and-alarms, composite-alarms]
- cloudtrail: [management-vs-data-events, multi-account-trail]
- aws-config: [compliance-rules-and-remediation]
- eventbridge: [event-driven-automation]
- cloudwatch-insights: [log-analysis-and-anomaly-detection]

### cross-domain-topics
- from: security-identity
  topics: [guardduty-findings-eventbridge-lambda, cloudtrail-config-compliance-automation]
  cheat-sheet-ref: "§1.1 Compliance and Governance Services"
- from: serverless
  topics: [cloudwatch-lambda-metrics-alarms, eventbridge-lambda-scheduled-automation]
  cheat-sheet-ref: "§2.2 Automation Strategies, §2.1 Serverless Technologies"
- from: integration-messaging
  topics: [sns-cloudwatch-alarm-notifications, eventbridge-sqs-event-routing]
  cheat-sheet-ref: "§2.1 Services for Loose Coupling"

## data-analytics
- athena: [serverless-s3-query-scenarios]
- redshift: [redshift-vs-athena-decision, redshift-spectrum]
- glue: [etl-pipeline-design, glue-crawler-catalog]
- elastic-mapreduce (EMR): [emr-vs-glue-decision]
- quicksight: [bi-dashboard-scenarios]
- lake-formation: [data-lake-access-control]
- managed-streaming-for-kafka (MSK): [msk-vs-kinesis-decision]
- machine-learning-services: [rekognition-comprehend-sagemaker-selection]

### cross-domain-topics
- from: storage
  topics: [athena-s3-partitioning, glue-s3-data-catalog, s3-data-lake-formation-access]
  cheat-sheet-ref: "§3.5 Building Data Lakes, §Quick Ref: Storage"
- from: serverless
  topics: [lambda-glue-etl-trigger, kinesis-firehose-lambda-transformation]
  cheat-sheet-ref: "§3.5 Data Streaming Architectures, §2.1 Serverless Technologies"
- from: databases
  topics: [redshift-rds-federation, dynamodb-streams-analytics-pipeline]
  cheat-sheet-ref: "§3.5 Data Ingestion Configurations, §Quick Ref: Database"
- from: integration-messaging
  topics: [kinesis-streams-analytics-pipeline, msk-kafka-analytics-ingestion, kinesis-firehose-s3-delivery]
  cheat-sheet-ref: "§3.5 Data Streaming Architectures, §Quick Ref: Messaging"

## dr-architecture
- disaster-recovery (DR) strategies: [backup-restore-vs-pilot-light-vs-warm-standby-vs-active-active]
- database-migration-service (DMS): [heterogeneous-migration-with-sct]
- aws-backup: [cross-region-backup-strategy]
- elastic-beanstalk: [beanstalk-vs-ecs-vs-lambda-decision]
- cloudformation: [iac-stack-design-and-drift-detection]
- high-performance-computing (HPC): [hpc-cluster-architecture]
- well-architected-framework: [pillar-trade-off-scenarios]

### cross-domain-topics
- from: dns
  topics: [route53-failover-routing-dr, multi-region-active-active-route53]
  cheat-sheet-ref: "§2.2 Strategies for HA and Fault Tolerance, §Quick Ref: DR Strategy"
- from: databases
  topics: [aurora-global-database-dr, dynamodb-global-tables-multi-region, rds-cross-region-read-replicas]
  cheat-sheet-ref: "§2.2 Eliminating SPOFs, §Quick Ref: Database"
- from: storage
  topics: [s3-cross-region-replication-dr, ebs-snapshot-cross-region-copy]
  cheat-sheet-ref: "§1.3 Data Backups and Replication, §4.1 Backup and Archival"
