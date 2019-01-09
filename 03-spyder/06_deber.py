# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 14:13:46 2018

@author: rprado
"""

import pandas as pd
import os
import numpy as np


# Encuesta Nacional de Condiciones de Vida - INEC
data = pd.read_csv('D:\\dev\\epn\\python\\prado-imbacuan-roberto-carlos\\03-spyder\\data\\01ecv6rvivienda.csv', sep=".", decimal=",", encoding="ansi", low_memory=False)


# 1) Conteo por tipo de vivienda a nivel Nacional
data.rename(columns={'VI07': 'tipo_de_vivienda'}, inplace=True)

grupo_por_tipo_vivienda = data.groupby(['tipo_de_vivienda'])

for name, grupo in grupo_por_tipo_vivienda:
    print(f"{name} - {len(grupo)}")