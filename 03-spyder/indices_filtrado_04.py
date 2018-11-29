# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 08:47:14 2018

@author: rprado
"""

import pandas as  pd
import os

directorio_archivo = "D:\\dev\\epn\\python\\prado-imbacuan-roberto-carlos\\03-spyder\\data\\artwork_data.pickle"

df_guardado = pd.read_pickle(directorio_archivo)

artistas_df_duplicados = df_guardado["artist"]

artistas = pd.unique(artistas_df_duplicados)

print(len(artistas))

artistas_bacon_francis = df_guardado["artist"] == "Bacon, Francis"

artistas_bacon_francis.value_counts()

serie_artistas = df_guardado['artist'].value_counts()

serie_artistas['Bacon, Francis']

df_bacon_francis_2 = df_guardado[artistas_bacon_francis]
