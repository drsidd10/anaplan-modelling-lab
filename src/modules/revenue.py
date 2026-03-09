# revenue.py — Revenue Calculation Module (Price × Volume)

import xarray as xr

def build_revenue_module(prices, volumes):
    """
    Given price and volume DataArrays (possibly with scenario dimension),
    compute Revenue = Price × Volume
    """
    revenue = prices * volumes
    ds = xr.Dataset(
        {
            "Price": prices,
            "Volume": volumes,
            "Revenue": revenue
        }
    )
    return ds
