import xarray as xr
from src.modules.revenue import build_revenue_module
def test_rev(): ds=build_revenue_module(xr.DataArray([10],dims=["time"]),xr.DataArray([5],dims=["time"])); assert float(ds["Revenue"])==50