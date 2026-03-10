# capex.py — Capex Module for FP&A

import xarray as xr
import numpy as np

def build_capex_module(yearly_capex, time, scenarios):
    """
    yearly_capex: dict {year: value}
    time: PeriodIndex
    scenarios: list
    """

    # Build quarterly capex (spread evenly)
    capex_q = xr.DataArray(
        [yearly_capex.get(t.year, 0) / 4 for t in time],
        dims=["time"],
        coords={"time": time}
    )

    # Expand into scenarios
    capex_s = capex_q.expand_dims(scenario=scenarios)

    return xr.Dataset({"Capex": capex_s})
