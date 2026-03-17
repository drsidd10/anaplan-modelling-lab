
# connected_kpis.py — KPI extraction functions
import xarray as xr

def extract_kpis(consolidated):
    return {
        'Revenue_Total': float(consolidated['Revenue'].sum()),
        'EBITDA_Total': float(consolidated['EBITDA'].sum()),
        'FCF_Total': float(consolidated['FCF'].sum()),
        'NPV': consolidated['NPV'].values.tolist(),
        'Workforce_Cost_Total': float(consolidated['WorkforceCost'].sum()),
        'Ending_Inventory': float(consolidated['Inventory'][-1])
    }
