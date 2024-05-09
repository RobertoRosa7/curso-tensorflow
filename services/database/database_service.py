# -*- coding: utf-8 -*-
import os
import sys

from dotenv import dotenv_values
from pymongo.errors import CollectionInvalid
from pymongo.mongo_client import MongoClient
from services.log.log_service import LogService
from pymongo.server_api import ServerApi

# import certifi

DIR_ROOT = os.path.abspath(os.getcwd())

sys.path.append(os.path.abspath(os.path.join(DIR_ROOT)))

from services.log.log_service import LogService

ENV_FILE = os.path.join(DIR_ROOT, '.env')


def check_env_file() -> bool:
    return os.path.exists(ENV_FILE)


def get_environment():
    return os.environ if not check_env_file() else dotenv_values(ENV_FILE)


def build_environment(env):
    return dict(
            DB_DRIVER=env['DB_DRIVER'],
            DB_HOST=env['DB_HOST'],
            DB_USER=env['DB_USER'],
            DB_PASSWORD=env['DB_PASSWORD'],
            DB_PORT=env['DB_PORT'],

            EMAIL_SUPPORT=env['EMAIL_SUPPORT'],
            EMAIL_SUPPORT_PASS=env['EMAIL_SUPPORT_PASS'],
            ENV=env['EMAIL_SUPPORT_PASS'],
            DB_NAME=env['DB_NAME'],
            BASE_URL=env['BASE_URL'],
            JWT_SECRET=env['JWT_SECRET']
    )


get_env = build_environment(get_environment())
uri = f'{get_env["DB_DRIVER"]}{get_env["DB_USER"]}:{get_env["DB_PASSWORD"]}@{get_env["DB_HOST"]}:{get_env["DB_PORT"]}'

class Environment:
    instance = None

    def __init__(self) -> None:
        self.prefix = f'{Environment.__name__}: started'
        # when to use SSL
        # uri = f"{environment['MONGO_URI']}/?retryWrites=true&w=majority", tlsCAFile = certifi.where()

        self.conn = MongoClient(f"{uri}/?retryWrites=true&w=majority&ssl=false")
        self.db = self.conn[get_env['DB_NAME']]

    def get_db(self):
        try:
            LogService.logger().info(f'{self.prefix}: access database')
            return self.db
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