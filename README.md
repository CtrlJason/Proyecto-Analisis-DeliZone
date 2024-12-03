## Análisis de Datos en Redes Sociales - DeliZone

### Descripción del Proyecto

El objetivo de este proyecto es analizar y comprender los efectos de las interacciones de las publicaciones de las redes sociales en este caso Instagram de el sitio web DeliZone, utilizando Python para el procesamiento y análisis de datos. Las métricas de Instagram se utilizarán para mejorar la toma de decisiones estratégicas con el fin de tener mas publico y adquirir nuevos clientes.

### Datos Disponibles

El proyecto trabajará con los siguientes conjuntos de datos:
1. Publicaciones
- Métricas clave:
    Impresiones: Número total de veces que se mostró la publicación.
    Alcance: Número de usuarios únicos que vieron la publicación.
    Me gusta: Cantidad de interacciones en las publicaciones.
    Compartidos: Número de veces que se compartió la publicación.
    Guardados: Número de veces que los usuarios guardaron la publicación.
2. Publico
- Datos relacionados con la cuenta de Instagram:
    Total de seguidores: Número total de usuarios que siguen la cuenta.
    Distribución por sexo y edad: Segmentación demográfica de los seguidores.
    Ubicación geográfica: Principales ciudades y países donde se encuentran los seguidores.
3. Engagement Diario
- Información sobre las interacciones y el crecimiento de la cuenta:
    Seguidores adquiridos por fecha: Número de seguidores ganados día a día.
    Visitas al perfil por fecha: Total de visitas al perfil de Instagram por día.
    
### Estructura del Proyecto

```
Proyecto-Analisis-DeliZone/
│
├── api/
│   └── api.py         # Api de FastAPI app
│
├── data/
│   └── publicaciones.csv
│   └── publico.csv
│
├── etl/
│   └── etl_proceso.ipynb
│   └── etl_proceso.py
│
├── graficos/
│
├── ml/
│   └── arboles.py
│   └── bayes.py
│
├── viz/
│   └── visualizaciones.py
│
├── main.py 
│
├── README.md            # Documentación del proyecto
├── requirements.txt     # Dependencias necesarias
```

## Proceso ETL de las Publicaciones

### Descripción General

Este proceso ETL (Extract, Transform, Load) tiene como objetivo extraer los datos de un archivo CSV en este caso haremos el proceso para las publicaciones de la cuenta de Instagram de *DeliZone*

1. El proceso comienza obteniendo la ubicación del archivo CSV publicaciones.csv, que se encuentra en la carpeta data. Se utiliza la función os.path para construir la ruta de manera flexible, asegurando que funcione correctamente en diferentes entornos.

```
# Extracción de los datos

# Importamos las librerias necesarias
import pandas as pd
import os

# Cargamos los datos
base_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_path, '..', 'data', 'publicaciones.csv')
df_origin = pd.read_csv(data_path)
df = df_origin.copy()
```

2. Visualización de los Datos:
Se visualiza el DataFrame df para tener una vista preliminar de los datos.
Se utiliza df.info() para obtener información detallada sobre los tipos de datos de cada columna, lo que ayuda a identificar posibles inconsistencias o datos no esperados.

```
# Mostramos los datos de las publicaciones
df

# Tipos de dato por columna
df.info()
```

3. Eliminación de Columnas Innecesarias:
Se define una lista COLUMNS_TO_DROP con los nombres de las columnas que no se necesitan para el análisis posterior.
La función df.drop() elimina estas columnas del DataFrame, dejando solo las columnas que serán relevantes para el análisis.

```
# Eliminación de columnas que no necesitamos
COLUMNS_TO_DROP = [
'Identificador de la cuenta',
'Nombre de usuario de la cuenta',
'Nombre de la cuenta', 'Duración (segundos)',
'Comentario sobre los datos',
'Comentarios',
'Enlace permanente',
'Fecha',
]
df = df.drop(COLUMNS_TO_DROP, axis=1)

# Mostramos el resultado
df
```

4. Extraccion de Hashtags
- Se muestra una de las descripciones de las publicaciones para observar cómo están formateados los hashtags.
- Utilizando el método str.findall(r'#\w+'), se extraen todos los hashtags presentes en la columna Descripción. Esta expresión regular busca las palabras que comienzan con el símbolo # y contienen caracteres alfanuméricos.
- Los hashtags encontrados se almacenan en una nueva columna llamada Hashtags, lo que permite tener una lista de hashtags por cada publicación.

```
# Separación de Hashtags de la descripción
# Mostramos una de las descripciones para obtener la información completa
df.iloc[0]['Descripción']
```

```
# Ahora obtenemos únicamente los numerales de todas las descripciones
df['Descripción'].str.findall('#')
```

```
# Ahora obtenemos los Hashtags completos
df['Descripción'].str.findall(r'#\w+') # findall nos sirve para buscar partes de un string en específico
```

```
# Ahora creamos separamos los hashtags de la descripción
df['Hashtags'] = df['Descripción'].str.findall(r'#\w+')
```

```
# Mostramos los datos
df
```