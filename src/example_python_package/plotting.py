"""Functions for plotting data."""

import matplotlib.pyplot as plt
import pandas as pd


def plot_data(df: pd.DataFrame) -> None:
    """Plot the data in the DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.
    """
    df.plot()
    plt.show()
