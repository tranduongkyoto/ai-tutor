# Monitoring & Audit — Mini Exam: Comprehensive Final (Phase 4)
**Date:** 2026-06-05 16:58
**Score:** 10/10 (100%)
**Time:** 15 min / 30 min ✓ within limit
**Scope:** comprehensive — full domain exam + cross-domain

---

## Questions & Results

### Q1 ✓ — cloudwatch-anomaly-detection
**Your answer: B** — Correct. CW Anomaly Detection = ML-based per-metric baselines. No manual thresholds.

### Q2 ✓ — aws-config-vs-cloudtrail
**Your answer: C** — Correct. CloudTrail = who (API call). Config = what changed (before/after values).

### Q3 ✓ — cloudwatch-logs-kds-fanout
**Your answer: C** — Correct. Subscription → KDS → KDF(S3) + Lambda(SIEM).

### Q4 ✓ — cloudtrail-eventbridge-region-detection
**Your answer: C** — Correct. CloudTrail Invoke + EventBridge region filter → Lambda disable.

### Q5 ✓ — security:config-aggregator-cross-account
**Your answer: A** — Correct. Config Aggregator + rules + SSM per account.

### Q6 ✓ — high-resolution-alarm-cost
**Your answer: B** — Correct. 10s periods = $0.30/alarm. Increase to ≥60s = $0.10/alarm.

### Q7 ✓ — cloudwatch-lambda-insights
**Your answer: B** — Correct. Lambda Insights = Lambda Layer for cold starts + system metrics.

### Q8 ✓ — security:guardduty-eventbridge-lambda
**Your answer: B** — Correct. GuardDuty → EventBridge(High) → Lambda quarantine SG.

### Q9 ✓ — cloudwatch-agent-iam-role
**Your answer: A, B** — Correct. Agent not installed + missing IAM role = two most common causes.

### Q10 ✓ — cw-config-cloudtrail-combined
**Your answer: C** — Correct. CW(metrics) + Config(SSL compliance) + CloudTrail(who modified).

---

## Summary
- **Score:** 10/10 (100%) — PASSED
- **Missed topics:** none
- **All P3 weak topics mastered:** cloudwatch-anomaly-detection, cloudtrail-eventbridge-region-detection, aws-config-vs-cloudtrail
