# Nine-Axis Feature Framework

Every feature in this project must be mapped to at least one axis. If a feature cannot be explained through this framework, it should not enter the training dataset until its role is clarified.

## Axis 1. Lead Time
Purpose: capture how forecast reliability changes as the target time moves farther from the forecast base time or cutoff time.

Representative features:
- `lead_time_hours`
- `lead_time_bin`
- `target_hour_from_cutoff`
- `lead_time x wind_speed`
- `lead_time x group_id`
- `lead_time x LDAPS_GFS_diff`

## Axis 2. Conditional Bias
Purpose: learn when NWP forecasts or baseline model predictions systematically overpredict or underpredict.

Representative features:
- `nwp_bias_by_group_lead`
- `nwp_bias_by_group_direction`
- `residual_bias_by_group_lead`
- `residual_bias_by_group_wind_bin`
- `hard_case_rate_by_group_lead`

Rule: these features must be built with train-only history or OOF logic.

## Axis 3. Wind Direction
Purpose: represent directional wind effects, terrain exposure, wake-like behavior, and group-specific favorable or unfavorable directions.

Representative features:
- `wind_dir_sin`
- `wind_dir_cos`
- `direction_bin_8`
- `direction_bin_16`
- `group_direction_bin`
- `dir_diff`

## Axis 4. Time And Seasonality
Purpose: capture recurring weather and generation patterns by hour, month, season, and day of year.

Representative features:
- `target_hour`
- `target_month`
- `target_season`
- `target_dayofyear`
- `hour_sin`
- `hour_cos`
- `month_sin`
- `month_cos`

## Axis 5. Air Density And Wind Power Physics
Purpose: reflect that wind power depends on air density and roughly on wind speed cubed.

Representative features:
- `wind_speed_squared`
- `wind_speed_cubed`
- `air_density_proxy`
- `wind_power_proxy`

## Axis 6. Cutoff Control
Purpose: prevent future information from entering feature generation.

Core rule:

```text
available_time <= cutoff_time
```

Representative fields:
- `cutoff_time`
- `available_time`
- `forecast_base_time`
- `target_time`
- `leakage_check_result`

## Axis 7. Official Metric And FICR Risk
Purpose: align training, validation, and postprocessing with the official scoring logic instead of generic MSE/RMSE.

Representative features or diagnostics:
- `ficr_risk_by_group`
- `ficr_risk_by_lead`
- `ficr_risk_by_wind_bin`
- `hard_case_rate`
- `near_6pct_error_rate`
- `near_8pct_error_rate`

## Axis 8. Group And Turbine Specification
Purpose: capture different generation responses across KPX groups, capacities, and turbine behavior.

Representative features:
- `group_id`
- `group_capacity`
- `group_capacity_ratio`
- `is_group3`
- `group_wind_speed_bin`
- `group_wind_speed_cubed`
- `group_season`
- `group_lead_time_bin`

## Axis 9. SCADA Operation Context
Purpose: capture recent plant state, ramp behavior, abnormal operation, curtailment-like behavior, and real-site wind context.

Representative features:
- `scada_power_last`
- `scada_power_mean_1h`
- `scada_power_mean_3h`
- `scada_power_mean_6h`
- `scada_power_mean_24h`
- `scada_power_ramp_1h`
- `scada_power_ramp_3h`
- `scada_zero_power_ratio_24h`
- `scada_low_power_high_wind_flag`

Rule: only SCADA available at or before the cutoff may be used.
