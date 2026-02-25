import pandas as pd -- This is to import the pandas library to Python.

def drop_missing(df, threshold=0.5): -- This is to define a function called drop_missing that takes in a DataFrame (df) and a threshold value (threshold default is 0.5).
    """Drop columns where missing values exceed the thrreshold."""
    return df.dropna(thresh=int(threshold * len(df), axis=1)

def fill_missing(df, strategy="mean"): -- This is to define a function called fill_missing that takes in a DataFrame (df) and a strategy for filling missing values (strategy default is "mean").
    """Fill missing values with mean, median, or mode."""
    for col in df.select_dtypes(include)="number").columns:
        if strategy == "mean":
            df[col].fillna(df[col].mean(), inplace=Ture)
        elif strategy == "median":
            df[col].fillna(df[col].median(), inplace=True)
    return df   