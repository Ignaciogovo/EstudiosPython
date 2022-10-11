from tkinter import Y
import matplotlib.pyplot as plt
import matplotlib.patheffects as pa
import pandas as pd

ValorClub = pd.read_csv(r'AnalisisDatos\EjemplosCSV\ValorEquipos.csv')
Mayor80 = pd.read_csv(r'AnalisisDatos\EjemplosCSV\Mayor80porClubflitrado.csv')
Menor80 = pd.read_csv(r'AnalisisDatos\EjemplosCSV\Menor80porClubflitrado.csv')
Mayor80Filtrado = pd.read_csv(r'AnalisisDatos\EjemplosCSV\Mayor80porClubflitradoVSmejor.csv')
Menor80Filtrado = pd.read_csv(r'AnalisisDatos\EjemplosCSV\Menor80porClubflitradoVSmejor.csv')
# print(archivo)
ganadosMy = Mayor80[(Mayor80.termino == 'ganados')]
empatadosMy = Mayor80[(Mayor80.termino == 'empatados')]
perdidosMy = Mayor80[(Mayor80.termino == 'perdidos')]
# Menor 80
ganadosMn = Menor80[(Menor80.termino == 'ganados')]
empatadosMn = Menor80[(Menor80.termino == 'empatados')]
perdidosMn = Menor80[(Menor80.termino == 'perdidos')]


ganadosMyfiltrado = Mayor80Filtrado[(Mayor80Filtrado.termino == 'ganados')]
empatadosMyfiltrado = Mayor80Filtrado[(Mayor80Filtrado.termino == 'empatados')]
perdidosMyfiltrado = Mayor80Filtrado[(Mayor80Filtrado.termino == 'perdidos')]
# Menor 80
ganadosMnfiltrado = Menor80Filtrado[(Menor80Filtrado.termino == 'ganados')]
empatadosMnfiltrado = Menor80Filtrado[(Menor80Filtrado.termino == 'empatados')]
perdidosMnfiltrado = Menor80Filtrado[(Menor80Filtrado.termino == 'perdidos')]


fig, ax = plt.subplots()
ax.set_title("Victorias con mas del 80% del aforo del estadio VS Victorias sin llegar al 80% del aforo del estadio")
ax.set_xlabel("Victorias")
ax.set_ylabel("club")
ax.scatter(ganadosMy['total'],ganadosMy['local'],label='Mas 80% del aforo')
ax.scatter(ganadosMn['total'],ganadosMn['local'], label='Menos 80% del aforo',color = 'tab:red')
plt.legend(shadow = False, prop = {"family":"Serif","size":15})
plt.show()
fig, ax = plt.subplots()
ax.set_title("Victorias con mas del 80% del aforo del estadio VS Victorias sin llegar al 80% del aforo del estadio")
ax.set_xlabel("Victorias")
ax.set_ylabel("club")
ax.scatter(ganadosMyfiltrado['total'],ganadosMyfiltrado['local'],label='Mas 80% del aforo VS equipos con valor superior a la AVG',color = 'tab:green')
ax.scatter(ganadosMnfiltrado['total'],ganadosMnfiltrado['local'], label='Menos 80% del aforo VS equipos con valor superior a la AVG',color = 'tab:orange')
plt.legend(shadow = False, prop = {"family":"Serif","size":15})
plt.show()

 


plt.title("Valor Total de los clubes")
plt.xlabel("Valor Total")
plt.ylabel("Club")
x = ValorClub['valor']
y = ValorClub['nombre']
plt.bar(x,y)
plt.show()
# Ejemplo:
# plt.title("Titulo")
# plt.xlabel("Titulo x")
# plt.ylabel("Titulo y")
# x = (4,8,13,17,20)
# y = (54, 67, 98, 78, 45)
# plt.scatter(x,y)
# x = [2,4,6,7,9,13,19,26,29,31,36,40,48,51,57,67,69,71,78,88]
# y = [54,72,43,2,8,98,109,5,35,28,48,83,94,84,73,11,464,75,200,54]
# plt.scatter(x,y)
# plt.show()