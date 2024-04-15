# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.abspath(os.getcwd()))

from services.versions.version_service import VersionService
from services.filewriter.filewriter_service import FileWriterService as fws
from keys.generate_key import GenerateKey as key

# injection dependencies
ver_service = VersionService()


def write_json(json_array: list):
    write_to = os.path.join(key.STORAGE, ver_service.get_next_version(key.FILENAME_CEP, key.EXT_JSON))
    fws.write_json(json_array, write_to)


def read_csv():
    latest_cep_version = ver_service.get_last_version(key.FILENAME_CEP, key.EXT_CSV)
    read_from = os.path.join(key.STORAGE, latest_cep_version)

    # read csv file
    return fws.read_csv(read_from)


if __name__ == '__main__':
    write_json(read_csv())
