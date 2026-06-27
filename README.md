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

## 4. Nine-Axis Framework
1. Lead time
2. Conditional forecast error and bias correction
3. Wind direction
4. Time and seasonality
5. Air density
6. Cutoff and leakage control
7. Official metric alignment
8. Group and turbine specifications
9. SCADA operation context

## 5. Pipeline
Data load -> cutoff filter -> feature engineering -> validation -> model -> postprocess -> submission

## 6. Models
Linear / Ridge / LightGBM / XGBoost / CatBoost / specialist models / ensemble

## 7. Validation
Use time-based validation with group, lead-time, wind-bin, and direction-bin error analysis.

## 8. Result
To be updated after experiments.
