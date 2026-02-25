def remove_duplicates(df, subset=None): -- This is to define a function called remove_duplicates that takes in a DataFrame (df) and an optional subset of columns (subset default is None).
    """Remove duplicate rows, optionally based on a subset of columns."""
    return df.drop_duplicates(subset=subset)