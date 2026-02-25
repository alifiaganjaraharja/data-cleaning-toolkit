def convert_to_datetime(df, column): -- This function takes a DataFrame and a column name as input, and converts the specified column to datetime format using the pandas library. If there are any errors during the conversion (e.g., invalid date formats), those entries will be set to NaT (Not a Time) due to the 'coerce' option.
    """Convert a column to datetime format."""
    df[column] = pd.to_datetime(df[column], errors='coerce')
    return df

def convert_to_numeric(df, column): -- This function take a DataFrame and a column name as input, and converts the specified column to numeric format.
    """Convert a column to numeric, coercing errors to NaN."""
    df[column] = pd.to_numeric(df[column], errors='coerce')
    return df