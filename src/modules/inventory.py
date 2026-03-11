# inventory.py — Inventory Rollforward Engine

import xarray as xr

def build_inventory_module(demand, supply, opening_inventory):
    scenarios = demand.coords["scenario"]
    time = demand.coords["time"]
    products = demand.coords["product"]

    inv = xr.zeros_like(demand)

    for s in scenarios.values:
        prev = opening_inventory
        for i, t in enumerate(time.values):
            inv.loc[dict(scenario=s, time=t)] = prev + supply.loc[dict(scenario=s)] - demand.loc[dict(scenario=s, time=t, product=products)].sum()
            prev = inv.loc[dict(scenario=s, time=t)].values

    return xr.Dataset({"Inventory": inv})
