from api.api import obtener_datos_api
from ui.ui import mostrar_datos_ui
from procesamiento_datos.procesamiento_datos import procesamiento_datos

def main():
    # Pedir al usuario el límite de registros
    limite_registros = int(input("Digite el límite de registros a extraer: "))

    # Pedir al usuario el nombre del departamento (opcional)
    nombre_departamento = input("Digite el nombre del departamento a filtrar: ")
    
    # Obtener los datos de la API usando la función de api_handler
    dataframe = obtener_datos_api(limite_registros, nombre_departamento)
    
    # Llamar a la UI para mostrar los datos
    mostrar_datos_ui(dataframe)
    
    mostrar_datos_ui(procesamiento_datos(dataframe))

main()