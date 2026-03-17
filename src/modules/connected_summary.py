
# connected_summary.py — Consolidates FP&A, Workforce, and S&OP into one dataset
import xarray as xr

def consolidate(fpna_ds, workforce_ds, sop_ds):
    return xr.Dataset({
        'Revenue': fpna_ds.get('Revenue'),
        'EBITDA': fpna_ds.get('EBITDA'),
        'FCF': fpna_ds.get('FCF'),
        'NPV': fpna_ds.get('NPV'),
        'WorkforceCost': workforce_ds.get('Cost'),
        'Inventory': sop_ds.get('Inventory')
    })
