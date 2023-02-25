import pandas as pd



# importar datos
df = pd.read_csv('AnalisisDatos/EjemplosCSV/curso_conceptos_pandas/Fullmetadata.csv')

print(df)
# Ejercicios


# Encuentra la cantidad de goles totales hechos por cada posición.
df=df.groupby('position',as_index=False)['goals'].sum()
# df.columns.values[2] = 'total'
# print(df.sort_values('goals', ascending=False))







# importar datos
df = pd.read_csv('AnalisisDatos/EjemplosCSV/curso_conceptos_pandas/Fullmetadata.csv')

# Agrupar los datos por posición y calcular la suma y la media de los goles
grouped = df.groupby('position',as_index=False).agg({'goals': ['sum', 'mean']})

# Añadir el total de valores únicos por posición
# grouped['total_positions'] = df.groupby('position')['position'].sum()
# print(df.groupby('position')['position'].count())
# Renombrar las columnas para reflejar que contienen la suma y la media de los goles
# grouped.columns = ['position', 'goals_sum', 'goals_mean', 'total_positions']

# Ordenar por la columna de la media de los goles
# grouped.sort_values(by='goals_mean', ascending=False, inplace=True)

# Mostrar los resultados
# print(grouped)


# Agrupar los datos por posición y calcular la suma y la media de los goles
grouped = df.groupby('position',as_index=False).agg({'goals': ['sum', 'mean']})

# Añadir el total de valores únicos por posición
position=((df.groupby('position',as_index=False)['position'].count()))
grouped['total_positions'] = position

# Renombrar las columnas para reflejar que contienen la suma y la media de los goles
grouped.columns = ['position', 'goals_sum', 'goals_mean', 'total_positions']

# Ordenar por la columna de la media de los goles
grouped=grouped.sort_values(['goals_mean','total_positions'],ascending=[False,True])

# Mostrar los resultados
print(grouped)



    # Encuentra la cantidad de goles totales hechos por cada posición. Hecho
    # 1¿Cuál es el jugador que más tiempo ha jugado y cuál es la media de tiempo de todos los jugadores? Esta pregunta tiene truco porque hay muchos jugadores suplentes que no juegan casi nunca y van a sesgar los datos, ¿cómo podrías solucionar esto?
    # 2¿Qué posición es la que más tiempo juega? ¿Y la que menos?
    # 3¿Qué porcentaje de goles son hechos por penales? La columna npg significa: goles hechos SIN penales.
    # 4¿Qué porcentaje de goles son hechos con asistencias?
    # 5¿Cuál fue el equipo que más goles hizo cada año? ¿Salió campeón ese año?
    # 6¿Cuántos jugadores jugaron todos los años del dataset? ¿Qué porcentaje del total representan?





# importar datos
df = pd.read_csv('AnalisisDatos/EjemplosCSV/curso_conceptos_pandas/Fullmetadata.csv')

tiempo_jugadores=df.groupby(['player_name'],as_index=False)['time'].sum()

#1¿Cuál es el jugador que más tiempo ha jugado 
print("El jugador:"+str(tiempo_jugadores['player_name'].max())+" tiempo: "+str(tiempo_jugadores['time'].max()))

#1¿cuál es la media de tiempo de todos los jugadores? 
no_suplentes=df["games"]>0

tiempo_jugadores=(df[no_suplentes])['time'].mean()
# print("La media de los jugadores que han jugado al menos un partido ha sido de: "+ str(tiempo_jugadores))

 #2 ¿Qué posición es la que más tiempo juega? ¿Y la que menos?
grouped = df.groupby('position',as_index=False)["time"].sum()
    # Método uno:
    # Ordenamos  por valor de time:
grouped = grouped.sort_values(by='time', ascending=False)
    # Posición con más tiempo
position_most_time = grouped.iloc[0]['position']
    # Posición con menos tiempo
position_least_time = grouped.iloc[-1]['position']

    # Método dos:
    # Escoguemos el indice del indice de la posición con más tiempo
index_most_time = grouped['time'].idxmax()
    # Posición con más tiempo
position_most_time = grouped.loc[index_most_time, 'position']

    # Escoguemos el indice del indice de la posición con menos tiempo
index_least_time = grouped['time'].idxmin()
    # Posición con menos tiempo
position_least_time = grouped.loc[index_least_time, 'position']
    # Estos métodos idxmin y idxmax son útiles cuando deseas encontrar el índice de una fila con el mínimo o máximo valor en una columna en particular.

#  3¿Qué porcentaje de goles son hechos por penales? La columna npg significa: goles hechos SIN penales.
subconjunto=df[["player_name","goals","xG","npg"]]
subconjunto=subconjunto.sort_values("goals", ascending=False)
subconjunto["PenalesXgol"]=((subconjunto["goals"]-subconjunto["npg"])*100)/subconjunto["goals"]
prueba=subconjunto['PenalesXgol'].idxmax()
# Jugador con mayor porcentaje de goles a partir de penaltis
# print(subconjunto.loc[prueba])


# 4¿Qué porcentaje de goles son hechos con asistencias?
subconjunto=df[["player_name","goals","assists"]]
total_goles=subconjunto["goals"].sum()
total_assits=subconjunto["assists"].sum()
# % de goles con asistencias
print(total_assits*100/total_goles)





# 6¿Cuántos jugadores jugaron todos los años del dataset? ¿Qué porcentaje del total representan?
años=len(df["year"].unique())
grouped=df.groupby(['player_name'],as_index=False)["year"].count()
print(grouped)
e_y_p=(grouped.query('year =='+str(años)).count())["player_name"]
total_players=(grouped.count())["player_name"]
# Jugadores que han jugado todas las temporadas:
print("La cantidad de jugadores que han jugado todas las temporadas es de: "+str(e_y_p))
# % de jugadores que han jugado todas las temporadas:
print("El porcentaje de jugadores que han jugado todas las temporadas es de : "+str(round((e_y_p*100/total_players),2))+"%")