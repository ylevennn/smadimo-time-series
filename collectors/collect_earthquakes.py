from pathlib import Path

import pandas as pd

URL = (
    "https://earthquake.usgs.gov/fdsnws/event/1/query"
    "?format=csv&starttime=2011-01-01&endtime=2011-06-30"
    "&minmagnitude=4.5&minlatitude=34&maxlatitude=42"
    "&minlongitude=138&maxlongitude=146&orderby=time-asc"
)

OUTPUT_PATH = Path(__file__).resolve().parents[1] / "data" / "earthquakes.csv"

df = pd.read_csv(URL)
df["time"] = pd.to_datetime(df["time"], utc=True).dt.tz_localize(None)
df = df.set_index("time")

counts_12h = df.resample("12h").size()
all_times = pd.date_range("2011-01-01", "2011-06-30 12:00:00", freq="12h")
counts_12h = counts_12h.reindex(all_times, fill_value=0)

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
counts_12h.to_csv(OUTPUT_PATH)
