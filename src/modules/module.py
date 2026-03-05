# module.py — Anaplan-style Module Framework (xarray)

import xarray as xr
import numpy as np

class Module:
    """Represents an Anaplan-style module using xarray Dataset."""

    def __init__(self, name, dataset: xr.Dataset):
        self.name = name
        self.data = dataset

    def line(self, item):
        """Return a line item."""
        return self.data[item]

    def add_lineitem(self, name, array):
        """Add a new line item (DataArray) to the module."""
        self.data[name] = array

    def apply_formula(self, new_name, formula_fn):
        """Apply a Python function to create a new derived line item."""
        self.data[new_name] = formula_fn(self.data)

    def __repr__(self):
        return f"Module({self.name}, {len(self.data.data_vars)} line items)"
