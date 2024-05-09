# -*- coding: utf-8 -*-
import json
import os
from datetime import datetime

import pandas as pd
from services.log.log_service import LogService

class PandasService:
    instance = None
    STORAGE = os.path.join('storage')
    SEPARATE = ';'

    def __init__(self):
        super().__init__()
        self.prefix = f"{PandasService.__name__} starting"
        self.log = LogService.logger()

        # self.log.info(f"{self.prefix}: SentimentCollection")
        # self.collection = self.db().get_collection("SentimentCollection")

    def read_csv(self, source: str) -> pd.DataFrame:
        return pd.read_csv(source, sep=self.SEPARATE, encoding='utf-8', low_memory=False, dtype=str)

    def get_ids_excludes(self, df: pd.DataFrame) -> str:
        return self.SEPARATE.join(df[df['CNPJ'].isnull()]['ID'].values)

    def get_ids_duplicated(self, df: pd.DataFrame) -> str:
        return self.SEPARATE.join(df[df.duplicated('CNPJ')]['ID'].values)


    def get_dataframe(self, collections) -> pd.DataFrame:
        self.log.info(f'{self.prefix}: return dataframe')
        return pd.DataFrame.from_records(collections)

    def update_classifier(self):
        self.log.info(f"{self.prefix}: update_classifier making pandas read csv")
        df_ws = pd.read_csv(f'{self.base_url}/ms-daily/what-happen/to-csv', sep=';')
        df_ss = pd.read_csv(f'{self.base_url}/ms-daily/sentiment/to-csv', sep=';')

        self.log.info(f"{self.prefix}: add new column foreign key to dataframe")
        df_ws["foreign_id"] = df_ss["what_happen_id"]

        self.log.info(f"{self.prefix}: filter id null")
        no_classifier = df_ws[df_ws["foreign_id"].isnull()]

        self.log.info(f"{self.prefix}: convert dataframe to json")
        body = no_classifier[
            no_classifier.columns.difference(["foreign_id"])].to_json(
                orient='records',
                force_ascii=False)
        self.log.info(f"{self.prefix}: return dict " + str(body))
        return json.loads(body)

    def find_model_by_metrics(self, records) -> dict:
        self.log.info(f'{self.prefix}: find model by metrics')
        df = pd.DataFrame.from_records(records)

        self.log.info(f'{self.prefix}: filter dataframe by max values')
        result = df[df['accuracy_score'] == df['accuracy_score'].max()]

        self.log.info(f'{self.prefix}: return model selected')
        return result.to_dict(orient="records")[0]

    def get_chart(self, collections):
        """
        this method is responsible to create information of chart where will be
        shown on frontend

        Returns
        -------
        dict
        """
        self.log.info(f'{self.prefix}: using pandas to fetch some data on col')
        df = pd.DataFrame.from_records(collections)

        return df['sentiment'].value_counts().map(lambda x: (x / df.shape[0]) * 100).to_dict()

    def read_messages(self, filename: str) -> pd.DataFrame:
        dateparse = lambda x: datetime.strptime(x, '%d/%m/%Y %H:%M')

        df = pd.read_csv(os.path.join(f'csv_files', filename), sep=";",
                         dtype=str, parse_dates=['date'], date_parser=dateparse)
        df['time_diff'] = df['date'].diff()
        df['time_diff'] = df['time_diff'].fillna(pd.Timedelta(seconds=0))

        return df

    def load_records(self, collections):
        return pd.DataFrame.from_records(collections)

    @staticmethod
    def get_instance():
        if not PandasService.instance:
            PandasService.instance = PandasService()
        return PandasService.instance