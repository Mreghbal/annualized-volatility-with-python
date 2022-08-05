import pandas as pd
import numpy as np
def annualize_vol(returns_series, periods_per_year):
    """
    Annualizes the volatilities of a set of returns:
    1- We should infer the periods per year.
    2- Periods could be day, month or quarter in dataset.
    3- Adjust your data series before the calculation to look better.
    """
    return returns_series.std() * np.sqrt(periods_per_year)