import pandas as pd

def drop_missing(df, threshold=0.5):
    """Drop columns where missing values exceed the threshold."""
    return df.dropna(thresh=int(threshold * len(df)), axis=1)

def fill_missing(df, strategy="mean"):
    """Fill missing values with mean, median, or mode."""
    for col in df.select_dtypes(include="number").columns:
        if strategy == "mean":
            df[col].fillna(df[col].mean(), inplace=True)
        elif strategy == "median":
            df[col].fillna(df[col].median(), inplace=True)
    return df