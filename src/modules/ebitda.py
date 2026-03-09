# ebitda.py — EBITDA Module

import xarray as xr

def build_ebitda_module(gm_ds, opex_ds):
    """
    gm_ds: dataset containing GrossMargin
    opex_ds: dataset containing Inflated_Opex
    """

    gm = gm_ds["GrossMargin"]
    opex = opex_ds["Inflated_Opex"].sum(dim="cost_category")

    ebitda = gm - opex

    return xr.Dataset(
        {
            "GrossMargin": gm,
            "OPEX": opex,
            "EBITDA": ebitda
        }
    )
