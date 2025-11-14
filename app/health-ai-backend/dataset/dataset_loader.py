import pandas as pd
import os

def load_all_datasets():
    folder_path = os.path.dirname(__file__)
    datasets = {}

    for file in os.listdir(folder_path):
        if file.endswith(".csv"):
            path = os.path.join(folder_path, file)
            df = pd.read_csv(path)
            datasets[file] = df
            print(f"✅ Loaded {file} with {len(df)} rows")

    return datasets
