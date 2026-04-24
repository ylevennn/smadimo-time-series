from pathlib import Path

import yfinance as yf

OUTPUT_PATH = Path(__file__).resolve().parents[1] / "data" / "usdt_usd_2026-04-19.csv"

df = yf.download("USDT-USD", period="5d", interval="1m")
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT_PATH)

