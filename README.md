#TPO - Gestión de Perfiles de Instagram

## Descripción
El sistema está compuesto por cuatro archivos principales:

### 'main.py'
Archivo principal que gestiona la interfaz de usuario y las operaciones del sistema.
### 'crud.py'
Contiene funciones CRUD para gestionar usuarios y hashtags.
### 'metricas.py'
Define funciones para la validación de datos y el manejo de métricas.
### 'validez.py'
Proporciona funciones para validar correos electrónicos.

## Requisitos
Para ejecutar este proyecto, asegúrate de tener instaladas las siguientes dependencias:
- 'instaloader': Para la carga de datos desde Instagram.
- 'json': Para el manejo de datos en formato JSON (incluido en la biblioteca estándar de Python)

Puedes instalar las dependencias necesarias usando 'pip':

''' bash
pip install instaloader





## Cambios Futuro

### Mejoras en la Recolección de Métricas

1. **Porcentaje de Engagement Más Asertado**: Se planea mejorar la recolección de datos en `metricas.py` para calcular el porcentaje de engagement. Esto incluirá la recolección de likes por publicación individual para obtener una métrica más precisa del engagement en lugar de sumar los likes totales.

2. **Análisis de Hashtags**: Se implementará una función para analizar los hashtags más utilizados entre todos los usuarios. Esto permitirá identificar qué hashtags son más frecuentes y pueden proporcionar información valiosa sobre tendencias y popularidad.

3. **Seguimiento de Compartidos**: Se agregará una funcionalidad para contar cuántas personas han compartido las publicaciones de cada usuario. Esta métrica ayudará a entender mejor el alcance y la viralidad de las publicaciones.

### Mejoras en la Funcionalidad de CRUD

1. **Agregar Correos Manualmente**: En `crud.py`, se añadirá una nueva función para permitir la adición manual de correos electrónicos a los perfiles de usuario. Esta funcionalidad será útil para completar la información de contacto y gestionar los datos de los usuarios de manera más eficaz.

### Visualización de Datos

1. **Generación de Gráficas**: En el futuro, se planea implementar gráficos para la visualización de datos usando la biblioteca `matplotlib`. Esto permitirá crear gráficos visuales para mejor análisis y presentación de las métricas recolectadas, como la distribución de likes, el uso de hashtags, y las estadísticas de compartidos.




1. Falta Ordenamiento de matrices
2. Poner limite a la cantidad de caracteres de los items de las matrices
