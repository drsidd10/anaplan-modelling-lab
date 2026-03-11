# supply.py — Supply Planning Module

import xarray as xr

def build_supply_module(capacity, production_ratio, scenarios, time, products):
    """
    capacity: dict {scenario: capacity per period}
    production_ratio: ratio of production to demand (e.g., 1.0 = match demand)
    """
    cap_arr = xr.DataArray(
        [capacity[s] for s in scenarios],
        dims=["scenario"],
        coords={"scenario": scenarios}
    )

    supply = xr.DataArray(
        production_ratio,
        dims=["scenario"],
        coords={"scenario": scenarios}
    )

    # supply(t) = min(capacity, ratio)
    return cap_arr * supply
