def mostrar_datos_ui(dataframe):
    # Diccionario con los nuevos nombres de las columnas
    columnas_nuevas = {
        "ciudad_municipio_nom": "Ciudad",
        "departamento_nom": "Departamento",
        "edad": "Edad",
        "fuente_tipo_contagio": "Tipo de Contagio",
        "tipo_recuperacion": "Recuperación",
        "estado": "Estado"
    }

    # Crear una lista con los nuevos nombres de columnas
    columnas = list(columnas_nuevas.values())

    # Renombrar columnas temporalmente para la impresión
    dataframe = dataframe.rename(columns=columnas_nuevas)

    # Encabezado con formato alineado
    encabezado = "{:<20} {:<15} {:<5} {:<16} {:<10} {:<10}".format(*columnas)
    print("=" * len(encabezado)) 
    print(encabezado)
    print("=" * len(encabezado))  # Línea separadora

    # Insertar cada fila del DataFrame con formato
    for _, row in dataframe.iterrows():
        fila = "{:<20} {:<15} {:<5} {:<16} {:<10} {:<10}".format(
            row["Ciudad"], row["Departamento"], row["Edad"], row["Tipo de Contagio"], row["Recuperación"], row["Estado"]
        )
        print(fila)