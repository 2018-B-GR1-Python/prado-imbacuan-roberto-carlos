# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 07:30:55 2018

@author: rprado
"""

import pandas as pd
import os
import numpy as np

data_frame_guardado = pd.read_pickle('D:\\dev\\epn\\python\\prado-imbacuan-roberto-carlos\\03-spyder\\data\\artwork_data.pickle')

seccion_df = data_frame_guardado.iloc[49980:50019,:].copy()

# grupu by

df_agrupado = seccion_df.groupby('artist')

type(df_agrupado)


for name, data_frmae_agrupado_de_artista in df_agrupado:
    print(name)
    print(data_frmae_agrupado_de_artista)
    anio_minimo = data_frmae_agrupado_de_artista['acquisitionYear'].min()
    # width_max = data_frmae_agrupado_de_artista['width'].max()
    print("{}:{}".format(name,anio_minimo))


seccion_dos_df = data_frame_guardado.loc[11838:16441, 'medium']

def llenar_valores_vacios(series):
    print(series)
    valores_contados = series.value_counts()
    """if valores_contados.empty:
        return series
    print(valores_contados)
    # iterar y sumar
    sumatoria = 0
    numero_nans = 0
    for valor in series:
        if type(valor) == str:
            sumatoria = sumatoria + int(valor)
        if type(valor) == float:
            numero_nans = numero_nans + 1
    print(sumatoria)
    # dividir
    division = series.size - numero_nans
    valor_mas_utilizado = sumatoria / division
    print(valor_mas_utilizado)"""
    valores_mas_utilizados = valores_contados.index[0]
    nuevo_valor = series.fillna(valores_mas_utilizados)
    return nuevo_valor

def transformar_df_por_artista(df):
    arreglo_datafames_por_grupo = []
    agrupado_por_artista = df.groupby('artist')
    for nombre_artista, grupo in agrupado_por_artista:
        # print(grupo['height'])
        df_llenado = grupo.copy()
        df_llenado.loc[:, 'medium'] = llenar_valores_vacios(grupo['medium'])
        # print(df_llenado)
        arreglo_datafames_por_grupo.append(df_llenado)
    nuevo_df_lleno = pd.concat(arreglo_datafames_por_grupo)
    return nuevo_df_lleno
        
dataframe_transformado = transformar_df_por_artista(seccion_df)

df_agrupado_por_titulo = data_frame_guardado.groupby('title')
titulos_contados = df_agrupado_por_titulo.size().sort_values(ascending= True)

condicion = lambda x: len(x.index) > 1

dup_titles_df = df_agrupado_por_titulo.filter(condicion)

dup_titles_df.sort_values('title', inplace=True)




        
        