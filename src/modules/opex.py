# opex.py — OPEX Module (Anaplan-style)

import xarray as xr

def build_opex_module(base_opex, inflation_rate, scenarios):
    """
    base_opex: xr.DataArray (time x cost_category)
    inflation_rate: dict of scenario -> quarterly inflation multiplier
    scenarios: list of scenarios
    """

    # Scenario inflation across time
    inflators = xr.DataArray(
        [inflation_rate[s] for s in scenarios],
        dims=["scenario"],
        coords={"scenario": scenarios}
    )

    # Expand opex into scenarios
    base_s = base_opex.expand_dims(scenario=scenarios)

    # Apply inflation per scenario
    # inflators broadcast across time x cost_category
    opex_s = base_s * inflators

    return xr.Dataset(
        {
            "Base_Opex": base_s,
            "Inflated_Opex": opex_s
        }
    )
