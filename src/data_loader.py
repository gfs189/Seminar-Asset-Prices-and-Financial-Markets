"""
Data loading and cleaning functions.
Owner: Person A
"""
import pandas as pd


def load_data(path: str = "../data/raw/dataset.csv") -> pd.DataFrame:
    """Load the raw dataset."""
    df = pd.read_csv(path)
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and preprocess the dataset."""
    df = df.dropna()
    df = df.drop_duplicates()
    return df
