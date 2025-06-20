import pandas as pd

# Raw Product Dimension
data = {
    "product_id": ["1", "2", "03", "004"],              # gemengde string‐formatting
    "product_name": ["Widget", None, "Doohickey", "Gadget"],  # één missing
    "category": ["Tools", "Electronics", "", None],           # empty & None
    "legacy_code": ["W-100", "G-200", "D-300", "G-400"],    # extra kolom
}
df = pd.DataFrame(data)
df.to_csv("raw_product_dim.csv", index=False)
print("Wrote raw_product_dim.csv")
