# -*- coding: utf-8 -*-
import os

from dotenv import dotenv_values
from pymongo.errors import CollectionInvalid
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from services.log.log_service import LogService

dotenv_values(os.path.join(os.path.abspath(os.getcwd()), '.env'))

uri = f'{os.environ["DB_DRIVER"]}{os.environ["DB_USER"]}:{os.environ["DB_PASSWORD"]}@{os.environ["DB_HOST"]}:{os.environ["DB_PORT"]}'


class Environment:
    instance = None

    def __init__(self) -> None:
        self.class_name = f'{Environment.__name__}'
        self.log = LogService.logger()
        self.log.info(f'{self.class_name} (__init__): making connection')
        self.conn = MongoClient(f"{uri}/?retryWrites=true&w=majority&ssl=false")
        self.db_daily = self.conn[os.environ['DB_NAME_DAILY']]
        self.db_users = self.conn[os.environ['DB_NAME_USERS']]

    def get_db(self):
        try:
            self.log.info(f'{self.class_name} (get_db): access database')
            return dict(daily=self.db_daily, users=self.db_users)
        except CollectionInvalid as e:
            raise ChildProcessError(e)

    @staticmethod
    def test_connection():
        return MongoClient(f"{uri}/?retryWrites=true&w=majority",
                           server_api=ServerApi('1'))

    @staticmethod
    def get_instance():
        if not Environment.instance:
            Environment.instance = Environment()
        return Environment.instance
