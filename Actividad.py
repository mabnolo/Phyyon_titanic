#!/usr/bin/env python
# coding: utf-8

# Manuel Alejandro Moreno Niño, grupo:202016908_69

# Fecha: 19/04/2023

# _

# _

# Importamos las librerías, adicional a ello generamos el matplotlib que sirve para mostrar las gráficas, el font para establecer el tamaño

# In[147]:


import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
font = {'size' : 12}
plt.rc('font', **font)


# Buscaremos en el directorio (prueba), ahora leeremos el excel con el comando pd.read, escribimimos delimiter que sirve para separar comas por columnas, ya hecho todos estos pasos procederemos a mostrar el encabezado

# In[148]:


os.chdir("C:\Prueba")
datos=pd.read_csv("titanic.csv", delimiter=",")
datos.head()


# Ahora vamos a corregir los siguientes datos para entender correctamente las gráficas

# In[149]:


datos['Survived']=datos['Survived'].map({
        0: 'No',
        1: 'Si'
    })
datos.head()


# Y datos de la embarcación

# In[150]:


datos['Embarked']=datos['Embarked'].map({
        'S': 'Southampton',
        'C': 'Cherbourg',
        'Q': 'Queenstown'
    })
datos.head()


# Ahora mostramos los datos generales con el siguiente comando, esto con el fin de saber que tipo de datos es

# In[151]:


datos.dtypes


# Describiremos los datos

# In[152]:


datos.describe()


# En este paso vamos hacer la estadística de la clase de usuarios que sobrevieron, para ello agrupamos (Groupby) y damos a las variables para generar la estadística

# In[153]:


datos.groupby(['Pclass', 'Survived'])['Survived'].count()
ax=sns.countplot(x='Pclass', hue='Survived', palette='rocket', data=datos)
ax.set(title='Supervivencia del ususario frente a la clase a la que pertenecia', 
       xlabel='Tipo de clase', ylabel='Total')
plt.show()


# Describiremos la cantidad de personas que sobrevivieron, pero en este caso el género indicará la cantidad de personas que se encuentran con vida o no (sex, survived, count)

# In[154]:


datos.groupby(['Sex', 'Survived'])['Survived'].count()


# Ahora lo describiremos a través de una gráfica

# In[155]:


ax=sns.countplot(x='Sex', hue='Survived', palette='rocket', data=datos)
ax.set(title='Total de pasajeros con respecto al sexo', 
       xlabel='Sexo', ylabel='Total')
plt.show()


# Ahora teniendo las dos variables de género y clase procedemos hacer una gráfica para determinar el procentaje de las personas que sobreviven

# In[156]:


ax=sns.catplot(x='Pclass', hue='Sex', col='Survived', palette='rocket', 
               data=datos, kind="count")
plt.show()


# Vamos a llamar datos de embarcación y personas que estuvieron ahí

# In[157]:


pd.crosstab(datos['Embarked'], datos['Survived'])


# Ahora vamos hacer una gráfica sobre la distribución de supervivencia según la embarcación

# In[158]:


ax=sns.countplot(x='Embarked', hue='Survived', data=datos)
ax.set(title='Distribucion de supervivencia', 
       xlabel='Lugar', ylabel='Total')
plt.show()


# Ahora agrupamos los datos de cabina  

# In[159]:


datos['Cabin'].groupby(datos['Cabin']).count()


# Sacaremos el dato de las personas menores de 18

# In[160]:


datos[datos['Age']<18]['Age'].count()


# Ahora sacaremos un intervalo entre la edad (-18) y la clase, adicional ello se hará la contabilidad en cada clase

# In[161]:


intervaloEdad1=datos[datos['Age']<18].pivot_table(values='Age', index='Pclass', aggfunc='count')
intervaloEdad1


# Ahora vamos a sacar el intervalo de las personas mayores entre 18 hasta los 50 

# In[162]:


intervaloEdad2=datos[(datos['Age']>=18) & (datos['Age']<=50)].pivot_table(values='Age', index='Pclass', aggfunc='count')
intervaloEdad2


# Por último sacaremos el dato de las personas mayores de 50

# In[163]:


intervaloEdad3=datos[datos['Age']>50].pivot_table(values='Age', index='Pclass', aggfunc='count')
intervaloEdad3


# Ya teniendo los datos, procedemos hacer la gráfica circular

# In[164]:


fig, ax=plt.subplots(1, 3, figsize = (16, 7))
ax[0].pie(intervaloEdad1['Age'].to_list(), labels=intervaloEdad1.index.to_list(), 
        autopct=funcPie(intervaloEdad1['Age'].to_list()), shadow=True, startangle=90)
ax[0].axis('equal')
ax[0].set_title('Menores a 18')  
ax[1].pie(intervaloEdad2['Age'].to_list(), labels=intervaloEdad2.index.to_list(),
        autopct=funcPie(intervaloEdad2['Age'].to_list()), shadow=True, startangle=90)
ax[1].axis('equal') 
ax[1].set_title('Mayores de 18 y menores o iguales a 50')  
ax[2].pie(intervaloEdad3['Age'].to_list(), labels=intervaloEdad3.index.to_list(),
        autopct=funcPie(intervaloEdad3['Age'].to_list()), shadow=True, startangle=90)
ax[2].axis('equal')  
ax[2].set_title('Edades mayores a 50') 
plt.legend()
plt.show()


# Ahora procedemos en sacar el dato general entre el año, género, la clase y si la persona sobrevivió 

# In[165]:


aux=datos[['Age', 'Sex', 'Pclass', 'Survived']].groupby('Age').filter(lambda x: (x['Age']).any())
aux


# Agrupamos (Groupby)

# In[166]:


aux=datos.groupby(['Pclass', 'Sex'])['Pclass'].count()
aux


# Ahora contaremos por el género sin tener en cuenta la clase

# In[167]:


aux[1]


# Ahora sacaremos el porcentaje de genero que estuvo en diferentes clases (1, 2 y 3)

# In[168]:


fig, ax=plt.subplots(1, 3, figsize = (16, 7))
ax[0].pie(aux[1].to_list(), labels=aux[1].index.to_list(), 
              autopct=funcPie(aux[1].to_list()), shadow=True, startangle=90)
ax[0].axis('equal')
ax[0].set_title('Total hombres y mujeres clase 1')
ax[1].pie(aux[2].to_list(), labels=aux[2].index.to_list(), 
              autopct=funcPie(aux[2].to_list()), shadow=True, startangle=90)
ax[1].axis('equal')
ax[1].set_title('Total hombres y mujeres clase 2')
ax[2].pie(aux[3].to_list(), labels=aux[3].index.to_list(), 
              autopct=funcPie(aux[3].to_list()), shadow=True, startangle=90)
ax[2].axis('equal')
ax[2].set_title('Total hombres y mujeres clase 3')
plt.legend()
plt.show()

