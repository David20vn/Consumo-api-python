import pandas as pd

def obtener_datos_kaggle(ruta_csv):
    # Coordina el flujo: desde leer el CSV hasta filtrar las columnas deseadas.
    dataframe =  pd.read_csv(ruta_csv)
    return dataframe
