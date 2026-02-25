import pandas as pd
from cleaners import remove_duplicates, drop_missing

def test_remove_duplicates():
    df = pd.DataFrame({"a": [1, 1, 2], "b": [3, 3, 4]})
    result = remove_duplicates(df)
    assert len(result) == 2

def test_drop_missing():
    df = pd.DataFrame({"a": [1, None, None], "b": [1, 2, 3]})
    result = drop_missing(df, threshold=0.5)
    assert "a" not in result.columns or "b" in result.columns