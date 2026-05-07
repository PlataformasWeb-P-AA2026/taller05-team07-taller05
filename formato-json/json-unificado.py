"""
Script para unificar los archivos JSON en un solo JSON con la estructura para CouchDB
"""
import json
import os

def unificar_jsons(directorio):
    unificado = []
    
    for filename in os.listdir(directorio):
        if filename.endswith('.json'):
            with open(os.path.join(directorio, filename), 'r', encoding='utf-8') as f:
                data = json.load(f)
                # Suponiendo que tus archivos de origen tienen la estructura {"docs": [...]}
                if "docs" in data:
                    # Usamos extend() para añadir los elementos de la lista, no la lista en sí
                    unificado.extend(data["docs"])
                elif isinstance(data, list):
                    # Por si algún archivo original era solo una lista pura
                    unificado.extend(data)
    
    # Envolvemos toda la lista fusionada en la estructura final de CouchDB
    resultado_final = {
        "docs": unificado
    }
    return resultado_final

if __name__ == "__main__":
    directorio = './data'  # Cambia esto al directorio donde están tus JSONs
    resultado = unificar_jsons(directorio)
    
    with open('./data/mundial_2026.json', 'w', encoding='utf-8') as f:
        json.dump(resultado, f, ensure_ascii=False, indent=4)
    
    print("JSON unificado creado como 'mundial_2026.json'")