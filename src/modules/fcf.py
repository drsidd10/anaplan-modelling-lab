# fcf.py — NOPAT, FCF, NPV module

import xarray as xr
import numpy as np

def build_fcf_module(ebitda_ds, depreciation_ds, capex_ds, nwc_delta, tax_rate=0.19):
    """
    ebitda_ds: Dataset with EBITDA
    depreciation_ds: Dataset with Depreciation
    capex_ds: Dataset with Capex
    nwc_delta: xr.DataArray (scenario x time)
    """

    dep = depreciation_ds["Depreciation"]
    ebit = ebitda_ds["EBITDA"] - dep

    tax = xr.where(ebit > 0, ebit * tax_rate, 0)
    nopat = ebit - tax

    capex = capex_ds["Capex"]

    fcf = nopat + dep - capex - nwc_delta

    return xr.Dataset(
        {
            "EBIT": ebit,
            "Tax": tax,
            "NOPAT": nopat,
            "FCF": fcf
        }
    )


def compute_npv(fcf, discount_rate=0.10):
    """Quarterly discounting"""
    quarters = np.arange(1, len(fcf["time"]) + 1)
    disc = (1 + discount_rate)**(quarters/4)

    npv = (fcf / disc).sum(dim="time")
    return npv
