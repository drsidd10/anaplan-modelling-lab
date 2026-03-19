import pandas as pd
from src.time.time import PREVIOUS, CUMULATE
def test_previous(): assert PREVIOUS(pd.Series([1,2])).iloc[1]==1