import re

def lowercase_columns(df): -- This function takes a DataFrame as input and converts all string columns to lowercase.
    """Convert all string columns to lowercase."""
    str_cols = df.select_dtypes(include=['object']).columns
    df[str_cols] = df[str_cols].apply(lambda x: x.str.lower())
    return df

def remove_special_characters(df, column): -- This function takes a DataFrame and a column name as input and removes special characters from the specified text column.
    "Remove special characters from a text column in a DataFrame."
    df[column] = df[column].apply(lambda x: re.sub(r'[^a-zA-Z0-9 ]', '',str(x)))
    return df