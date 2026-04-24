from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "earthquakes.csv"

df = pd.read_csv(DATA_PATH, index_col=0, parse_dates=[0])
series = df.iloc[:, 0]
series.name = "count"

cumulative_mean = series.expanding().mean()

fig, axes = plt.subplots(2, 1, figsize=(14, 8), sharex=True)

axes[0].plot(series.index, series.values, label="Число событий за 12 часов")
axes[0].axvline(pd.Timestamp("2011-03-11"), linestyle="--", color="red", label="t_c")
axes[0].axvline(pd.Timestamp("2011-03-08"), linestyle="--", color="green", label="t_EW")
axes[0].set_ylabel("Количество землетрясений")
axes[0].legend()
axes[0].grid(True)

axes[1].plot(
    cumulative_mean.index,
    cumulative_mean.values,
    color="tab:orange",
    label="Окно со скользящей правой границей",
)
axes[1].axvline(pd.Timestamp("2011-03-11"), linestyle="--", color="red", label="t_c")
axes[1].axvline(pd.Timestamp("2011-03-08"), linestyle="--", color="green", label="t_EW")
axes[1].set_xlabel("Дата")
axes[1].set_ylabel("Среднее число событий")
axes[1].legend()
axes[1].grid(True)

fig.tight_layout()
plt.show()
