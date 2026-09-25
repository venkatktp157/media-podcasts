import json
import pandas as pd

# 1. Paste your Vercel Blob base storage URL here (ending with /)
BLOB_BASE_URL = "https://public.blob.vercel-storage.com/"

# Load Excel file
df = pd.read_excel("media.xlsx")

# Update filename column to use the Vercel Blob URL prefix
if "filename" in df.columns:
    df["filename"] = df["filename"].astype(str).apply(
        lambda f: f if f.startswith("http://") or f.startswith("https://") 
        else f"{BLOB_BASE_URL.rstrip('/')}/{f.lstrip('/')}"
    )

# Convert DataFrame to Python dictionary records
data = df.to_dict(orient="records")

# Save as clean JSON without escaped slashes and preserving UTF-8 characters
with open("media.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ Converted media.xlsx to clean media.json with Vercel Blob URLs!")