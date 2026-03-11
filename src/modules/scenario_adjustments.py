# scenario_adjustments.py — Scenario Adjustments for S&OP

import xarray as xr

def apply_scenario_multiplier(base_array, scenarios, multipliers):
    """
    base_array: xr.DataArray(time x product)
    scenarios: list
    multipliers: list of multipliers (one per scenario)
    """
    mul = xr.DataArray(
        multipliers,
        dims=["scenario"],
        coords={"scenario": scenarios}
    )
    return base_array.expand_dims(scenario=scenarios) * mul
