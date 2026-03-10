# fte_sys.py — Workforce Planning SYS Module

import xarray as xr
import numpy as np

def build_fte_sys(fte_list, salary_map, oncost_map):
    """
    fte_list: list of FTE types/roles
    salary_map: dict {fte: base salary}
    oncost_map: dict {fte: oncost percentage}
    """

    sys_ds = xr.Dataset(
        {
            "Salary": xr.DataArray(
                [salary_map[f] for f in fte_list],
                dims=["fte"],
                coords={"fte": fte_list}
            ),
            "Oncost": xr.DataArray(
                [oncost_map[f] for f in fte_list],
                dims=["fte"],
                coords={"fte": fte_list}
            )
        }
    )
    return sys_ds
