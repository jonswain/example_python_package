from unittest.mock import patch

from example_python_package.plotting import plot_data


def test_plot_data(example_dataframe):
    with patch("example_python_package.plotting.plt.show") as mock_show:
        plot_data(example_dataframe)
        mock_show.assert_called_once()
