# cogs.py — COGS Module (Anaplan-style)
import xarray as xr

def build_cogs_module(revenue, cogs_pct):
    """
    revenue: xr.DataArray with scenario dimension
    cogs_pct: float or DataArray
    """

    cogs = revenue * cogs_pct

    return xr.Dataset(
        {
            "Revenue": revenue,
            "COGS": cogs,
            "GrossMargin": revenue - cogs
        }
    )
