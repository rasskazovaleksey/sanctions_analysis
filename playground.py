import pandas as pd

from lib.data_loader import *


def load_data_example():
    # 1. Create instance of DataLoader
    targets = [
        ConsolidatedSanctionsTargetsLoader(),
        ConsolidatedSanctionsEntriesLoader()
    ]
    # 2. call load data to update entries
    for tar in targets:
        tar.load_and_save()


def open_in_pandas_example_cvs() -> pd.DataFrame:
    # 1. Take path from DataLoader
    path = ConsolidatedSanctionsTargetsLoader().path()
    # 2. Load data to DataFrame. Note: opensanctions have 1 entry per line.
    return pd.read_json(path, lines=True)


def open_in_pandas_example_json() -> pd.DataFrame:
    # 1. Take path from DataLoader
    path = ConsolidatedSanctionsEntriesLoader().path()
    # 2. Load data to DataFrame.
    return pd.read_json(path, lines=True)


def main():
    pass


if __name__ == "__main__":
    main()
