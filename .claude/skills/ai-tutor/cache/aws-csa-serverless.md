# Serverless - AWS CSA Content Cache

## Definition & Core Concept
- **Serverless paradigm**: Developers don't manage servers; they deploy code/functions
- **Initially**: FaaS (Function as a Service) with AWS Lambda
- **Modern definition**: Includes managed services - databases, messaging, storage, etc.
- **Key fact**: Serverless does NOT mean no servers; means you don't manage/provision/see them
- **Pioneered by**: AWS Lambda

## Services & Concepts

### AWS Lambda
- **Type**: Virtual functions, no servers to manage
- **Execution**: Limited by time (short executions only) and memory
- **Scaling**: Automated scaling
- **Invocation**: On-demand, triggered by events
- **Max execution time**: 900 seconds (15 minutes)
- **Max memory**: 128 MB to 10 GB (1 MB increments)
- **Max /tmp storage**: 512 MB to 10 GB
- **Concurrent executions limit**: 1,000 per region (can be increased)
- **Free tier**: 1,000,000 requests + 400,000 GB-seconds compute time per month
- **Pricing**: Pay per request ($0.20 per 1M requests) + compute time ($1.00 per 600,000 GB-seconds)
- **RAM scaling benefit**: Increasing RAM also improves CPU and network quality
- **Cold starts**: New instance load + init code (fixed overhead for large dependencies); dramatically reduced in VPC (Oct-Nov 2019)
- **Provisioned concurrency**: Pre-allocates concurrency to eliminate cold starts
- **SnapStart** (Java, Python, .NET): Pre-initializes function from snapshot (10x performance improvement, no extra cost)

### Lambda Language Support
- **Built-in**: Node.js (JavaScript), Python, Java, C# (.NET Core/Powershell), Ruby
- **Custom Runtime API**: Rust, Go, or community-supported languages
- **Lambda Container Image**: Container must implement Lambda Runtime API
- **For arbitrary Docker**: Use ECS/Fargate (not Lambda)

### Lambda Invocation Types
- **Synchronous**: Caller waits for response; ThrottleError returns 429 on limit
- **Asynchronous**: Retries automatically on throttle/500-series errors; goes to DLQ after 6 hours; retry interval: 1 sec → 5 min exponential backoff

### Amazon DynamoDB
- **Type**: NoSQL database, fully managed, highly available
- **Replication**: Across multiple AZs
- **Transaction support**: Yes
- **Scale**: Millions of requests/second, trillions of rows, 100s TB storage
- **Latency**: Single-digit milliseconds (fast & consistent)
- **Item size limit**: 400 KB max
- **Data types**: Scalar (String, Number, Binary, Boolean, Null), Document (List, Map), Set (String Set, Number Set, Binary Set)
- **Schema evolution**: Can add attributes over time; schema is flexible

### DynamoDB Table Structure
- **Tables** contain infinite items (rows)
- **Primary Key** (decided at creation, cannot change):
  - **Simple**: Partition Key only (must be unique)
  - **Composite**: Partition Key + Sort Key
- **Attributes**: Key-value pairs (can be null, can be added anytime)

### DynamoDB Capacity Modes
- **Provisioned Mode** (default):
  - Specify read/writes per second
  - Requires capacity planning
  - Pay for provisioned RCU (Read Capacity Units) & WCU (Write Capacity Units)
  - Can add auto-scaling
  - Good for predictable workloads
  
- **On-Demand Mode**:
  - Scales automatically up/down with workload
  - No capacity planning
  - Pay per request (more expensive)
  - Good for unpredictable workloads, sudden spikes
  - No free tier

### DynamoDB Accelerator (DAX)
- **Purpose**: In-memory cache for DynamoDB
- **Solves**: Read congestion
- **Latency**: Microseconds (vs milliseconds from DynamoDB)
- **API compatible**: No application logic changes needed
- **Default TTL**: 5 minutes for cache
- **Use**: Cache individual objects and query/scan results
- **vs ElastiCache**: DAX caches DynamoDB responses; ElastiCache stores aggregation results

### DynamoDB Streams
- **Purpose**: Ordered stream of item-level modifications (create/update/delete)
- **Retention**: 24 hours
- **Consumers**: Limited number
- **Processing**: AWS Lambda Triggers or DynamoDB Stream Kinesis adapter
- **vs Kinesis Data Streams**: Newer option; 1-year retention, high # of consumers, multiple processing options (Lambda, Analytics, Firehose, Glue)
- **Use cases**: React to changes (welcome emails), usage analytics, insert into derivative tables, cross-region replication

### DynamoDB Global Tables
- **Purpose**: Make table accessible with low latency in multiple regions
- **Replication**: Active-Active (two-way)
- **READ and WRITE**: Possible in any region
- **Prerequisite**: Must enable DynamoDB Streams
- **Benefits**: Multi-region availability, disaster recovery

### DynamoDB TTL (Time To Live)
- **Feature**: Automatically delete items after expiry timestamp
- **Use cases**: Keep only current items, regulatory compliance, web session handling
- **Execution**: Background expiration process (scan & expire), then deletion (scan & delete)

### DynamoDB Backups
- **Continuous PITR** (Point-in-Time Recovery):
  - Enabled for last 35 days only
  - Restore to any point within window
  - Creates new table on restore
  - No performance/latency impact
  
- **On-Demand Backups**:
  - Full backups for long-term retention
  - Deleted only when explicitly removed
  - No performance impact
  - Managed via AWS Backup (enables cross-region copy)
  - Creates new table on restore

### DynamoDB + S3 Integration
- **Export to S3** (requires PITR enabled):
  - Works for any 35-day point
  - No read capacity consumption
  - Formats: DynamoDB JSON or ION
  - Use cases: Data analysis, auditing, ETL on S3 before reimporting
  
- **Import from S3**:
  - Formats: CSV, DynamoDB JSON, ION
  - No write capacity consumed
  - Creates new table
  - Import errors logged in CloudWatch

### AWS API Gateway
- **Purpose**: Expose Lambda/HTTP/AWS services as REST API with HTTPS
- **WebSocket support**: Yes
- **Versioning**: Support (v1, v2, etc.)
- **Environments**: dev, test, prod, etc.
- **Security**: Authentication, Authorization, API keys, throttling
- **Import**: Swagger/OpenAPI to quickly define APIs
- **Transform**: Validate & transform requests/responses
- **SDK generation**: Auto-generate client SDKs
- **Caching**: Cache API responses

### API Gateway Integrations
- **Lambda Function**: Invoke Lambda, expose REST API backed by Lambda
- **HTTP**: Expose HTTP endpoints (on-premise, ALB, etc.); add rate limiting, caching, auth, keys
- **AWS Service**: Expose any AWS API (start Step Function, post to SQS); add auth, deploy publicly, rate control

### API Gateway Endpoint Types
- **Edge-Optimized** (default):
  - For global clients
  - Routed through CloudFront Edge locations (improves latency)
  - API lives in one region only
  
- **Regional**:
  - For clients in same region
  - Can manually combine with CloudFront (more control)
  
- **Private**:
  - Only accessible from VPC using interface VPC endpoint (ENI)
  - Resource policy defines access

### API Gateway Security
- **User Authentication**:
  - IAM Roles (internal applications)
  - Cognito (external/mobile users)
  - Custom Authorizer (custom logic)
  
- **Custom Domain HTTPS**:
  - Integrate with AWS Certificate Manager (ACM)
  - Edge-Optimized: Certificate must be in us-east-1
  - Regional: Certificate must be in API Gateway region
  - Setup CNAME or A-alias record in Route 53

### AWS Step Functions
- **Purpose**: Serverless visual workflow to orchestrate Lambda functions
- **Features**: Sequence, parallel, conditions, timeouts, error handling
- **Integration**: EC2, ECS, on-premises, API Gateway, SQS, etc.
- **Human approval**: Supported
- **Use cases**: Order fulfillment, data processing, web applications, any workflow

### Amazon Cognito - Overview
- **Purpose**: Give users identity to interact with web/mobile apps
- **Manages**: Serverless user database

### Cognito User Pools (CUP)
- **Purpose**: Sign-in functionality for app users
- **Features**:
  - Username/password or email login
  - Password reset
  - Email & phone verification
  - Multi-factor authentication (MFA)
  - Federated identities (Facebook, Google, SAML)
- **Integration**: API Gateway & Application Load Balancer
- **Flow**: Client authenticates with CUP → receives token → passes token to API Gateway/ALB for verification

### Cognito Identity Pools (Federated Identity)
- **Purpose**: Get temporary AWS credentials for users to access AWS resources directly
- **Identity sources**: Cognito User Pools, 3rd party logins (Google, Facebook, SAML, OpenID)
- **Access**: Users obtain temp AWS credentials → access AWS services directly
- **IAM policies**: Defined in Cognito, customizable by user_id (fine-grained control)
- **Default roles**: Authenticated and guest user roles
- **Row-level security**: Policy conditions can check cognito-identity.amazonaws.com:sub

### CloudFront Functions vs Lambda@Edge

| Feature | CloudFront Functions | Lambda@Edge |
|---------|-------------------|-----------|
| Runtime | JavaScript | Node.js, Python |
| Requests/sec | Millions | Thousands |
| Triggers | Viewer Request/Response | Viewer Request/Response, Origin Request/Response |
| Execution time | < 1 ms | 5-10 seconds |
| Memory | 2 MB | 128 MB - 10 GB |
| Package size | 10 KB | 1 MB - 50 MB |
| Network/File access | No | Yes |
| Request body access | No | Yes |
| Pricing | Free tier + 1/6th price of @Edge | No free tier, per request & duration |

### CloudFront Functions Use Cases
- Cache key normalization (transform headers, cookies, query strings, URL)
- Header manipulation (insert/modify/delete)
- URL rewrites or redirects
- Request authentication & authorization (JWT validation)

### Lambda@Edge Use Cases
- Longer execution time (several ms)
- Adjustable CPU/memory
- Depends on 3rd party libraries (AWS SDK, etc.)
- Network access to external services
- File system or HTTP request body access

## Key Configurations

### Lambda Limits (per region)
**Execution:**
- Memory allocation: 128 MB - 10 GB (1 MB increments)
- Max execution time: 900 seconds (15 minutes)
- Environment variables: 4 KB
- /tmp disk: 512 MB - 10 GB
- Concurrent executions: 1,000 (can be increased via support ticket)
- Reserved concurrency: Can set per function to limit max concurrent invocations

**Deployment:**
- Compressed .zip size: 50 MB max
- Uncompressed (code + dependencies): 250 MB max
- Can use /tmp to load additional files at startup
- Environment variables: 4 KB total

### Lambda Concurrency & Throttling
- **Default limit**: 1,000 concurrent executions across all functions
- **Reserved concurrency**: Set per function to limit; throttles if exceeded
- **Throttle behavior**:
  - Synchronous: Returns ThrottleError (429)
  - Asynchronous: Retries auto; eventually goes to DLQ
- **Retry on async throttle/500**: Exponential backoff 1 sec → 5 min max, retry for up to 6 hours

### DynamoDB Concurrency Issue
- Without reserved concurrency, ASG can consume all 1,000 concurrent executions
- Other clients (API Gateway, SDK/CLI) get throttled if ASG takes limit
- Solution: Reserve concurrency for important functions

### Lambda VPC Considerations
- **Default**: Lambda runs in AWS-owned VPC (cannot access VPC resources)
- **To access private RDS/ElastiCache/internal ELB**: Deploy in customer VPC
- **Trade-off**: ENI creation adds cold start latency (greatly improved in 2019)
- **Cold starts in VPC**: Dramatically reduced (Oct-Nov 2019)

### RDS Proxy
- **Purpose**: Connection pooling for Lambda → RDS
- **Benefits**:
  - Improves scalability (pools/shares connections)
  - Improves availability (66% failover time reduction, preserves connections)
  - Improves security (IAM auth, Secrets Manager credentials)
- **Constraint**: Must deploy Lambda in VPC (RDS Proxy never publicly accessible)

### Invoking Lambda from RDS & Aurora
- **Support**: RDS PostgreSQL, Aurora MySQL
- **Requirement**: Outbound traffic allowed (Public, NAT GW, VPC Endpoints)
- **Permissions**: Lambda resource-based policy + IAM policy on DB instance
- **Use case**: Data event processing (e.g., trigger email on user INSERT)

### RDS Event Notifications
- **Contents**: DB instance events (created, stopped, started, etc.) - NOT data changes
- **Event categories**: DB instance, snapshot, parameter group, security group, RDS Proxy, custom engine
- **Latency**: Near real-time (up to 5 minutes)
- **Targets**: SNS or EventBridge

## Architectural Patterns

### Basic Serverless REST API
**Components**: Client → API Gateway → Lambda → DynamoDB
- Client makes REST HTTPS call to API Gateway
- API Gateway authenticates via Cognito
- API Gateway invokes Lambda function
- Lambda queries/reads from DynamoDB

### High Read Throughput Pattern
**Add caching layers**:
- DAX between Lambda and DynamoDB (microsecond latency)
- API Gateway response caching (eliminates backend calls)
- CloudFront for static content distribution

### Direct S3 Access from Client
**Pattern**: Cognito Identity Pools → temporary credentials → direct S3 access
- User authenticates with Cognito User Pool
- Cognito Identity Pool provides temp AWS credentials
- Client uploads/downloads files directly to S3 with restricted folder permissions
- Uses IAM policy to enforce user_id-based row-level security

### Serverless Thumbnail Generation
**Flow**: S3 upload → Lambda trigger → create thumbnail → S3 output + optional SQS/SNS
- Upload photo to S3 (can use Transfer Acceleration)
- S3 triggers Lambda function
- Lambda generates thumbnail
- Lambda uploads thumbnail back to S3
- Optional: Notify via SQS queue or SNS topic

### Serverless CRON Job
**Components**: CloudWatch Events/EventBridge → Lambda
- Scheduled rule triggers Lambda every N hours/days
- Lambda performs background task (cleanup, reports, etc.)

### Welcome Email Flow
**Components**: DynamoDB → DynamoDB Streams → Lambda → SES
- User inserted into DynamoDB table
- Stream captures INSERT event
- Lambda function triggered by stream
- Lambda uses SES (Simple Email Service) to send welcome email

### Global Blog/Website
**Components**: CloudFront (static) + API Gateway + Lambda + DynamoDB Global Tables
- Static content: S3 + CloudFront distribution with OAC (Origin Access Control)
- Dynamic API: API Gateway + Lambda
- Database: DynamoDB Global Tables (multi-region active-active)
- DAX for read caching
- API Gateway caching for frequently requested data

### Microservices Architecture
**Pattern**: Route 53 → (service1.domain, service2.domain, service3.domain)
- Each service has own API/backend stack
- Service1: API Gateway + Lambda + ElastiCache + DynamoDB
- Service2: ALB + ECS + RDS
- Service3: ALB + Auto Scaling + EC2
- Each can have different architecture
- Services communicate via REST APIs

### Software Update Offloading
**Pattern**: Add CloudFront in front of static files
- Existing: ALB + Auto Scaling Group (EC2)
- Add: CloudFront distribution
- CloudFront caches update files at edge locations
- EC2 instances handle less load during update spike
- No application changes needed
- Reduces EC2 scaling, bandwidth, costs

## Important Numbers & Limits

| Metric | Value | Notes |
|--------|-------|-------|
| Lambda free requests/month | 1,000,000 | |
| Lambda free compute/month | 400,000 GB-seconds | |
| Lambda request price | $0.0000002 per request | $0.20 per 1M |
| Lambda compute price | $1.00 per 600,000 GB-seconds | After free tier |
| Lambda max execution time | 900 seconds | 15 minutes |
| Lambda memory range | 128 MB - 10 GB | 1 MB increments |
| Lambda concurrent limit | 1,000 | Per region, can increase |
| Lambda /tmp storage | 512 MB - 10 GB | Depends on memory |
| Lambda deployment .zip | 50 MB | Compressed |
| Lambda uncompressed code | 250 MB | Code + dependencies |
| Lambda env var size | 4 KB | Total limit |
| DynamoDB item max size | 400 KB | Single item |
| DynamoDB streams retention | 24 hours | Limited consumers |
| Kinesis streams retention | 1 year | More consumers |
| DynamoDB PITR window | 35 days | Continuous backups |
| CloudFront Functions package | 10 KB | JavaScript only |
| CloudFront Functions memory | 2 MB | |
| CloudFront Functions latency | < 1 ms | Sub-millisecond |
| Lambda@Edge package | 1 MB - 50 MB | |
| Lambda@Edge memory | 128 MB - 10 GB | |
| Lambda@Edge latency | 5-10 seconds | Longer execution |

## Diagram Descriptions

### Serverless Thumbnail Creation
S3 bucket (upload image) → triggers Lambda → Lambda creates thumbnail → outputs to S3 + metadata to DynamoDB

### Serverless CRON Job
CloudWatch Events/EventBridge (every 1 hour) → triggers Lambda → Lambda performs task

### Mobile App Architecture
Mobile client (REST HTTPS) → API Gateway (authenticates via Cognito) → Lambda (invokes) → DynamoDB (queries)
- Direct S3 access: Client gets credentials from Cognito Identity Pool, uploads files directly to S3

### Global Blog Website
- Static: Client → CloudFront (edge optimization) → S3 (with OAC bucket policy)
- Dynamic: Client → API Gateway (REST HTTPS) → Lambda (invokes) → DAX (caches) → DynamoDB (Global Tables)
- Email flow: DynamoDB Stream → Lambda (with IAM role) → SES (sends email)
- Photo upload: Client → CloudFront Transfer Acceleration → S3 → Lambda trigger → thumbnail S3 → SQS/SNS (optional)

### Microservices with DNS Routing
Route 53 (DNS) routes to three services based on hostname:
- service1.example.com → API Gateway + Lambda + ElastiCache + DynamoDB
- service2.example.com → ALB + ECS + DynamoDB
- service3.example.com → ALB + Auto Scaling + RDS

### Software Update Offloading Before & After
Before: Users → ALB → Auto Scaling Group (multiple EC2s) → high bandwidth
After: Users → CloudFront → ALB → Auto Scaling (fewer EC2s needed) → low bandwidth

## Exam-Relevant Details

### Lambda vs EC2
- Lambda: Short execution, event-driven, auto-scaling, pay per use
- EC2: Long-running, continuous, manual scaling, pay per instance

### When to Use Serverless Services
- Unpredictable traffic: On-Demand DynamoDB, Lambda
- Predictable traffic: Provisioned DynamoDB, could use Lambda
- Real-time requirements: DynamoDB streams, Lambda
- Need caching: DAX (DynamoDB), ElastiCache (general), CloudFront (static)
- Need scalability: Lambda (automatic), DynamoDB Global Tables, CloudFront

### DynamoDB vs Relational DB
- DynamoDB: NoSQL, scales horizontally, flexible schema, high throughput
- RDS: SQL, vertical scaling, fixed schema, transactional guarantees

### Authentication Selection
- **Internal apps**: IAM
- **Mobile/external users**: Cognito User Pools
- **Direct AWS access**: Cognito Identity Pools
- **Custom logic**: Custom Authorizer

### Cold Start Considerations
- **Problem**: New instance initialization adds latency
- **Solutions**:
  - Provisioned concurrency (pre-allocated)
  - SnapStart (Java/Python/.NET pre-initialization)
  - Keep dependencies small
  - Warm up functions periodically

### Common Traps
- **Lambda and VPC**: Default deployment cannot access private RDS (must deploy in VPC)
- **Concurrent limits**: ASG + Lambda can share 1,000 limit; reserve concurrency if needed
- **DynamoDB throttling**: On-Demand more expensive but auto-scales; Provisioned cheaper if predictable
- **Cognito pools**: User Pools for sign-in; Identity Pools for direct AWS access
- **API Gateway caching**: Cache key, TTL, and invalidation often forgotten
- **CloudFront**: Works best for static/cacheable content; OAC prevents direct S3 access
- **DynamoDB Streams**: Limited consumers; Kinesis better for many consumers
- **Global tables**: Requires Streams; not just copying across regions

### Keywords Signaling Service Choice
- "One-time spike in traffic" → Lambda, On-Demand DynamoDB, CloudFront
- "Multiple regions, low latency" → DynamoDB Global Tables, CloudFront
- "Send emails" → SES + Lambda
- "Schedule background job" → CloudWatch Events + Lambda
- "Stream data changes" → DynamoDB Streams → Lambda
- "Cache reads" → DAX (DynamoDB), ElastiCache (general), CloudFront (static)
- "Multiple AZs, high availability" → All serverless services have built-in HA
- "Direct user S3 access" → Cognito Identity Pools + restricted IAM policy
- "User authentication" → Cognito User Pools
