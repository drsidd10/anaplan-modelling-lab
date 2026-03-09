# scenario.py — Scenario Engine for Anaplan Modelling Lab
import xarray as xr
import numpy as np

class ScenarioManager:
    """
    Anaplan-style Scenario / Version Manager.
    Applies scenario multipliers to xarray DataArrays.
    """

    def __init__(self, scenarios, price_multipliers, volume_multipliers):
        self.scenarios = scenarios
        self.price_multipliers = xr.DataArray(
            price_multipliers, dims=["scenario"], coords={"scenario": scenarios}
        )
        self.volume_multipliers = xr.DataArray(
            volume_multipliers, dims=["scenario"], coords={"scenario": scenarios}
        )

    def apply_price(self, price_array):
        """Broadcast price array across scenarios."""
        return price_array.expand_dims(scenario=self.scenarios) * self.price_multipliers

    def apply_volume(self, volume_array):
        """Broadcast volume array across scenarios."""
        return volume_array.expand_dims(scenario=self.scenarios) * self.volume_multipliers
``
