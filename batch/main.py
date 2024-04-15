# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.abspath(os.getcwd()))

from keys.estabelecimento_key import EstabelecimentoKey as esta_key
from services.log.log_service import LogService
from services.stabelishment.estabelecimento_service import EstabelecimentoService
from services.filewriter.filewriter_service import FileWriterService
from services.pandas.pandas_service import PandasService
from services.versions.version_service import VersionService

# injection dependencies
estaService = EstabelecimentoService()
fileService = FileWriterService()
pdService = PandasService()
logService = LogService()
verService = VersionService()


def download_csv() -> None:
    logService.info('(download_csv): making downloading...')
    response = estaService.get_csv(esta_key.export_csv)

    logService.info('(download_csv): saving... csv')
    fileService.save_csv(verService.get_next_version(esta_key.FILENAME, esta_key.EXT_CSV), response)

    logService.info('(download_csv): success...')


def delete_all() -> None:
    logService.info('(delete_all): new instance of pandas and read csv')
    df = pdService.read_csv(estaService.get_url(esta_key.export_csv))

    logService.info('(delete_all): get all ids to remove')
    ids_null = pdService.get_ids_excludes(df)

    logService.info('(delete_all): get all ids duplicated to remove')
    ids_duplicated = pdService.get_ids_duplicated(df)

    logService.info('(delete_all): join ids duplicated and ids null')
    ids = ids_duplicated + ids_null

    if len(ids) > 0:
        logService.info('(delete_all): making request to services')
        estaService.delete_all(esta_key.delete_all, {'data': ids})

    logService.info('(delete_all): success...')


def start() -> None:
    delete_all()
    download_csv()


if __name__ == '__main__':
    logService.info('(__main__): started...')
    start()
