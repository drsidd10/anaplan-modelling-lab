# saved_views.py — Anaplan-style Saved Views
import xarray as xr

def create_saved_view(dataset, filters):
    """
    dataset: xr.Dataset
    filters: dict -> {dimension: [values]}
    """
    view = dataset
    for dim, vals in filters.items():
        view = view.sel({dim: vals})
    return view
