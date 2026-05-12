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

## load-balancing-scaling
- application-load-balancer (ALB): [path-based-vs-host-based-routing, alb-vs-nlb-decision]
- network-load-balancer (NLB): [ultra-low-latency-tcp-scenarios]
- gateway-load-balancer (GWLB): [third-party-appliance-integration]
- auto-scaling-group (ASG): [scaling-policies-target-vs-step-vs-simple, predictive-scaling]
- sticky-sessions: [session-affinity-trade-offs]
- cross-zone-load-balancing: [cross-az-traffic-distribution]
- ssl-server-name-indication (SNI): [multi-domain-ssl-on-single-alb]
- connection-draining: [graceful-deregistration-scenarios]

## dns
- route-53-records: [alias-vs-cname-selection]
- routing-policies: [weighted-vs-latency-vs-failover-vs-geolocation]
- health-checks: [active-passive-failover-design]
- alias-vs-cname: [zone-apex-routing]
- hybrid-dns: [on-premises-dns-resolution]

## integration-messaging
- simple-queue-service (SQS): [standard-vs-fifo-queue, dead-letter-queue-design]
- simple-notification-service (SNS): [sns-fanout-pattern, message-filtering]
- kinesis-data-streams: [shard-capacity-planning, kinesis-vs-sqs-decision]
- kinesis-data-firehose: [real-time-etl-to-s3-redshift]
- fan-out-pattern: [sns-sqs-fanout-architecture]
- amazon-mq: [mq-migration-from-on-premises]

## serverless
- lambda: [cold-start-optimization, concurrency-limits, lambda-in-vpc]
- api-gateway: [rest-vs-http-vs-websocket-api]
- step-functions: [orchestration-vs-choreography]
- cognito: [serverless-auth-flow]
- lambda-at-edge: [edge-compute-vs-cloudfront-functions]
- cloudfront-functions: [lightweight-edge-processing]

## monitoring-audit
- cloudwatch: [custom-metrics-and-alarms, composite-alarms]
- cloudtrail: [management-vs-data-events, multi-account-trail]
- aws-config: [compliance-rules-and-remediation]
- eventbridge: [event-driven-automation]
- cloudwatch-insights: [log-analysis-and-anomaly-detection]

## data-analytics
- athena: [serverless-s3-query-scenarios]
- redshift: [redshift-vs-athena-decision, redshift-spectrum]
- glue: [etl-pipeline-design, glue-crawler-catalog]
- elastic-mapreduce (EMR): [emr-vs-glue-decision]
- quicksight: [bi-dashboard-scenarios]
- lake-formation: [data-lake-access-control]
- managed-streaming-for-kafka (MSK): [msk-vs-kinesis-decision]
- machine-learning-services: [rekognition-comprehend-sagemaker-selection]

## dr-architecture
- disaster-recovery (DR) strategies: [backup-restore-vs-pilot-light-vs-warm-standby-vs-active-active]
- database-migration-service (DMS): [heterogeneous-migration-with-sct]
- aws-backup: [cross-region-backup-strategy]
- elastic-beanstalk: [beanstalk-vs-ecs-vs-lambda-decision]
- cloudformation: [iac-stack-design-and-drift-detection]
- high-performance-computing (HPC): [hpc-cluster-architecture]
- well-architected-framework: [pillar-trade-off-scenarios]
