from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import kruskal, levene
from statsmodels.tsa.stattools import adfuller, kpss

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "usdt_usd_2026-04-19.csv"


df = pd.read_csv(DATA_PATH, header=[0, 1], index_col=0, skiprows=[2])
df.index = pd.to_datetime(df.index, errors="coerce")
df = df[df.index.notna()]

close = df[("Close", "USDT-USD")].astype(float).dropna()

days = close.index.normalize().unique()
day = days[0]
close_day = close[close.index.normalize() == day]

log_ret = np.log(close_day / close_day.shift(1)).dropna()
log_ret.name = "log_return"


adf_p = adfuller(log_ret, autolag="AIC")[1]
kpss_p = kpss(log_ret, regression="c", nlags="auto")[1]

parts = np.array_split(log_ret.values, 4)
_, lev_p = levene(*parts)
_, kw_p = kruskal(*parts)

results = {
    "adf_p": adf_p,
    "kpss_p": kpss_p,
    "levene_p": lev_p,
    "kruskal_p": kw_p,
}


print(
    f"ADF:     {'Стационарный' if results['adf_p'] < 0.05 else 'Нестационарный'} (p={results['adf_p']:.4f})"
)
print(
    f"KPSS:    {'Стационарный' if results['kpss_p'] > 0.05 else 'Нестационарный'} (p={results['kpss_p']:.4f})"
)
print(
    f"Levene:  {'Однородный' if results['levene_p'] > 0.05 else 'Неоднородный'} (p={results['levene_p']:.4f})"
)
print(
    f"Kruskal: {'Однородный' if results['kruskal_p'] > 0.05 else 'Неоднородный'} (p={results['kruskal_p']:.4f})"
)
