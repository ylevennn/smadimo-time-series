from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import kruskal, levene
from statsmodels.tsa.stattools import adfuller

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "co2.csv"

df = pd.read_csv(DATA_PATH, index_col=0)
data = df.iloc[:, 0].dropna().values


n_chunks = 4
adf_p = adfuller(data)[1]
print("ADF: " + ("Стационарный" if adf_p < 0.05 else "Нестационарный"))

diff = np.diff(data)
adf_p = adfuller(diff)[1]
print("diff ADF: " + ("Стационарный" if adf_p < 0.05 else "Нестационарный"))

chunks = np.array_split(diff, n_chunks)
_, lev_p = levene(*chunks)
_, kw_p = kruskal(*chunks)
print("Levene: " + ("Однородный" if lev_p > 0.05 else "Неоднородный"))
print("Kruskal: " + ("Однородный" if kw_p > 0.05 else "Неоднородный"))
