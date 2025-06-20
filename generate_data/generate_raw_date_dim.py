import pandas as pd
from datetime import datetime, timedelta
from random import choice

# Raw Date Dimension
start = datetime(2025, 1, 1)
dates = [start + timedelta(days=i) for i in range(90)]
# Bewaar in verschillende string‐formaten
date_strs = [d.strftime(choice(["%Y-%m-%d","%d/%m/%Y","%b %d, %Y"])) for d in dates]
df = pd.DataFrame({
    "date_key": [d.strftime("%Y%m%d") for d in dates] + [dates[5].strftime("%Y%m%d")],  # dup
    "date": date_strs + [""],    # lege waarde voor missing
    "year": [d.year for d in dates] + [None],
    "month": [d.month for d in dates] + [0],
    "day": [d.day for d in dates] + [99],
    "weekday": [d.strftime("%A") for d in dates] + ["N/A"],
})
df.to_csv("raw_date_dim.csv", index=False)
print("Wrote raw_date_dim.csv")
