import pandas as pd

def inspeccionar_datos(df):
    # Realiza una inspección general del DataFrame.
    print("Número de filas:", df.shape[0])
    print("Número de columnas:", df.shape[1])
    print("Nombres de columnas:", df.columns.values.tolist())
    print("Tipos de datos en columnas:\n", df.dtypes)

def identificar_valores_nulos(df):
    # Identifica columnas con valores nulos y muestra ejemplos.
    cols_nulos = df.columns[df.isnull().any()].tolist()
    print("Columnas con valores nulos:", cols_nulos)
    filas_con_nulos = df[df.isnull().any(axis=1)]
    print("Número de filas con valores nulos:", filas_con_nulos.shape[0])
    print("Ejemplos de índices con datos nulos:", filas_con_nulos.index.tolist()[:5])

def calcular_estadisticas(df):
    # Calcula y muestra estadísticas descriptivas.
    print("Información general:")
    df.info()
    print("Estadísticas descriptivas:")
    print(df.describe())

def limpiar_datos(df):
    # Elimina filas con valores nulos en la columna 'Outcome'
    print("Eliminando filas con valores nulos en 'Outcome'...")
    df_limpio = df.dropna(subset=['Outcome'])
    print("Forma del DataFrame después de limpiar:", df_limpio.shape)
    return df_limpio

def procesamiento_datos(df):
    inspeccionar_datos(df)
    identificar_valores_nulos(df)
    calcular_estadisticas(df)
    return limpiar_datos(df)
