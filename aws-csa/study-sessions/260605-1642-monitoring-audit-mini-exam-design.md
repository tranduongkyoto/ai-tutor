# Monitoring & Audit — Mini Exam: Design (Phase 3)
**Date:** 2026-06-05 16:42
**Score:** 7/10 (70%)
**Time:** 23 min / 30 min ✓ within limit
**Scope:** design — architecture design decisions and trade-offs

---

## Questions & Results

### Q1 ✓ — cloudtrail-multi-account-trail
**Question:** 30 accounts under Organizations, 5-year audit retention, ad-hoc SQL queries. Least operational overhead?
A) Per-account trails + Glue + Athena B) Organization Trail + central S3 + Athena C) CW Logs 10yr + Logs Insights D) OpenSearch cluster
**Your answer: B** — Correct. Organization Trail auto-applies to all members. Central S3 + Athena = serverless, least overhead.

### Q2 ✓ — cloudwatch-composite-alarms
**Question:** 200+ alerts/day from single-metric spikes. Real incidents = CPU AND memory. Reduce noise 90%.
**Your answer: A** — Correct. Composite Alarm (AND logic) routes only correlated alerts to SNS.

### Q3 ✓ — cloudtrail-log-integrity-validation
**Question:** Tamper-proof audit logs for regulators (including vs AWS admins).
**Your answer: A** — Correct. Log File Integrity Validation (SHA-256) + S3 Object Lock Compliance Mode.

### Q4 ✓ — aws-config-compliance-remediation
**Question:** Auto-remediate unencrypted EBS + open SSH SGs within 10 min, 5 retries, email notification.
**Your answer: B** — Correct. Config rules + SSM Automation (5 retries) + EventBridge → SNS.

### Q5 ✗ — cloudwatch-anomaly-detection
**Question:** Auto-detect abnormal 5xx error rate spikes per service without manual thresholds.
A) Static thresholds B) CW Anomaly Detection (ML) C) CloudTrail Insights D) Contributor Insights
**Your answer: C** — Incorrect. Correct: B. CloudTrail Insights detects unusual API call patterns, not application metrics. CW Anomaly Detection uses ML for per-metric baselines.

### Q6 ✓ — cloudwatch-logs-kds-fanout
**Question:** CW Logs → OpenSearch (real-time) + S3 (near-real-time) from single source.
**Your answer: B** — Correct. Subscription → KDS → Lambda+OpenSearch & KDF+S3.

### Q7 ✓ — eventbridge-resource-based-policy
**Question:** Only 20 accounts + 2 SaaS partners may PutEvents on central bus.
**Your answer: B** — Correct. Resource-based Policy on event bus.

### Q8 ✗ — cloudtrail-eventbridge-region-detection
**Question:** Detect Lambda invocation in unauthorized regions → auto-disable.
A) Config + SSM B) GuardDuty C) CloudTrail + EventBridge region filter D) CW Anomaly Detection
**Your answer: A** — Incorrect. Correct: C. Config evaluates resource existence, not invocations. CloudTrail logs Invoke API with region metadata → EventBridge matches.

### Q9 ✗ — aws-config-vs-cloudtrail
**Question:** Track RDS config changes with before/after values over past year.
A) CloudTrail B) Config timeline C) CloudWatch D) RDS Events
**Your answer: A** — Incorrect. Correct: B. CloudTrail = who called what API. Config = what changed + before/after values. Configuration history timeline = Config.

### Q10 ✓ — cw-config-cloudtrail-combined
**Question:** ELB monitoring: traffic metrics + SSL compliance + listener audit.
**Your answer: B** — Correct. CloudWatch(metrics) + Config(SSL rule) + CloudTrail(API audit).

---

## Summary
- **Score:** 7/10 (70%)
- **Missed topics:** cloudwatch-anomaly-detection, cloudtrail-eventbridge-region-detection, aws-config-vs-cloudtrail
- **Strong areas:** multi-account-trail, composite-alarms, log-integrity, config-remediation, kds-fanout, eventbridge-policy, combined-monitoring
- **Key lessons:**
  - CW Anomaly Detection = ML baselines for metrics. CloudTrail Insights = unusual API patterns. Don't confuse them.
  - Config = resource configuration state (before/after). CloudTrail = API call history (who/when). Config answers "what changed?" CloudTrail answers "who changed it?"
  - Detecting API calls in specific regions → CloudTrail + EventBridge. Config doesn't track invocations.
