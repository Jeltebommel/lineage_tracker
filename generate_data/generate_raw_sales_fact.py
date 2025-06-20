import pandas as pd
import numpy as np
from random import choice, randint, uniform

# Laad raw dims
prod = pd.read_csv("raw_product_dim.csv", dtype=str)
date = pd.read_csv("raw_date_dim.csv")

n = 100
df = pd.DataFrame({
    "sale_id": range(1, n+1),
    # gemixte formats + blanks
    "sale_date": [choice(date["date"].tolist()+[""]) for _ in range(n)],
    # soms missing, soms letter
    "product_id": [choice(prod["product_id"].tolist()+[None,"X"]) for _ in range(n)],
    # quantity als int, string, of 0
    "quantity": [choice([randint(0,20), str(randint(1,10)), None]) for _ in range(n)],
    # revenue met $ of negatieve waarden
    "revenue": [choice([f"${uniform(5,200):.2f}", uniform(-100,500), None]) for _ in range(n)],
    "notes": [choice(["", "urgent", None]) for _ in range(n)],  # extra kolom
})
df.to_csv("raw_sales_fact.csv", index=False)
print("Wrote raw_sales_fact.csv")
