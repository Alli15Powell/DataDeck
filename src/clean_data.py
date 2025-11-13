import pandas as pd
import os

# Paths
RAW_DIR = "data/raw"
CLEAN_DIR = "data/cleaned"
os.makedirs(CLEAN_DIR, exist_ok=True)

# Load Main Steam Dataset
steam_df = pd.read_csv(
    os.path.join(RAW_DIR, "steam.csv"),
    encoding="utf-8",
    on_bad_lines="skip",
    low_memory=False
)

# Keep only the most useful columns
columns_to_keep = [
    "appid", "name", "release_date", "developer", "publisher",
    "platforms", "required_age", "categories", "genres",
    "positive_ratings", "negative_ratings", "price"
]
steam_df = steam_df[columns_to_keep]

# Clean missing or invalid data
steam_df = steam_df.dropna(subset=["name", "genres"])
steam_df["price"] = steam_df["price"].fillna(0)

# Save to cleaned folder
steam_df.to_csv(os.path.join(CLEAN_DIR, "steam_cleaned.csv"), index=False)
print("steam_cleaned.csv saved successfully!")

# Optional: Clean tag or requirements files if you want to use them later
# (Skip this for now to stay focused on the core dashboard)
