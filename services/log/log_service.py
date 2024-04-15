# -*- coding: utf-8 -*-

import logging
from datetime import datetime


class LogService:
    date_log = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    logging.basicConfig(filename='logs/batch.log', level=logging.INFO)

    def info(self, msg) -> None:
        logging.info('[{}] {}'.format(self.date_log, msg))
