import sqlite3
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent

CSV_PATH = PROJECT_ROOT / "data" / "processed" / "estateiq_processed.csv"
DB_PATH = PROJECT_ROOT / "data" / "estateiq.db"

TABLE_NAME = "estateiq_processed"


if not CSV_PATH.exists():
    raise FileNotFoundError(
        f"Processed dataset not found: {CSV_PATH}"
    )


print("Loading processed dataset...")

df = pd.read_csv(CSV_PATH)

print(f"Records: {len(df):,}")
print(f"Columns: {len(df.columns)}")


# Normalize AREA into a numeric field
if "AREA" in df.columns:

    df["AREA"] = (
        df["AREA"]
        .astype(str)
        .str.replace(",", "", regex=False)
        .str.extract(r"([\d.]+)", expand=False)
    )

    df["AREA"] = pd.to_numeric(
        df["AREA"],
        errors="coerce"
    )


# Normalize numeric analytical fields
numeric_columns = [
    "PRICE_SQFT",
    "BEDROOM_NUM",
    "BATHROOM_NUM",
    "BALCONY_NUM",
    "FLOOR_NUM",
    "TOTAL_FLOOR",
]

for column in numeric_columns:

    if column in df.columns:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )


print()
print("Database field validation")
print("-" * 40)

print(f"AREA dtype: {df['AREA'].dtype}")

print(
    f"Valid AREA values: "
    f"{df['AREA'].notna().sum():,}"
)

print(
    f"Missing AREA values: "
    f"{df['AREA'].isna().sum():,}"
)


# Create database directory
DB_PATH.parent.mkdir(
    parents=True,
    exist_ok=True
)


# Create / replace SQLite database
connection = sqlite3.connect(DB_PATH)

df.to_sql(
    TABLE_NAME,
    connection,
    if_exists="replace",
    index=False
)


connection.close()


print()
print("SQLite database created successfully.")
print(f"Database: {DB_PATH}")
print(f"Table: {TABLE_NAME}")