import pandas as pd

from lib.data_loader import *


def load_data_example():
    # 1. Create instance of DataLoader
    targets = [
        ConsolidatedSanctionsTargetsLoader(),
        ConsolidatedSanctionsEntriesLoader(),
        DefaultSanctionsEntriesLoader()
    ]
    # 2. call load data to update entries
    for tar in targets:
        tar.load_and_save()


def open_data_frame_example() -> pd.DataFrame:
    # 1. Take DataLoader
    loader = ConsolidatedSanctionsEntriesLoader()
    # 2. Call open function
    return loader.open()


def main():
    DefaultSanctionsEntriesLoader().load_and_save()


if __name__ == "__main__":
    main()
