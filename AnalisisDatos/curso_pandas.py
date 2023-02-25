import pandas as pd

# Curso sacado de esta pagina:
#https://deepnote.com/@anthonymanotoa/Tutorial-de-Pandas-en-Espanol-d21a300b-571d-4704-b81e-a7ba553b185a



# importar datos
df = pd.read_csv('AnalisisDatos/EjemplosCSV/curso_conceptos_pandas/Fullmetadata.csv')
# Importar con un indice
df = pd.read_csv('AnalisisDatos/EjemplosCSV/curso_conceptos_pandas/Fullmetadata.csv', index_col='player_id')

# Imprimimos dateframe
print(df)
print(df.shape)
print(df.describe())

# Imprimir unas columnas especificas:
print(df[["player_name","xG","npxG"]])

# df.head() → retorna las 5 primeras filas. También le puedes pasar un entero como parámetro y te devolverá esa cantidad de primeras filas.
# df.tail() → retorna las últimas 5 filas del dataset.
# df.sample() → es parecido a los 2 anteriores, pero este tomará muestras al azar del DataFrame.
# df.shape → retorna las filas y columnas que tiene el DataFrame.
# df.size → multiplica las filas y columnas y te da el total de datos del DataFrame.
# df.info() → este es genial, te da la cuenta de valores no nulos, el tipo de dato de cada columna (recuerda que solo puede haber un único tipo de dato por columna) y el uso de memoria. Cuando estés procesando los datos, será un gran aliado.
# df.describe() → te ayudará mucho con las primeras impresiones de los datos. Calcula algunas estadísticas descriptivas para cada columna.
    # Describe:
    #     count: el número de valores no vacíos.
    #     mean - El valor promedio (media).
    #     std - La desviación estándar.
    #     min - el valor mínimo.
    #     25% - El percentil 25%*.
    #     50% - El percentil 50%*.
    #     75% - El percentil 75%*.
    #     max - el valor máximo.

    #     *Significado de percentil: cuántos de los valores son menores que el percentil dado







# ORDENAR DATOS


print(df.sort_values('player_name',ascending=True))
# Ordenar varias columnas
print(df.sort_values(['red_cards','player_name'],ascending=[False,True]))



# Subconjuntos y filtros de datos

# Imprimimos los equipos unicos del dataframe
print(df["team_name"].unique())



# Filtrar filas:
# Hay tres formas:
    # df[df.player_name=='Aaron Connolly']
    # df[df['player_name']=='Aaron Connolly']
    # df.query('player_name == "Aaron Connolly"')
print(df.query('player_name == "Aaron Connolly"'))


# Consultas conjuntas:
    # Goles de Lionel Messi en 2014
leo = df[(df.player_name == 'Lionel Messi') & (df.year == 2014)]
cols = ['player_name', 'year', 'goals']
print(leo[cols])




#  Incluir varios datos en una condicion:
# .isin()
    # Goles de Ronaldo, Rubén Castro y Suárez en 2015
players = ['Cristiano Ronaldo', 'Rubén Castro', 'Luis Suárez']
top_players = df[(df.player_name.isin(players)) & (df.year == 2015)]
print(top_players[cols])

# condiciones con .loc
    # Es necesario que la condición que vayas a poner sea el indice:
df = pd.read_csv('AnalisisDatos/EjemplosCSV/curso_conceptos_pandas/Fullmetadata.csv', index_col='player_name')
    # Condicion: jugadores
players = ['Cristiano Ronaldo', 'Rubén Castro', 'Luis Suárez']
cols = ['year', 'goals']
    # .loc
top_players_cp = df.loc[players, cols]
print(top_players_cp.query('year==2015'))



    #     .sum() → suma todos los valores de una columna.
    #     .mean() → promedio de los valores de una columna.
    #     .max() → valor máximo de una columna.
    #     .min() → valor mínimo de una columna.
    #     .cumsum() → en cada fila va poniendo la suma acumulada de una columna.
    #     .cummax() → en cada fila va poniendo el valor máximo encontrado en orden de una columna.
    #     .value_counts(sort=True) → cuenta los distintos valores que existen en una columna (muy útil para contar categorías) y los ordena descendientemente.
    #     .drop_duplicates(subset='col_name') → elimina duplicados en una columna.

    # También es posible pasar funciones que nosotros mismos hayamos creado u otras funciones importadas de otras librerías. Para ello se usa .agg(function).


# Ejemplos:
# Maximo goleador en una temporada de todas las temporadas:
max_goals = df['goals'].max()
cols = ['goals', 'year', 'team_name']
print(df[df.goals == max_goals][cols])


# Porcentaje de disparos al arco que terminan en gol
total_shots = df['shots'].sum()
total_goals = df['goals'].sum()
print(round(total_goals / total_shots * 100, 2))






# Agrupar: groupby
#df.groupby()
# Top 10 jugadores que más goles han marcado
top_players = df.groupby('player_name')['goals'].sum()
print(top_players.sort_values(ascending=False).head(10))
# Alternativa para evitar que el group by sea el indice:
top_players = df.groupby('player_name',as_index=False)['goals'].sum()

# Top 5 equipos con más tarjetas rojas y amarillas
red_cards = df.groupby('team_name')[['red_cards', 'yellow_cards']].sum()
print(red_cards.sort_values('red_cards', ascending=False).head())

# Crear columnas:
df['goals_assists'] = df.goals + df.assists
best_players = df.groupby('player_name')['goals_assists'].sum()
print(best_players.sort_values(ascending=False).head())




