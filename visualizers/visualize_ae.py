from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "ae.csv"

df = pd.read_csv(DATA_PATH)

cumulative_mean = df["ae_event_count"].expanding().mean()

fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

axes[0].plot(df["time_bin_center_s"], df["ae_event_count"], color="#c0392b")
axes[0].set_ylabel("Количество событий акустической эмиссии")
axes[0].grid(True, alpha=0.3)

axes[1].plot(df["time_bin_center_s"], cumulative_mean, color="tab:orange")
axes[1].set_xlabel("Время в секундах")
axes[1].set_ylabel("Среднее число событий")
axes[1].grid(True, alpha=0.3)

fig.tight_layout()
plt.show()
