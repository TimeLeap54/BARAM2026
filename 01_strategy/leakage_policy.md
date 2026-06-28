# Leakage Policy

Leakage control is the first safety rule of the project. A feature that improves validation but violates the cutoff rule must be removed.

## Core Rule
Every feature must satisfy:

```text
available_time <= cutoff_time
```

## Required Time Fields
Feature generation should track these fields whenever possible:

- `target_time`
- `cutoff_time`
- `forecast_base_time`
- `available_time`
- `feature_time`
- `source`

## NWP Forecast Features
NWP features may use only forecasts released before or at the cutoff.

Required checks:
- confirm `forecast_base_time`
- confirm the forecast was available before `cutoff_time`
- confirm the feature targets the correct `target_time`

## SCADA Features
SCADA features may use only measurements available before or at the cutoff.

Forbidden:
- target-time SCADA values
- future rolling windows
- any aggregation that includes values after `cutoff_time`

Allowed:
- last known value before cutoff
- rolling history ending at or before cutoff
- recent ramp or abnormal-state summaries ending at or before cutoff

## Train-Only And OOF Features
Bias, residual, hard-case, and FICR-risk features must not use validation or test targets.

Allowed methods:
- expanding-window historical statistics
- fold-specific train-only statistics
- OOF residual tables

Forbidden methods:
- full-data target encoding
- residual tables computed using validation targets
- public score feedback encoded into features

## Leakage Check Log
Every risky feature should be recorded in `05_experiments/leakage_check_log.md`.

Required decision rule:

```text
Pass if available_time <= cutoff_time.
Fail otherwise.
```
