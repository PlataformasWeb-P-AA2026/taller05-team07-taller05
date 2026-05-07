# Explicación generación formato JSON
## Pasos iniciales
Para generar el formato JSON que va a tomar en cuenta todas las fuentes de información de la carpeta *data*
primero generamos un entorno virtual de Python para instalar ahí las librerias necesarias

```python
python -m venv .venv
```

Levantamos el entorno virtual y procedemos a instalar las librerías necesarias (archivo dentro de la carpeta 
**formato-json**)
```python
.venv\Scripts\activate
pip install -r requirements.txt
```

## Explicación de las librerias usadas
* **pandas**: Para el CSV. Para poder sacar la información del archivo CSV y al finalizar para poder guardar el archivo convertido usamos with open que nos sirve para trabajar de forma correcta un archivo en donde se garantiza el cierre del bloque.
* **beautifulsoup4**: Para poder sacar la informacion del documento HTML
* **pdfplumber**: Para poder extraer la informacion del documento PDF para la conversion lo hacemos por paginas usa la primera fila de la primera página como encabezado y se leen las demás filas, al momento de pasar la pagina y que no exista problemas de encabezado usamos zip() para combinar los headers con los valores de la fila.
* **request**: Para enviar la lista a la base de datos mediante un POST (API REST)

## COMANDOS DE PYTHON PARA EJECUTARLO EN CMD
Ejecutar cada uno de los siguientes comandos sucesivamente
### Comandos para generar los archivos JSON en base a la data
```python
py generar-json-csv.py
```

```python
py generar-json-html.py
```

```python
py generar-json-pdf.py
```

El siguiente comando se ejecuta después de haber realizado el proceso de conversión de los archivos data, para juntar toda la data en un solo JSON para su posterior importe a la base CouchDB

```python
py json-unificado.py
```

Luego de haber ejecutado los comandos, los archivos JSON resultantes se encuentran en la carpeta **data** dentro de la ruta **formato-json**

Finalmente, con el archivo JSON final preparado (mundial_2026.json) se ejecuta el siguiente comando para realizar la importación a la base CouchDB. La configuración del archivo para el comando POST a la base, se encuentra en el archivo **config.py**

```python
py importacion-couchdb.py
```

Con todos estos pasos realizados, podemos acceder a la interfaz web de CouchDB (Fauxton) para comprobar que los datos se encuentran ahí
