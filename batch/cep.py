# -*- coding: utf-8 -*-
import os
import sys

from keys.cep_key import CepKey as cep_key
from services.filewriter.filewriter_service import FileWriterService as fws
from services.versions.version_service import VersionService
from services.stabelishment.estabelecimento_service import EstabelecimentoService
from itertools import chain

sys.path.append(os.path.abspath(os.getcwd()))


# injection dependencies
sc_version = VersionService()
sc_esta = EstabelecimentoService()

# general variables
header = ['cep', 'cidade_estado', 'bairro', 'lougradouro', 'complemento']


def flat(matrix) -> list:
    f"""
    Version: {1.0}
    Summary: Responsible to flat matrix bidimensional to dimensional

    Params: matrix<list>
    Return: list
    """
    return list(chain.from_iterable(matrix))


def write_json(json_array: list) -> None:
    write_to = os.path.join(cep_key.STORAGE, sc_version.get_next_version(
        cep_key.FILENAME_CEP, cep_key.EXT_JSON))

    fws.write_json(json_array, write_to)


def read_csv() -> list:
    read_from = os.path.join(cep_key.STORAGE, sc_version.get_last_version(
        cep_key.FILENAME_CEP, cep_key.EXT_CSV))

    return fws.read_csv(read_from)


def write_csv(data) -> None:
    write_to = os.path.join(cep_key.STORAGE, sc_version.get_next_version(
        cep_key.FILENAME_CEP, cep_key.EXT_CSV))

    fws.save_csv_with_header(write_to, header, data)


def read_txt() -> None:
    write_csv(fws.read_txt(os.path.join(cep_key.STORAGE, 'cep.1.0.0.txt')))


def check_base_cep():
    return sc_esta.check_base()


def create_base_cep() -> None:
    """
    version: 1.0.0
    summary: Create new Database of zip code, run if not exist base on service
    """
    read_from = os.path.join(cep_key.STORAGE, sc_version.get_last_version(
        cep_key.FILENAME_CEP, cep_key.EXT_JSON))
    json_files = fws.fetch_local_cep(read_from)
    previousLine = 484621

    for index, file in enumerate(json_files[previousLine:]):
        line = index + previousLine
        left = len(json_files) - line
        try:
            sc_esta.post_all(cep_key.CREATE, data=file)
            print('[cep] (create_base_cep) : line: {} left {} saved {}'.format(
                line, left, file.get('cep')))
        except Exception as e:
            print(e)
            print('[cep] (create_base_cep) : line: {} left {} saved {}'.format(
                line, left, file.get('cep')))


if __name__ == '__main__':
    # write_json(read_csv())
    # create_base_cep()
    sc_esta.get_url(cep_key.CHECK)
    check_base_cep().subscribe(lambda result: print(result))
