# BARAM 2026 Wind Power Forecasting

## 1. Problem Definition
Use weather forecasts available at the competition cutoff time and historical SCADA data to predict next-day wind power generation for KPX groups.

## 2. Objective
Optimize the official competition score: nMAE, FICR, and total score.

## 3. Key Constraint
Every feature must satisfy:

```text
available_time <= cutoff_time
```

## 4. Strategy
The project is organized around two design rules:

1. Every feature must belong to one of the nine strategic axes.
2. Every feature must have a priority level from P0 to P4.

The core hypothesis is that raw LDAPS/GFS forecasts are not enough. The model must learn conditional NWP reliability and group-specific wind-power response without leaking future information.

## 5. Nine-Axis Framework
1. Lead time
2. Conditional forecast error and bias correction
3. Wind direction
4. Time and seasonality
5. Air density
6. Cutoff and leakage control
7. Official metric alignment
8. Group and turbine specifications
9. SCADA operation context

## 6. Feature Priority
P0: mandatory baseline features.
P1: physical and domain weather features.
P2: cutoff-safe SCADA context features.
P3: train-only or OOF residual and bias features.
P4: advanced optional features.

## 7. Pipeline
Data load -> cutoff filter -> feature engineering -> validation -> model -> postprocess -> submission

## 8. Models
Linear / Ridge / LightGBM / XGBoost / CatBoost / specialist models / ensemble

## 9. Validation
Use time-based validation with group, lead-time, wind-bin, and direction-bin error analysis.

## 10. Result
To be updated after experiments.
