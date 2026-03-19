import xarray as xr
from src.modules.scenario import ScenarioManager
def test_scenario(): sm=ScenarioManager(["Base","Up"],[1,1.1],[1,1.05]); s=xr.DataArray([100],dims=["time"]); assert float(sm.apply_price(s).sel(scenario="Up"))==110