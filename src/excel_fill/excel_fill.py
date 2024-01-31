from openpyxl import load_workbook


def escribir_celda_excel(ruta_excel, hoja, celda, valor):
    # Cargamos el libro de Excel existente
    wb = load_workbook(filename=ruta_excel)

    # Seleccionamos la hoja en la que queremos trabajar
    hoja = wb[hoja]

    # Asignamos los valores a las celdas específicas
    hoja[celda] = valor

    # Guardamos los cambios en el libro de Excel
    wb.save(filename=ruta_excel)


if __name__ == '__main__':
    filename = r'C:\Harold_DS\2024-01\02-informe_diario\02-informe_diario\src\excel_fill\test.xlsx'
    hoja = '22-09-2021'
    celda = 'H3'
    valor = 'Pared oeste'
    escribir_celda_excel(filename, hoja, celda, valor)
