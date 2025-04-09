import pandas as pd
import ssl
import urllib.request
from pathlib import Path

# Get the absolute path to the project's "data" directory
DATA_DIR = Path(__file__).resolve().parents[1] / "data"

def download_blockchain_metric(metric_name, save_as):
    base_url = f"https://api.blockchain.info/charts/{metric_name}?timespan=5y&format=csv"
    response = urllib.request.urlopen(base_url, context=ssl._create_unverified_context())
    df = pd.read_csv(response)
    df.columns = ['Date', metric_name]
    df['Date'] = pd.to_datetime(df['Date'])
    df.to_csv(DATA_DIR / f"{save_as}.csv", index=False)
    return df

