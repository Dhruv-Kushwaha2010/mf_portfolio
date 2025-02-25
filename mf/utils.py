import plotly.graph_objects as go
import pandas as pd
import numpy as np
import os
from tqdm import tqdm
from IPython.display import display


def plot_correlation_matrix(df, width=800, height=600):
    """
    Create a correlation matrix heatmap using plotly with red-green color scheme.
    Parameters:
    df (pandas.DataFrame): Input dataframe
    width (int): Width of the plot in pixels
    height (int): Height of the plot in pixels
    Returns:
    plotly.graph_objects.Figure: Correlation matrix plot
    """
    # Calculate correlation matrix
    corr_matrix = df[df.columns[::-1]].corr()

    # Reverse the order of columns to get diagonal from top-right to bottom-left
    corr_matrix = corr_matrix[corr_matrix.columns[::-1]]

    # Create custom color scale (red for negative, green for positive)
    colors = [[0, "red"], [0.5, "white"], [1, "green"]]

    # Create heatmap
    fig = go.Figure(
        data=go.Heatmap(
            z=corr_matrix,
            x=corr_matrix.columns,
            y=corr_matrix.index,
            zmin=-1,
            zmax=1,
            colorscale=colors,
            text=np.round(corr_matrix, 2),  # Round to 2 decimal places
            texttemplate="%{text}",  # Show the text for all cells
            textfont={"size": 10},
            hoverongaps=False,
            hovertemplate="%{x} vs %{y}<br>Correlation: %{z:.2f}<extra></extra>",
        )
    )

    # Update layout
    fig.update_layout(
        width=width,
        height=height,
        title="Correlation Matrix",
        xaxis_title="Features",
        yaxis_title="Features",
        xaxis={"side": "bottom"},
        yaxis={"side": "left"},
    )

    return fig


def path_from_relative_path(relative_path):
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the CSV file
    file_path = os.path.join(script_dir, relative_path)
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the CSV file
    file_path = os.path.join(script_dir, relative_path)

    return file_path
