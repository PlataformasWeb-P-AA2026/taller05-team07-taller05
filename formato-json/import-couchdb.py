"""
Script para importar el JSON unificado a CouchDB usando la API REST.
"""
import requests
import json

url = "http://admin:admin@localhost:5984/jugadores/_bulk_docs"
with open('mundial_data.json', 'rb') as f:
    data = json.load(f)

response = requests.post(url, json=data, headers={'Content-Type': 'application/json; charset=utf-8'})
print(response.status_code)