# Feature Design

## Core Hypothesis
Raw LDAPS/GFS forecasts are not enough. The winning system should transform weather forecasts into leakage-safe features that explain:

- how reliable each forecast is under the current condition
- how each KPX group responds to wind speed, wind direction, season, and lead time
- when recent SCADA context signals normal operation, ramping, zero output, or abnormal behavior
- when the prediction is likely to fail the official settlement thresholds

## Row Definition
One training or inference row represents:

```text
one cutoff_time x one group_id x one target_time
```

Required keys:
- `group_id`
- `target_time`
- `forecast_date`
- `cutoff_time`
- `forecast_base_time`
- `lead_time`

Preferred target:

```text
normalized_power = generation_mw / group_capacity
```

## Priority P0. Mandatory Baseline Features
P0 features must be implemented first. They make the minimum viable dataset.

Feature groups:
- group identity: `group_id`
- target time: `target_hour`, `target_month`, `target_season`
- cyclical time: `hour_sin`, `hour_cos`, `month_sin`, `month_cos`
- lead time: `lead_time_hours`, `lead_time_bin`
- raw NWP: LDAPS/GFS wind speed, wind direction, temperature
- target: `normalized_power`

Purpose: establish a stable baseline that understands the problem shape.

## Priority P1. Physical And Domain Weather Features
P1 features are the first real performance battlefield.

Feature groups:
- wind speed powers: `wind_speed_squared`, `wind_speed_cubed`
- air density: `air_density_proxy`
- wind power proxy: `wind_power_proxy`
- LDAPS/GFS disagreement: `ws_diff`, `ws_abs_diff`, `dir_diff`, `temp_diff`
- wind regime: `wind_speed_bin`, `direction_bin_8`, `direction_bin_16`
- group interactions: `group_wind_speed_bin`, `group_direction_bin`
- lead-time interactions: `lead_time x wind_speed`, `lead_time x LDAPS_GFS_diff`

Purpose: stop trusting raw forecasts directly and encode physical response and forecast uncertainty.

## Priority P2. SCADA Context Features
P2 features describe the recent operating state of each group.

Feature groups:
- recent power: `scada_power_last`, rolling means over 1h, 3h, 6h, 12h, 24h
- recent wind: rolling wind speed mean/std and direction dispersion
- ramp: `scada_power_ramp_1h`, `scada_power_ramp_3h`
- abnormal state: `zero_power_ratio`, `high_wind_low_power_flag`

Rule: P2 features must use only SCADA values available before the cutoff.

## Priority P3. Conditional Bias And Residual Features
P3 features are powerful but dangerous. They must be built only from train history or OOF predictions.

Feature groups:
- NWP bias: `nwp_bias_by_group_lead`, `nwp_bias_by_group_direction`
- residual bias: `residual_bias_by_group_lead`, `residual_bias_by_group_wind_bin`
- hard-case rates: `hard_case_rate_by_group_lead`, `hard_case_rate_by_direction_bin`
- threshold risk: `near_6pct_error_rate`, `near_8pct_error_rate`

Purpose: learn where forecasts or base models usually fail under specific conditions.

## Priority P4. Advanced Optional Features
P4 features should be considered after P0-P3 are stable.

Candidates:
- `empirical_power_curve_distance`
- `rated_power_saturation_flag`
- `cut_in_risk_flag`
- `curtailment_proxy`
- `group3_smoothing_feature`
- `terrain_direction_proxy`

Purpose: add advanced domain corrections without destabilizing the core pipeline.

## Key Battlefields
1. LDAPS vs GFS disagreement.
2. Group-specific wind speed response.
3. Group-specific wind direction response.
4. Lead-time-dependent forecast reliability.
5. Cutoff-safe recent SCADA state.
6. Train-only or OOF residual bias correction.
7. FICR and hard-case risk.

## Implementation Mapping
Feature files should follow the priority and axis structure.

```text
04_src/features/
  feature_registry.py
  features_time.py
  features_leadtime.py
  features_nwp.py
  features_wind.py
  features_air_density.py
  features_group.py
  features_scada.py
  features_bias.py
  features_settlement.py
```

The registry should keep feature priority explicit so that experiments can select P0 only, P0+P1, or later P0-P3 safely.
