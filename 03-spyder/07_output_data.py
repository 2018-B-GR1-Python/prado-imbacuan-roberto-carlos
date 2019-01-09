# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 09:24:09 2018

@author: rprado
"""

import pandas as pd
import os
import numpy as np
import sqlite3


data_frame_guardado = pd.read_pickle('D:\\dev\\epn\\python\\prado-imbacuan-roberto-carlos\\03-spyder\\data\\artwork_data.pickle')

seccion_df = data_frame_guardado.iloc[50019:50100,:].copy()


with sqlite3.connect('mi_base_de_datos3.db') as conexion:
    seccion_df.to_sql('Artwork', conexion, if_exists='append')
    
        
seccion_df.to_json('artwork.json')
seccion_df.to_json('artwork-table.json', orient='table')
seccion_df.to_excel("basico.xlsx")


seccion_df.to_excel("basico_sin_indice.xlsx", index = False)    


seccion_df.to_excel("solo_algunas_columnas.xlsx", columns=["artist", "title", "year"])




writer = pd.ExcelWriter('multiples_hojas.xlsx', engine='xlsxwriter')


seccion_df.to_excel(writer, sheet_name = "Preview", index = False)

writer.save()

# Formateo condicional

artsitas_contados = data_frame_guardado['artist'].value_counts()

artsitas_contados.head()

writer = pd.ExcelWriter('colores.xlsx', engine='xlsxwriter')


artsitas_contados.to_excel(writer, sheet_name="Artist Counts") 

hoja = writer.sheets['Artist Counts']

cells_range = 'B2:B{}'.format(len(artsitas_contados.index))

hoja.conditional_format(cells_range, {
        'type':'2_color_scale',
        'min_value': '10',
        'min_type': 'percentile',
        'max_value': '99',
        'max_type': 'percentile'
        })   
writer.save()
    