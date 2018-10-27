# Suicidios anuales por cada 100.000 personas a nivel mundial

Información mundial clasificada en rankings de suicidios anuales por cada 100.000 personas.

Fuente: [ List of countries by suicide rate](https://en.wikipedia.org/wiki/List_of_countries_by_suicide_rate)

# Integrantes

Carlos Botero

# Archivos
`DatosSuicidioPais.py`:  Clase que representa la estructura de los datos por registro de suicidio.
`main.py`: Script para la ejecución de las tareas integrales de solicitud de URL, creación del DOM, generación de registros de la tabla de interés, producción de dataframe, y volcado a CSV.

# Librerías requeridas

## Requests

Permite la invocación de verbos HTTP.

Instalación:

    python –m pip install requests

## BeautifulSoup
Librería Python que permite el análisis de documentos HTML a través de una API intuitiva y eficiente.

Instalación:

    python –m pip install beautifulsoup

## Pandas

Librería Python para el análisis de datos. Permite la lectura y escritura de varios formatos de archivos estándar (i.e., CSV, XML, entre otros).

Instalación:

    python –m pip install pandas

# Ejecución

Desde una terminal de Linux, MacOS, o Windows ejecutar el comando:

    python main.py

**Nota**: Es necesario instalar las librerías definidas en el apartado anterior para la correcta ejecución del script.
