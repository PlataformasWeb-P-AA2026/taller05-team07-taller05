# Explicación generación formato JSON

Para generar el formato JSON que va a tomar en cuenta todas las fuentes de información de la carpeta *data*
primero generamos un entorno virtual de Python para instalar ahí las librerias necesarias

```
python -m venv .venv
```

Levantamos el entorno virtual y procedemos a instalar las librerías necesarias
```
pip install -r requirements.txt
```



*   **pandas**: Para el CSV.
  * Para poder sacar la información del documento CSV usamos las librerias de pandas y json, para la conversion y uso de COUCHDB usamos "docs": lista_jugadores para poder hacer la conexion, al finalizar para poder guardar el archivo convertido usamos with open que nos sirve par atrabajar de forma correcta un archivo en donde se garantiza el cierre del bloque aun que puedan llegar a existir errores.
*   **beautifulsoup4**: Para el HTML.
  * Para poder sacar la informacion del documento HTML usamos las libreias de BeautifulSoup y json, para la conversion y uso de COUCHDB usamos "docs": lista_jugadores para poder hacer la conexion, al finalizar para poder guardar el archivo convertido usamos with open que nos sirve par atrabajar de forma correcta un archivo en donde se garantiza el cierre del bloque aun que puedan llegar a existir errores.
*   **pdfplumber**: Para extraer tablas de PDFs.
  * Para poder sacar la informacion del documento PDF usamos las libreias de pdfplumber y json, para la conversion lo hacemos por paginas usa la primera fila como encabezado y se leen las demas filas, al momento de pasar la pagina y que no exista problemas de encabezado usamos zip() para combinar los headers con los valores de la fila, finalmente para la conversion y uso de COUCHDB usamos "docs": lista_jugadores para poder hacer la conexion, al finalizar para poder guardar el archivo convertido usamos with open que nos sirve par atrabajar de forma correcta un archivo en donde se garantiza el cierre del bloque aun que puedan llegar a existir errores.
* **request**: Para enviar la lista a la base de datos mediante un POST

## COMANDOS DE PYTHON PARA EJECUTARLO EN CMD

py generar-json-csv.py
py generar-json-html.py
py generar-json-pdf.py

py json-unificado.py
py import-couchdb.py
