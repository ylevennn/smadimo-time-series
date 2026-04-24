from pathlib import Path

import pandas as pd
from statsmodels.datasets import co2

OUTPUT_PATH = Path(__file__).resolve().parents[1] / "data" / "co2.csv"

data = co2.load_pandas().data["co2"].dropna().values
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
pd.DataFrame(data).to_csv(OUTPUT_PATH)

