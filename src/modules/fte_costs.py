# fte_costs.py — Headcount Rollforward + Costing

import xarray as xr

def compute_fte_rollforward(hiring_ds, sys_ds):
    hires = hiring_ds["Hiring"]
    fte_list = hires.coords["fte"]
    time = hires.coords["time"]

    # Create empty FTE dataset
    fte = xr.zeros_like(hires)

    # Opening headcount = 0
    opening = xr.zeros_like(hires.isel(time=0))

    for i, t in enumerate(time):
        if i == 0:
            fte.loc[dict(time=t)] = opening + hires.sel(time=t)
        else:
            prev = fte.sel(time=time[i-1])
            fte.loc[dict(time=t)] = prev + hires.sel(time=t)

    # Cost Calculation
    salary = sys_ds["Salary"]
    oncost = sys_ds["Oncost"]

    cost = fte * salary * (1 + oncost)

    return xr.Dataset(
        {
            "FTE": fte,
            "Cost": cost
        }
    )
