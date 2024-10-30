"""Functions for creating and manipulating tables of data."""

import pandas as pd


def fill_na_with_mean(df: pd.DataFrame, how: str) -> pd.DataFrame:
    """Fill missing values with the mean as specified.



    Args:
        df (pd.DataFrame): The input DataFrame.
        how (str): The method to use for filling missing values. Options are "row",
                   "column", or "all".

    Returns:
        pd.DataFrame: The DataFrame with missing values filled.
    """
    if how == "row":
        return df.apply(lambda row: row.fillna(row.mean()), axis=1)
    elif how == "column":
        return df.apply(lambda col: col.fillna(col.mean()), axis=0)
    elif how == "all":
        return df.fillna(df.mean().mean())
    else:
        raise ValueError(f"Invalid value for 'how': {how}")
