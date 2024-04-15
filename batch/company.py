# -*- coding: utf-8 -*-

import os
import sys
import json
import pandas as pd

sys.path.append(os.path.abspath(os.getcwd()))

# set local data
STORAGE = os.path.join('storage')
FILENAME = 'tb_estabelecimento.1.1.0.csv'


def init():
    # read data from local
    usecols = ['CNPJ', 'NOME_FANTASIA', 'ATIVIDADE_PRINCIPAL', 'CEP']
    df = pd.read_csv(f'{STORAGE}/{FILENAME}', sep=';',
                     dtype=str, usecols=usecols)

    print(df.to_json(orient='records'))


if __name__ == '__main__':
    init()
