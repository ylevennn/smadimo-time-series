from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "usdt_usd_2026-04-19.csv"

df = pd.read_csv(DATA_PATH, header=[0, 1], index_col=0, skiprows=[2])
df.index = pd.to_datetime(df.index, errors="coerce")
df = df[df.index.notna()]
close = df[("Close", "USDT-USD")].astype(float).dropna()

days = close.index.normalize().unique()
day = days[0]
close_day = close[close.index.normalize() == day]

log_ret = np.log(close_day / close_day.shift(1)).dropna()

fig, axes = plt.subplots(2, 1, figsize=(14, 8), sharex=True)

axes[0].plot(close_day.index, close_day.values, color="tab:blue")
axes[0].set_ylabel("Close, USD")
axes[0].grid(True)

axes[1].plot(log_ret.index, log_ret.values, color="tab:orange")
axes[1].axhline(0, color="black", linewidth=0.8)
axes[1].set_title("Log returns")
axes[1].set_xlabel("Time")
axes[1].set_ylabel("log(P_t / P_{t-1})")
axes[1].grid(True)

fig.tight_layout()
plt.show()
