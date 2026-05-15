# Networking — Mini Exam (Phase 2: Concepts)
**Date:** 2026-05-15 | **Score:** 9/10 (90%) | **Scope:** concepts

## Results

| # | Result | Your Answer | Correct | Topic |
|---|--------|-------------|---------|-------|
| 1 | ✓ | B | B | subnets |
| 2 | ✓ | B | B | nacl-vs-sg |
| 3 | ✓ | C | C | vpc-endpoints |
| 4 | ✓ | C | C | nat-gateway |
| 5 | ✓ | B,C | B,C | vpc-peering |
| 6 | ✓ | B | B | direct-connect |
| 7 | ✓ | C | C | transit-gateway |
| 8 | ✓ | C | C | egress-only-igw |
| 9 | ✓ | A,C | A,C | flow-logs |
| 10 | ✗ | A | B | nat-instance |

## Missed Topics
- **nat-instance**: NAT Instance requires disabling Source/Destination Check (unique to NAT Instance, not needed for NAT Gateway). Both NAT Instance and NAT Gateway need Elastic IP.

## Key Takeaway
Remember: NAT Instance is an EC2 instance forwarding traffic — EC2 default behavior drops traffic not addressed to itself, so Source/Destination Check must be disabled.
