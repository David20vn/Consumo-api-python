from api.api import obtener_datos_kaggle
from ui.ui import mostrar_datos_ui
from procesamiento_datos.procesamiento_datos import procesamiento_datos

def main():
    # Pedir al usuario el límite de registros a visualizar
    limite_registros = int(input("Digite el límite de registros a extraer: "))

    # Definir la ruta del archivo CSV (se encuentra en la misma carpeta que main.py)
    ruta_csv = "diabetes.csv"

    # Obtener el DataFrame a partir del CSV y filtrar las columnas deseadas
    dataframe = obtener_datos_kaggle(ruta_csv)
    
    # Limitar el DataFrame al número de registros especificado
    dataframe = dataframe.head(limite_registros)
    
    # Mostrar datos originales
    print("\nDatos originales:")
    mostrar_datos_ui(dataframe)
    
    # Procesar los datos (inspección, estadísticas y limpieza)
    dataframe_procesado = procesamiento_datos(dataframe)
    
    # Limitar nuevamente el DataFrame procesado a la cantidad de registros solicitada
    dataframe_procesado = dataframe_procesado.head(limite_registros)
    
    print("\nDatos procesados:")
    mostrar_datos_ui(dataframe_procesado)

if __name__ == '__main__':
    main()
