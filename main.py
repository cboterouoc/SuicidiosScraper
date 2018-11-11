import requests
from bs4 import BeautifulSoup
import pandas as pd
from DatosSuicidioPais import DatosSuicidioPais
from urllib.request import urlretrieve
import os

# Representa la URL de trabajo:
URL = 'https://en.wikipedia.org/wiki/List_of_countries_by_suicide_rate'
# Estado OK de la solicitud:
HTTP_OK = 200


def main():
    """
    Inicializa el procesamiento de los datos siguiendo los siguientes pasos:
    1. Realizar solicitud sobre la URL para scryping
    2. Creación del DOM a partir de una instancia de BeautifulSoup
    3. Obtener la tabla objetivo (Suicides per 100,000 people per year (age standardized))
    4. Obtener los registros (filas) de la tabla
    5. Limpiar el nombre de país para remover caracteres especiales o paréntesis innecesarios
    6. Crear el data frame
    7. Crear el archivo CSV
    """
    respuesta = requests.get(URL)

    if respuesta.status_code == HTTP_OK:
        datos = respuesta.text

        soup = BeautifulSoup(datos, 'html.parser')

        tables = soup.find_all('table')

        suicidios = tables[2]
        contenido = suicidios.find('tbody')
        registros = contenido.find_all('tr')

        counter = 1

        datos_suicidos_paises = []

        for registro in registros:
            if counter == 1:
                counter += 2
                continue

            campos = registro.find_all('td')

            datos_suicidos_paises.append(crear_dato_suicidos_pais(campos))

        df = crear_dataframe(datos_suicidos_paises)

        df.to_csv('suicidos_a_nivel_mundial.csv', index=False)
    else:
        print('Problema al consultar el recurso Web')


def crear_dato_suicidos_pais(campos):
    """
    Crea un objeto de tipo DatosSuicidioPais
    :param campos: Lista de valores del contenido de los tags TD
    :return: Objeto DatosSuicidioPais
    """
    ranking = int(campos[0].text)
    pais = limpiar_pais(campos[1].text)
    descargar_bandera(campos[1].find('img')['src'], pais)
    ambos_sexos = float(campos[2].text)
    ranking_masculino = int(campos[3].text)
    masculino = float(campos[4].text)
    ranking_femenino = int(campos[5].text)
    femenino = float(campos[6].text)

    return DatosSuicidioPais(ranking, pais, ambos_sexos, ranking_masculino, masculino, ranking_femenino, femenino)


def limpiar_pais(pais):
    """
    Limpia el nombre del país removimiento paréntesis innecesarios y la letra 'b' al final del nombre.
    :param pais: Nombre del país
    :return: Nombre del pais limpio
    """
    pais = str(pais)

    if pais.find('(more info)') != -1:
        indice = pais.find('(more info)')
        pais = pais[0:indice]

    pais = pais.strip()

    if pais[-1] == 'b':
        pais = pais[0:-1]

    return pais


def descargar_bandera(img_url, pais):
    """
    Descarga las banderas de cada país.
    :return:
    """
    img_url = 'https:{}'.format(img_url)
    urlretrieve(img_url, 'banderas/{}.png'.format(pais))


def crear_dataframe(datos_suicidos_paises):
    """
    Crea el dataframe con los datos de todos los registros de suicidios por país.
    :param datos_suicidos_paises: Lista de registros de suicidos por pais
    :return: Dataframe con los datos de todos los registros de suicidios por país.
    """
    columnas = ['ranking', 'pais', 'ambos_sexo', 'ranking_masculino', 'masculino', 'ranking_femenino', 'femino']
    df = pd.DataFrame(columns=columnas)

    for i in range(len(datos_suicidos_paises)):
        df.loc[i] = [datos_suicidos_paises[i].ranking, datos_suicidos_paises[i].pais, datos_suicidos_paises[i].ambos_sexos, datos_suicidos_paises[i].ranking_masculino, datos_suicidos_paises[i].masculino, datos_suicidos_paises[i].ranking_femenino, datos_suicidos_paises[i].femenino]

    return df


if __name__ == '__main__':
    """
    Inicializa la ejecución de la aplicación.
    """
    main()


