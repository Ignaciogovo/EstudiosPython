from tkinter import Y
import matplotlib.pyplot as plt
import matplotlib.patheffects as pa
import pandas as pd


Mayor80 = pd.read_csv(r'AnalisisDatos\EjemplosCSV\Mayor80porClubflitrado.csv')
Menor80 = pd.read_csv(r'AnalisisDatos\EjemplosCSV\Menor80porClubflitrado.csv')
# print(archivo)
ganadosMy = Mayor80[(Mayor80.termino == 'ganados')]
empatadosMy = Mayor80[(Mayor80.termino == 'empatados')]
perdidosMy = Mayor80[(Mayor80.termino == 'perdidos')]
# Menor 80
ganadosMn = Menor80[(Menor80.termino == 'ganados')]
empatadosMn = Menor80[(Menor80.termino == 'empatados')]
perdidosMn = Menor80[(Menor80.termino == 'perdidos')]

plt.title("Ganados mayor 80 VS ganados menor 80")
plt.xlabel("Victorias")
plt.ylabel("club")
plt.scatter(ganadosMy['total'],ganadosMy['local'])
plt.scatter(ganadosMn['total'],ganadosMn['local'])
# ax.plot(ganadosMn['local'],label = 'prueba', path_effects = [pa.SimpleLineShadow(),pa.Normal()])
plt.show()
