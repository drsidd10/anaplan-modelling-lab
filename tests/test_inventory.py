import xarray as xr
from src.modules.inventory import build_inventory_module
def test_inv(): demand=xr.DataArray([[5,5]],dims=["scenario","time"]); supply=xr.DataArray([15],dims=["scenario"]); inv=build_inventory_module(demand,supply,0); assert float(inv["Inventory"].isel(time=1))>=0