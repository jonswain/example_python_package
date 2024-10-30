"""Functional tests for the tables module."""

import pandas as pd
import pytest
from example_python_package.tables import fill_na_with_mean


def test_fill_na_with_mean_row(example_dataframe_with_missing_values):
    """Test the fill_na_with_mean function with 'row' method."""
    df = fill_na_with_mean(example_dataframe_with_missing_values, "row")
    assert df.equals(
        pd.DataFrame(
            {
                "A": [1.0, 2.5, 3.0, 4.0, 5.0],
                "B": [5.0, 4.0, 3.0, 2.0, 3.0],
                "C": [1.0, 1.0, 3.0, 1.0, 1.0],
            }
        )
    )


def test_fill_na_with_mean_column(example_dataframe_with_missing_values):
    """Test the fill_na_with_mean function with 'column' method."""
    df = fill_na_with_mean(example_dataframe_with_missing_values, "column")
    assert df.equals(
        pd.DataFrame(
            {
                "A": [1.0, 3.25, 3.0, 4.0, 5.0],
                "B": [5.0, 4.0, 3.0, 2.0, 3.5],
                "C": [1.0, 1.0, 1.0, 1.0, 1.0],
            }
        )
    )


def test_fill_na_with_mean_all(example_dataframe_with_missing_values):
    """Test the fill_na_with_mean function with 'all' method."""
    df = fill_na_with_mean(example_dataframe_with_missing_values, "all")
    assert df.round(4).equals(
        pd.DataFrame(
            {
                "A": [1.0, 2.5833, 3.0, 4.0, 5.0],
                "B": [5.0, 4.0, 3.0, 2.0, 2.5833],
                "C": [1.0, 1.0, 2.5833, 1.0, 1.0],
            }
        )
    )


def test_fill_na_with_mean_no_nan(example_dataframe):
    """Test the fill_na_with_mean function with no missing values."""
    df = fill_na_with_mean(example_dataframe, "column")
    assert df.equals(example_dataframe)


def test_fill_na_with_mean_invalid_method(example_dataframe):
    """Test the fill_na_with_mean function with invalid method."""
    with pytest.raises(ValueError):
        fill_na_with_mean(example_dataframe, "invalid")
