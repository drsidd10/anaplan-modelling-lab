# demand.py — Demand Planning Module

import xarray as xr

def build_demand_module(base_demand, seasonality, adjusted_demand):
    """
    base_demand: base demand xr.DataArray(time x product)
    seasonality: xr.DataArray(time)
    adjusted_demand: scenario-adjusted demand (scenarios x time x product)
    """
    seasonal = adjusted_demand * seasonality
    return xr.Dataset({
        "BaseDemand": base_demand,
        "AdjustedDemand": adjusted_demand,
        "SeasonalDemand": seasonal
    })
