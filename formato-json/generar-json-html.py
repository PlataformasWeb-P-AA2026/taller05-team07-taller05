from bs4 import BeautifulSoup as bs
import json

"""
Script para generar el archivo JSON a partir de la fuente HTML
"""

def generar_json_desde_html():
    lista_jugadores = []

    # --- 1. PROCESAR HTML (EUROPA) ---
    print("Procesando HTML...")
    with open('../data/fuente_html_europa.html', 'r', encoding='utf-8') as f:
        soup = bs(f, 'html.parser')
        tabla = soup.find('table')
        # Extraer encabezados
        headers = [th.text.strip() for th in tabla.find_all('th')]
        # Extraer filas
        for tr in tabla.find_all('tr')[1:]:  # Omitimos la cabecera
            cells = tr.find_all('td')
            if cells:
                jugador = {headers[i]: cells[i].text.strip() for i in range(len(cells))}
                lista_jugadores.append(jugador)

    # --- ESTRUCTURA REQUERIDA POR COUCHDB ---
    # CouchDB necesita el formato { "docs": [ ... ] }
    resultado_couch = {
        "docs": lista_jugadores
    }

    # --- GUARDAR ARCHIVO ---
    with open('html_data.json', 'w', encoding='utf-8') as f:
        json.dump(resultado_couch, f, ensure_ascii=False, indent=4)

    print(f"Éxito: Se han procesado {len(lista_jugadores)} registros.")

if __name__ == "__main__":
    generar_json_desde_html()