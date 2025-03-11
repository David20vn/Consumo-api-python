import pandas as pd
from sodapy import Socrata

def conectar_api():
    #Establece la conexión con la API de datos abiertos.
    return Socrata("www.datos.gov.co", None)

def obtener_datos(client, limit, departamento):
    #Obtiene los datos de la API según el límite y el departamento especificado.
    return client.get("gt2j-8ykr", limit=limit, departamento_nom=departamento)

def convertir_a_dataframe(results):
    #Convierte los datos obtenidos en un DataFrame de Pandas.
    return pd.DataFrame.from_records(results)

def filtrar_columnas(dataframe):
    #Filtra las columnas deseadas del DataFrame.
    columnas_deseadas = [
        "ciudad_municipio_nom", 
        "departamento_nom", 
        "edad", 
        "fuente_tipo_contagio", 
        "tipo_recuperacion", 
        "estado"
    ]
    return dataframe[columnas_deseadas]

def obtener_datos_api(limit, departamento):
    #Función principal que coordina el flujo de datos desde la API hasta el DataFrame final.
    client = conectar_api()
    results = obtener_datos(client, limit, departamento)
    dataframe = convertir_a_dataframe(results)
    return filtrar_columnas(dataframe)
