# 🧹 Data Cleaning Toolkit

A collection of reusable Python functions for cleaning pandas DataFrames.

## Modules
- `missing_values` — drop or fill missing data
- `duplicates` — remove duplicate rows
- `outliers` — detect and remove outliers
- `text_cleaning` — normalize text columns
- `type_conversion` — convert column types

## Usage
```python
from cleaners import remove_duplicates, fill_missing

df = remove_duplicates(df)
df = fill_missing(df, strategy="median")
```

## Setup
```bash
pip install -r requirements.txt
```

Use this code depending on your case

Alifia G.
