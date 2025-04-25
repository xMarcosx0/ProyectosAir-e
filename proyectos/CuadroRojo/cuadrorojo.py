import pandas as pd
import time 
import threading 

def mostrar_tiempo():
    inicio = time.time()
    while True:
        transcurrido = int(time.time() - inicio)
        minutos = transcurrido // 60
        segundos = transcurrido % 60
        print(f"/r ⏳ Tiempo Transcurrido: {minutos:02d}:{segundos:02d}", end="")
        time.sleep(1)

# Cargar el Documento de Excel 
df = pd.read_excel(r'C:\Users\apr.gestiondered6\Music\Resumen Estad Proy. Viab.xlsx')

# Ver las primeras filas
print(df.head)