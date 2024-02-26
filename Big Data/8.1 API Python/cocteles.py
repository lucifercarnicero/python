import requests
import json
import csv
import os

directorio_actual = os.path.dirname(os.path.abspath(__file__))

def obtener_categorias():
    url = "https://www.thecocktaildb.com/api/json/v1/1/list.php?c=list"
    response = requests.get(url)
    if response.status_code == 200:
        categorias = response.json()['drinks']
        return [categoria['strCategory'] for categoria in categorias]
    else:
        raise Exception("Error al obtener las categorías")

def obtener_cocteles_por_categoria(categoria):
    url = f"https://www.thecocktaildb.com/api/json/v1/1/filter.php?c={categoria.replace(' ', '_')}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['drinks']
    else:
        raise Exception(f"Error al obtener cócteles para la categoría {categoria}")

def generar_json_por_categoria(categorias, directorio_salida):
    conteo_cocteles = {}
    for categoria in categorias:
        cocteles = obtener_cocteles_por_categoria(categoria)
        conteo_cocteles[categoria] = len(cocteles)
        nombre_archivo_json = f"{categoria.replace('/', '_')}.json"
        ruta_completa_json = os.path.join(directorio_salida, nombre_archivo_json)
        with open(ruta_completa_json, 'w') as archivo_json:
            json.dump(cocteles, archivo_json)
    return conteo_cocteles

def generar_csv_con_todos_los_cocteles(categorias, directorio_salida):
    ruta_completa_csv = os.path.join(directorio_salida, 'cocteles.csv')
    with open(ruta_completa_csv, 'w', newline='', encoding='utf-8') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(['Id', 'Nombre', 'Imagen', 'Categoría'])

        for categoria in categorias:
            cocteles = obtener_cocteles_por_categoria(categoria)
            for coctel in cocteles:
                escritor_csv.writerow([coctel['idDrink'], coctel['strDrink'], coctel['strDrinkThumb'], categoria])

def main():
    directorio_salida = directorio_actual  # Usar el directorio actual del script

    try:
        categorias = obtener_categorias()
        conteo_cocteles = generar_json_por_categoria(categorias, directorio_salida)
        for categoria, cantidad in conteo_cocteles.items():
            print(f"Categoría '{categoria}': {cantidad} cócteles")
        generar_csv_con_todos_los_cocteles(categorias, directorio_salida)
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
