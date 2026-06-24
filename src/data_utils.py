import pandas as pd
from pathlib import Path
from src.config import DATA_PATH


def load_processed_data():
    data_path = Path(__file__).parent.parent / DATA_PATH
    df = pd.read_parquet(data_path)
    return df
