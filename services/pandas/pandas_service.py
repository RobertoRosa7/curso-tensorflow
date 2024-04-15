# -*- coding: utf-8 -*-

import os

import pandas as pd


class PandasService:
    STORAGE = os.path.join('storage')
    SEPARATE = ';'

    def read_csv(self, source: str) -> pd.DataFrame:
        return pd.read_csv(source, sep=self.SEPARATE, encoding='utf-8', low_memory=False, dtype=str)

    def get_ids_excludes(self, df: pd.DataFrame) -> str:
        return self.SEPARATE.join(df[df['CNPJ'].isnull()]['ID'].values)

    def get_ids_duplicated(self, df: pd.DataFrame) -> str:
        return self.SEPARATE.join(df[df.duplicated('CNPJ')]['ID'].values)
