"""
Analysis and statistics functions.
Owner: Person B
"""
import pandas as pd


def run_eda(df: pd.DataFrame) -> None:
    """Print basic exploratory data analysis."""
    print(df.describe())
    print(df.dtypes)


def run_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """Run statistical analysis and return results."""
    results = df.describe()
    return results
