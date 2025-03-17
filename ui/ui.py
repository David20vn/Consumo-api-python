def mostrar_datos_ui(dataframe):
    # Diccionario con los nuevos nombres para mayor claridad en la visualización
    columnas_nuevas = {
        "Pregnancies": "Embarazos",
        "Glucose": "Glucosa",
        "BloodPressure": "Presión",
        "SkinThickness": "Espesor Piel",
        "Insulin": "Insulina",
        "BMI": "IMC",
        "DiabetesPedigreeFunction": "Pedigree",
        "Age": "Edad",
        "Outcome": "Resultado"
    }

    # Renombrar las columnas del DataFrame para la impresión
    dataframe = dataframe.rename(columns=columnas_nuevas)

    # Crear una lista de columnas (los nuevos nombres) para el encabezado
    columnas = list(columnas_nuevas.values())

    # Construir el encabezado con un formato fijo (ancho 15 para cada columna)
    encabezado = "".join(["{:<15}".format(col) for col in columnas])
    print("=" * len(encabezado))
    print(encabezado)
    print("=" * len(encabezado))
    
    # Imprimir cada fila del DataFrame formateada
    for _, row in dataframe.iterrows():
        fila = "".join(["{:<15}".format(row[col]) for col in columnas])
        print(fila)
