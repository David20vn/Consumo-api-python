from api.api_handler import get_api_data
from ui.ui import display_ui

def main():
    # Pedir al usuario el límite de registros
    limite_registros = int(input("Digite el límite de registros a extraer: "))

    # Pedir al usuario el nombre del departamento (opcional)
    nombre_departamento = input("Digite el nombre del departamento a filtrar: ")
    
    # Obtener los datos de la API usando la función de api_handler
    dataframe = get_api_data(limite_registros, nombre_departamento)
    
    # Llamar a la UI para mostrar los datos
    display_ui(dataframe)

main()