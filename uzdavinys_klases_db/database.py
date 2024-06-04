from typing import Literal

import pandas as pd
from pandas import DataFrame
from sqlalchemy import create_engine, inspect


URL = "sqlite:///text.db"


class PandaDB:

    def __init__(self, url: str = URL):
        self.engine = create_engine(url)
        self.data = pd.DataFrame

    def create_dataframe(self, data: list) -> DataFrame:
        self.data = pd.DataFrame(data)
        self.data.rename(columns={'0': 'Col_1'}, inplace=True)
        return self.data

    def print_info(self):
        print(self.data.info())
        print(self.data.head())
        print(self.data.tail())

    def read_data_from_DB(self, table_name: str) -> DataFrame:
        return pd.read_sql_table(table_name=table_name, con=self.engine)

    def create_table_in_DB(
            self,
            table_name: str,
            if_exists: Literal["fail", "replace", "append"] = "replace",
    ) -> None:
        self.data.to_sql(
            name=table_name,

            con=self.engine,
            if_exists=if_exists,
        )

    # def drop_all_tables_in_DB(self) -> None:
    #     with self.engine.connect() as connection:
    #         inspector = inspect(self.engine)
    #         for table_name in inspector.get_table_names():
    #             print(table_name)
    #             # connection.execute(f'DROP TABLE IF EXISTS "{table_name}" CASCADE')
