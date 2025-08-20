# email: 23f2002842@ds.study.iitm.ac.in
# This is a Marimo notebook demonstrating interactive data analysis.

import marimo

__generated_with = "0.9.0"
app = marimo.App()


# Cell 1: Import dependencies and create sample dataset
# Data will be reused in downstream cells
@app.cell
def __():
    import pandas as pd
    import numpy as np

    # Create a simple dataset
    np.random.seed(42)
    data = pd.DataFrame({
        "x": np.linspace(0, 10, 100),
        "y": np.linspace(0, 10, 100) + np.random.normal(0, 1, 100)
    })
    data.head()
    return data, np, pd


# Cell 2: Create an interactive slider
# Slider value will be used by later cells for filtering/analysis
@app.cell
def __():
    import marimo as mo

    slider = mo.ui.slider(start=0, stop=10, step=1, value=5, label="Select X cutoff")
    slider
    return slider,


# Cell 3: Filter the dataset based on slider
# This cell depends on both the dataset and the slider
@app.cell
def __(data, slider):
    cutoff = slider.value
    filtered = data[data["x"] <= cutoff]
    filtered.head()
    return cutoff, filtered


# Cell 4: Plot relationship between variables
# Plot will dynamically update based on slider
@app.cell
def __(filtered):
    import matplotlib.pyplot as plt

    plt.scatter(filtered["x"], filtered["y"])
    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.title("Scatter plot of filtered data")
    plt.show()
    return


# Cell 5: Dynamic markdown output
# Markdown text updates based on the slider value
@app.cell
def __(cutoff, mo):
    mo.md(f"""
    ### Analysis Summary  
    You selected a cutoff of **{cutoff}**.  
    The dataset is filtered to include only rows where `x <= {cutoff}`.  
    This demonstrates variable dependencies and interactive filtering.
    """)
    return


if __name__ == "__main__":
    app.run()
# This code is a Marimo notebook that demonstrates interactive data analysis
# using a slider to filter a dataset and visualize the results.
# It includes cells for importing dependencies, creating a dataset,
# filtering based on user input, plotting, and displaying dynamic markdown.