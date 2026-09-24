import pandas as pd

# Load Excel file
df = pd.read_excel("media.xlsx")

# Convert to JSON with native UTF-8 character preservation
df.to_json("media.json", orient="records", indent=2, force_ascii=False)

print("✅ Converted media.xlsx to media.json successfully!")