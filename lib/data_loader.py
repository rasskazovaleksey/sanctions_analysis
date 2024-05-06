from abc import abstractmethod
from pathlib import Path

import requests
import tqdm

import pandas as pd


class DataLoader:
    """
    Interface for data loading
    """

    @abstractmethod
    def url(self) -> str:
        """
        Private holder for url
        :return: url data source
        """
        pass

    @abstractmethod
    def path(self) -> Path:
        """
        Local location of data corresponding to project root
        :return:
        """
        pass

    @abstractmethod
    def open(self) -> pd.DataFrame:
        """
        Opens local file in pandas.DataFrame if exists
        :return: pd.DataFrame
        """
        pass

    def load_and_save(self):
        """
        loads data from source and saves data directory
        """
        print(f"INFO: Loading '{self.path()}' file from '{self.url()}'")
        response = requests.request("GET", self.url(), stream=True)

        total_size = int(response.headers.get("content-length", 0))
        block_size = 1024

        if response.status_code == 200:
            self.path().parent.mkdir(exist_ok=True)
            with tqdm.tqdm(total=total_size, unit="B", unit_scale=True) as progress_bar:
                with open(self.path(), 'w+b') as file:
                    for data in response.iter_content(block_size):
                        progress_bar.update(len(data))
                        file.write(data)
        else:
            response.raise_for_status()  # Will only raise for 4xx codes, so...
            raise RuntimeError(f"Request to {self.url()} returned status code {response.status_code}")


class ConsolidatedSanctionsTargetsLoader(DataLoader):

    def open(self) -> pd.DataFrame:
        return pd.read_csv(self.path())

    def url(self) -> str:
        return "https://data.opensanctions.org/datasets/20240506/sanctions/targets.simple.csv"

    def path(self) -> Path:
        return Path("data/sanctions_targets.csv")


class ConsolidatedSanctionsEntriesLoader(DataLoader):

    def open(self) -> pd.DataFrame:
        # 1. Take path from DataLoader
        path = self.path()
        # 2. Load data to DataFrame. Note: opensanctions have 1 entry per line.
        return pd.read_json(path, lines=True)

    def url(self) -> str:
        return "https://data.opensanctions.org/datasets/20240506/sanctions/entities.ftm.json"

    def path(self) -> Path:
        return Path("data/sanctions_entries.json")
