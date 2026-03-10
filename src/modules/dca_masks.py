# dca_masks.py — Dynamic Cell Access (DCA) masks

import xarray as xr

def build_dca_masks(time, editable_start_period):
    """
    time: PeriodIndex
    editable_start_period: first editable period (e.g. '2026Q3')
    """
    mask = [1 if t >= editable_start_period else 0 for t in time]

    return xr.DataArray(mask, dims=["time"], coords={"time": time})
