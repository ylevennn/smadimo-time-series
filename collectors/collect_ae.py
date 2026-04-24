from pathlib import Path

import pandas as pd

SOURCE_FILE = "/Users/ylevenn/Downloads/AE data 4.csv"
OUTPUT_PATH = Path(__file__).resolve().parents[1] / "data" / "ae.csv"

TIME_COL = "Time (s)"
BINS = 1000
TIME_MIN = 750
TIME_MAX = 1700

df = pd.read_csv(SOURCE_FILE)

ae = df[[TIME_COL]].copy()
ae[TIME_COL] = pd.to_numeric(ae[TIME_COL], errors="coerce")
ae = ae.dropna().sort_values(TIME_COL)
ae = ae[(ae[TIME_COL] >= TIME_MIN) & (ae[TIME_COL] <= TIME_MAX)]

ae["time_bin"] = pd.cut(ae[TIME_COL], bins=BINS)
counts = ae.groupby("time_bin", observed=False).size()
bin_centers = [interval.mid for interval in counts.index]

result = pd.DataFrame(
    {
        "time_bin_center_s": bin_centers,
        "ae_event_count": counts.values,
    }
)

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
result.to_csv(OUTPUT_PATH, index=False)
