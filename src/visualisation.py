"""
Visualisation functions.
Owner: Person B
"""
import matplotlib.pyplot as plt
import pandas as pd


def plot_results(results: pd.DataFrame) -> None:
    """Plot key results."""
    fig, ax = plt.subplots(figsize=(10, 6))
    results.T.plot(kind="bar", ax=ax)
    ax.set_title("Analysis Results")
    plt.tight_layout()
    plt.savefig("../figures/results.png", dpi=150)
    plt.show()
