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

Proyecto-Analisis-DeliZone/
│
├── data/                   # Carpeta para los conjuntos de datos
│   ├── publicaciones.csv   # Datos sobre las publicaciones
│   ├── publico.csv      # Datos de los seguidores
│
├── notebooks/           # Jupyter Notebooks para el análisis
│   ├── analisis_publicaciones.ipynb
│   ├── analisis_publico.ipynb
│
├── scripts/             # Scripts de Python organizados
│   ├── limpieza_datos.py
│   ├── visualizaciones.py
│   ├── analisis.py
│
├── README.md            # Documentación del proyecto
├── requirements.txt     # Dependencias necesarias
