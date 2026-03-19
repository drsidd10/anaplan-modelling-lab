import xarray as xr
from src.modules.opex import build_opex_module
def test_opex(): base=xr.DataArray([[100]],dims=["time","cost_category"]); infl={"Base":1}; ds=build_opex_module(base,infl,["Base"]); assert float(ds["Inflated_Opex"])==100