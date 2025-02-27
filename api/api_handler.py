import pandas as pd
from sodapy import Socrata

def get_api_data(limit, departamento):

    client = Socrata("www.datos.gov.co", None)
    
    results = client.get("gt2j-8ykr", limit=limit, departamento_nom=departamento)

    dataframe = pd.DataFrame.from_records(results)

    columnas_deseadas = [
        "ciudad_municipio_nom", 
        "departamento_nom", 
        "edad", 
        "fuente_tipo_contagio", 
        "tipo_recuperacion", 
        "estado"
    ]

    return dataframe[columnas_deseadas]
