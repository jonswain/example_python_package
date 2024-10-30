"""Conftest for example_python_package tests."""

import pandas as pd
import pytest


@pytest.fixture
def example_dataframe():
    """Provide an example test dataset for testing."""
    return pd.DataFrame(
        {
            "A": [1, 2, 3, 4, 5],
            "B": [5, 4, 3, 2, 1],
            "C": [1, 1, 1, 1, 1],
        }
    )


@pytest.fixture
def example_dataframe_with_missing_values():
    """Provide an example test dataset for testing."""
    return pd.DataFrame(
        {
            "A": [1, None, 3, 4, 5],
            "B": [5, 4, 3, 2, None],
            "C": [1, 1, None, 1, 1],
        }
    )
