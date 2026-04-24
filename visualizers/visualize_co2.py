from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "co2.csv"

df = pd.read_csv(DATA_PATH, index_col=0)
series = df.iloc[:, 0].dropna()
series.name = "co2"

fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(series.index, series.values, color="#2a9d8f", linewidth=1.2)
ax.set_xlabel("Номер наблюдения")
ax.set_ylabel("CO2")
ax.grid(True, linestyle="--", alpha=0.4)
fig.tight_layout()
plt.show()
