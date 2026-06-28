# Metric Policy

Model selection should follow the official competition objective rather than generic loss only.

## Primary Metrics
- nMAE
- FICR
- total score

## Required Diagnostics
Every serious experiment should report:

- local 1-nMAE
- local FICR
- local total score
- below 6% error ratio
- 6-8% error ratio
- above 8% error ratio
- group-level score
- lead-time weakness
- wind-bin weakness
- direction-bin weakness

## Decision Rule
Prefer models that improve the official metric under time-based validation. Public score should be treated as a delayed sanity check, not as the primary optimization target.
