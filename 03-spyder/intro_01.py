# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 09:37:33 2018

@author: rprado
"""
import numpy as np
import pandas as pd
nombre = "Roberto"


arreglo_randomico_tres = np.random.rand(3)

arreglo_randomico_2D = np.random.rand(2,3)

# Pandas Serie

series_arreglo = pd.Series(arreglo_randomico_tres)

serie_arreglo_v2 = pd.Series(arreglo_randomico_tres, index=["Uno","Dos","Tres"])



series_arreglo[0]
serie_arreglo_v2[0]
serie_arreglo_v2["Uno"]


series_arreglo.index

serie_arreglo_v2.index

# Pandas Dataframes
data_frame = pd.DataFrame(arreglo_randomico_2D)

data_frame[0:][0]

data_frame.columns = ['Uno','Dos','Tres']

data_frame['Uno'][0]
