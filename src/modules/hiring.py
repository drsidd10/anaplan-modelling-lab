# hiring.py — Hiring Plan Input Module

import xarray as xr
import numpy as np

def build_hiring_module(time, fte_list, hiring_data):
    """
    hiring_data: nested dict of {fte: [values per time]}
    """
    arr = []
    for f in fte_list:
        arr.append(hiring_data[f])
    
    arr = np.array(arr)  # fte x time

    hires = xr.DataArray(
        arr,
        dims=["fte", "time"],
        coords={"fte": fte_list, "time": time}
    )

    return xr.Dataset({"Hiring": hires})
