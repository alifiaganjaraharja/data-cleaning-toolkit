def remove_outliers_iqr(df, column): -- This function takes a DataFrame and a column name as input and return a new DataFrame with the outliers removed based on the interquartile range (IQR) method.
    """Remove utliers using the interquartile range (IQR) method."""
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    return df[(df[column] >= Q1 - 1.5 * IQR) & (df[column] <=Q3 + 1.5 * IQR)]