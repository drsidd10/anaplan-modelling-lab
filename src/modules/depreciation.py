# depreciation.py — Depreciation Engine

import xarray as xr
import numpy as np

def build_depreciation_module(capex_ds, useful_life_years, time):
    """
    capex_ds: Dataset with Capex (scenario x time)
    useful_life_years: int
    """

    capex = capex_ds["Capex"]
    quarters = useful_life_years * 4

    # Create depreciation array same shape as capex
    depreciation = xr.zeros_like(capex)

    # Loop over time index to allocate depreciation
    for i, t in enumerate(time):
        dep_amount = capex.sel(time=t) / quarters
        end = i + quarters
        dep_window = time[i+1:end+1] if end < len(time) else time[i+1:]

        if len(dep_window) > 0:
            depreciation.loc[dict(time=dep_window)] += dep_amount.values

    return xr.Dataset({"Depreciation": depreciation})
