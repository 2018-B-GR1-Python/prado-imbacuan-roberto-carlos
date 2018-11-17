# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 09:56:35 2018

@author: rprado
"""

import pandas as pd
import os

CSV_PATH = "D:\\dev\\epn\\python\\prado-imbacuan-roberto-carlos\\03-spyder\\data\\artwork_data.csv"

# Se puede leer:
# Archivos de texto
# Binary files
# Realtional Databases

data_frame_artwork = pd.read_csv(CSV_PATH, nrows=5, index_col='id',usecols=['id','artist', 'title'])

# Serialización del Dataframe
CSV_PATH_GUARDADO = "D:\\dev\\epn\\python\\prado-imbacuan-roberto-carlos\\03-spyder\\data\\artwork_data.pickle"

data_frame_artwork.to_pickle(CSV_PATH_GUARDADO)
