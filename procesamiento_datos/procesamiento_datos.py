import pandas as pd

def inspeccionar_datos(df):
    #Realiza una inspección general del DataFrame.
    print("Número de filas::", df.shape[0])
    print("Número de columnas::", df.shape[1])
    print("Nombres de columnas::", df.columns.values.tolist())
    print("Tipos de datos en columnas::\n", df.dtypes)


def identificar_valores_nulos(df):
    #Identifica valores nulos en el DataFrame.
    print("Columns with Missing Values::", df.columns[df.isnull().any()].tolist())
    print("Number of rows with Missing Values::", len(df[df.isnull().any(axis=1)]))
    print("Sample Indices with missing data::", df[df.isnull().any(axis=1)].index.tolist()[0:5])


def calcular_estadisticas(df):
    #Calcula estadísticas descriptivas de las columnas numéricas.
    print("General Stats::")
    print(df.info())
    print("Summary Stats::" )
    print(df.describe())

def limpiar_datos(df):
    #Elimina filas con valores nulos en la columna 'tipo_recuperacion'.
    print("Eliminar filas con fechas faltantes::")
    df_dropped = df.dropna(subset=['tipo_recuperacion'])
    print("Forma del DataFrame::", df_dropped.shape)
    return df_dropped

def procesamiento_datos(df):
    inspeccionar_datos(df)
    identificar_valores_nulos(df)
    calcular_estadisticas(df)
    return limpiar_datos(df)