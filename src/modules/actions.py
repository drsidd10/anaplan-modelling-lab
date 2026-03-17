# actions.py — Import/Export Actions
import pandas as pd

def export_to_csv(dataset, filename):
    df = dataset.to_dataframe()
    df.to_csv(filename)
    return filename

def import_from_csv(filename):
    return pd.read_csv(filename)
