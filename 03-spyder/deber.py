# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 15:06:38 2018

@author: rprado
"""
import numpy as np
import pandas as pd

# Progresión geometrica
# 1/1 + 1/2 + 1/4 + 1/8...
n_array = np.arange(0, 5000, 1)
u = pd.Series(index = n_array)
u[0] = 1

progresion_geom = pd.Series(u[0]*(1/2)**(np.array(u.index) - u[0]), index = n_array)

# Datframes
estados = ['Activo', 'Inactivo']
nombres =  ['Juan', 'Ana', 'Pedro', 'Jose', 'Carlos', 'Angela']
apellidos = ['Ramirez', 'Gonzales', 'Fernandez', 'Alvarado', 'Garcia']
salarios = ['400', '750' , '1000', '1500']
cargos = ['Gerente', 'Administrador', 'Programador', 'Mantenimiento', 'Ventas']
ids = np.arange(0,1000)
columnas = ['estado','nombres','apellido','salarios','cargo']
rows = 1000
d = {
     'estado' : pd.Series(np.random.choice(estados,rows), index=ids),
     'nombre' : pd.Series(np.random.choice(nombres,rows), index=ids),
     'aoellido' : pd.Series(np.random.choice(apellidos,rows), index=ids),
     'salario' : pd.Series(np.random.choice(salarios,rows), index=ids),
     'cargo' : pd.Series(np.random.choice(cargos,rows), index=ids),
     }
empleados = pd.DataFrame(d)
print(empleados.where(empleados['cargo'] == 'Administrador'))

# Leer archivos
CSV_PATH = "D:\\dev\\epn\\python\\prado-imbacuan-roberto-carlos\\03-spyder\\data\\hygdata_v3.csv"
stars = pd.read_csv(CSV_PATH)
print(stars['dist'] * 3262)

print(stars['lum'].mean())
print(stars['lum'].min())
print(stars['lum'].max())


index_lum_normal = stars['lum'] == 1
print(stars[index_lum_normal])
index_lum_bajo = stars['lum'] < 1
print(stars[index_lum_bajo])


