import json
import pandas as pd

# Load Excel file
df = pd.read_excel("media.xlsx")

# Convert DataFrame to Python dictionary records
data = df.to_dict(orient="records")

# Save as clean JSON without escaped slashes and preserving UTF-8 characters
with open("media.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ Converted media.xlsx to clean media.json successfully!")