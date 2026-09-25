import json
import pandas as pd

# Load Excel file
df = pd.read_excel("media.xlsx")

# Automatically prefix 'media/' to filename if it isn't already present
if "filename" in df.columns:
    df["filename"] = df["filename"].astype(str).apply(
        lambda f: f if f.startswith("media/") else f"media/{f}"
    )

# Convert DataFrame to Python dictionary records
data = df.to_dict(orient="records")

# Save as clean JSON without escaped slashes and preserving UTF-8 Hindi characters
with open("media.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ Converted media.xlsx to clean media.json successfully!")