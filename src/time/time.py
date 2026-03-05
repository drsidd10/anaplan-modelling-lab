# time.py — Anaplan-style Time Functions (Python)

import pandas as pd

def make_time_range(start="2026Q1", periods=8):
    return pd.period_range(start=start, periods=periods, freq="Q")

def PREVIOUS(series):
    """Equivalent of Anaplan PREVIOUS() — shift by one period."""
    return series.shift(1)

def CUMULATE(series):
    """Equivalent of Anaplan CUMULATE()."""
    return series.cumsum()

def TIMESUM(series, start, end):
    """SUM across a time window (Anaplan TIMESUM)."""
    return series.loc[start:end].sum()

def select_range(series, start, end):
    """Return sub-range (useful for Time Ranges)."""
    return series.loc[start:end]
