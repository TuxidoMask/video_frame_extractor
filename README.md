# Extractor de Fotogramas de Vídeo

Herramienta desarrollada en **Python** para extraer automáticamente fotogramas de uno o varios vídeos a intervalos de tiempo configurables.

El programa está pensado como una **herramienta auxiliar para proyectos de visión artificial**, permitiendo convertir secuencias de vídeo en conjuntos de imágenes que posteriormente pueden utilizarse para tareas como la creación y preparación de conjuntos de datos (*datasets*).

La herramienta permite seleccionar múltiples vídeos, establecer el intervalo de extracción, seleccionar una carpeta de destino y generar automáticamente un reporte con información sobre el procesamiento realizado.

---

## Características

- Selección de uno o varios vídeos mediante una interfaz gráfica.
- Compatibilidad con formatos de vídeo comunes:
  - `.mp4`
  - `.avi`
  - `.mov`
  - `.mkv`
  - `.webm`
- Selección de la carpeta de destino mediante una interfaz gráfica.
- Intervalo de extracción configurable.
- Intervalo mínimo permitido de **0.5 segundos**.
- Valor predeterminado de **2 segundos**.
- Creación automática de una carpeta `frames`.
- Extracción de fotogramas en formato `.jpg`.
- Numeración consecutiva de los fotogramas.
- Procesamiento de múltiples vídeos en una misma ejecución.
- Evita sobrescribir los fotogramas obtenidos de vídeos anteriores durante la misma ejecución.
- Obtención de información de cada vídeo:
  - FPS
  - Número total de fotogramas
  - Duración
  - Número de fotogramas extraídos
- Generación automática de un reporte `.txt`.
- Visualización del reporte al finalizar el procesamiento.

---

## Propósito

La herramienta fue creada como apoyo para la **preparación de datos destinados a proyectos de visión artificial**.

En proyectos donde los datos de entrada se encuentran originalmente en formato de vídeo, puede ser necesario convertir estos vídeos en imágenes individuales para posteriormente realizar tareas como:

- Clasificación de imágenes.
- Detección de objetos.
- Etiquetado de imágenes.
- Creación de conjuntos de datos.
- Entrenamiento y evaluación de modelos de visión artificial.

Por ejemplo, en un proyecto de **detección de baches mediante visión artificial**, los vídeos obtenidos durante recorridos por carretera pueden procesarse para obtener imágenes individuales que posteriormente puedan ser revisadas, seleccionadas y etiquetadas para formar parte de un conjunto de datos.

> **Importante:** esta herramienta únicamente se encarga de la extracción y organización básica de los fotogramas. No realiza detección, clasificación ni etiquetado automático de baches.

---

## Requisitos

- **Python 3.13.13**
- OpenCV
- Tkinter

### Instalar OpenCV

La principal dependencia externa del proyecto es OpenCV:

```bash
pip install opencv-python
```

`tkinter` normalmente viene incluido con las instalaciones de Python para Windows. En otros sistemas operativos puede ser necesario instalarlo por separado.

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/USUARIO/REPOSITORIO.git
```

Reemplaza `USUARIO/REPOSITORIO` por la dirección correspondiente a este repositorio.

### 2. Acceder al directorio del proyecto

```bash
cd REPOSITORIO
```

### 3. Instalar las dependencias

```bash
pip install opencv-python
```

---

## Uso

Ejecuta el programa mediante:

```bash
python nombre_del_archivo.py
```

Al iniciar, el programa solicitará la información necesaria mediante ventanas gráficas.

### 1. Seleccionar los vídeos

Primero se mostrará una ventana para seleccionar uno o varios vídeos.

Se pueden seleccionar múltiples archivos para procesarlos durante una misma ejecución.

Formatos contemplados actualmente:

```text
.mp4
.avi
.mov
.mkv
.webm
```

### 2. Seleccionar la carpeta de destino

A continuación, se solicitará seleccionar la carpeta donde se almacenarán los resultados.

El programa creará automáticamente dentro de ella una carpeta denominada:

```text
frames/
```

### 3. Configurar el intervalo de extracción

Finalmente, se solicitará indicar cada cuántos segundos se desea extraer un fotograma.

El valor predeterminado es:

```text
2.0 segundos
```

El valor mínimo permitido es:

```text
0.5 segundos
```

Por ejemplo:

| Intervalo | Extracción aproximada |
|---:|---|
| `2.0 s` | 1 fotograma cada 2 segundos |
| `1.0 s` | 1 fotograma cada segundo |
| `0.5 s` | 1 fotograma cada medio segundo |

---

## Estructura de los resultados

Después de procesar los vídeos, la carpeta seleccionada tendrá una estructura similar a:

```text
Carpeta seleccionada/
│
├── frames/
│   ├── frame_0001.jpg
│   ├── frame_0002.jpg
│   ├── frame_0003.jpg
│   ├── frame_0004.jpg
│   ├── ...
│   └── frame_XXXX.jpg
│
└── reporte_frames_20260824_112030.txt
```

Los fotogramas se almacenan en formato **JPG**.

La numeración de los fotogramas es consecutiva durante toda la ejecución del programa. Por ejemplo, si el primer vídeo genera 150 imágenes:

```text
frame_0001.jpg
frame_0002.jpg
...
frame_0150.jpg
```

el siguiente vídeo comenzará con:

```text
frame_0151.jpg
frame_0152.jpg
...
```

Esto permite procesar varios vídeos sin sobrescribir los fotogramas obtenidos anteriormente durante la misma ejecución.

---

## Reporte de procesamiento

Al finalizar el procesamiento, se genera automáticamente un archivo de texto cuyo nombre incluye la fecha y hora de generación:

```text
reporte_frames_YYYYMMDD_HHMMSS.txt
```

El reporte contiene información detallada sobre el procesamiento realizado.

Entre los datos registrados se encuentran:

- Intervalo de extracción utilizado.
- Nombre de cada vídeo.
- FPS.
- Número total de fotogramas del vídeo.
- Duración.
- Número de fotogramas extraídos.
- Número total de vídeos procesados.
- Número total de fotogramas extraídos.
- Ruta donde fueron almacenados los fotogramas.

### Ejemplo

```text
=================================================================
                    RESULTADOS DEL PROCESAMIENTO
=================================================================

Intervalo de extracción: 2.00 segundos

-----------------------------------------------------------------
Vídeo 1
-----------------------------------------------------------------
Archivo: ejemplo.mp4
FPS: 60.77
Fotogramas: 18231
Duración: 300.02 segundos
Frames extraídos: 151

=================================================================
RESUMEN
=================================================================

Vídeos procesados: 1
Total de fotogramas: 151

=================================================================
RUTA DE GUARDADO
=================================================================

C:\Videos\frames
```

---

## Funcionamiento

De forma general, el proceso realizado por la herramienta es:

```text
Inicio
  │
  ▼
Seleccionar uno o varios vídeos
  │
  ▼
Seleccionar carpeta de destino
  │
  ▼
Definir intervalo de extracción
  │
  ▼
Crear carpeta "frames"
  │
  ▼
Procesar cada vídeo
  │
  ├── Obtener FPS
  ├── Obtener número de fotogramas
  ├── Calcular duración
  └── Extraer fotogramas
  │
  ▼
Generar información del procesamiento
  │
  ▼
Crear reporte TXT
  │
  ▼
Mostrar resultados
  │
  ▼
Fin
```

---

## Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| Python 3.13.13 | Lenguaje de programación |
| OpenCV | Lectura y procesamiento de vídeos |
| Tkinter | Interfaz gráfica |
| `os` | Gestión de archivos y directorios |
| `datetime` | Generación de marcas de tiempo para los reportes |

---

## Compatibilidad

El programa contempla actualmente los siguientes formatos:

- MP4
- AVI
- MOV
- MKV
- WEBM

Sin embargo, **la compatibilidad real puede depender del códec utilizado, la codificación del vídeo y de la versión de OpenCV instalada en el sistema**.

Por este motivo, que un archivo tenga una de las extensiones anteriores no garantiza necesariamente que pueda ser procesado correctamente.

Si un vídeo no puede ser abierto por OpenCV, el programa mostrará un mensaje indicando que no fue posible abrirlo y continuará con el siguiente vídeo seleccionado.

---

## Consideraciones y limitaciones

- El intervalo mínimo de extracción es de **0.5 segundos**.
- Los fotogramas se almacenan en formato `.jpg`.
- El programa depende de **OpenCV** para la lectura y procesamiento de los vídeos.
- La compatibilidad con un vídeo puede depender de su códec, codificación y características internas.
- El procesamiento de vídeos largos puede requerir una cantidad considerable de espacio de almacenamiento.
- La extracción mediante posiciones temporales puede presentar pequeñas diferencias respecto al tiempo exacto esperado dependiendo del vídeo y de su codificación.
- El programa está pensado principalmente como una herramienta auxiliar y no como un sistema completo de procesamiento o análisis de vídeo.
- El comportamiento puede variar entre diferentes versiones de Python, OpenCV y sistemas operativos.

---

## Ejemplo de aplicación en visión artificial

Una posible aplicación consiste en utilizar vídeos obtenidos durante recorridos por carretera para generar imágenes que posteriormente puedan formar parte de un conjunto de datos.

El flujo podría ser:

```text
Vídeo de carretera
       │
       ▼
Extractor de fotogramas
       │
       ▼
Imágenes individuales
       │
       ▼
Selección de imágenes útiles
       │
       ▼
Etiquetado
       │
       ▼
Dataset
       │
       ▼
Modelo de visión artificial
```

En un sistema destinado a la **detección de baches**, por ejemplo, los fotogramas extraídos podrían utilizarse como material inicial para identificar y etiquetar imágenes que contengan baches.

---

## Estado del proyecto

El proyecto se encuentra en desarrollo y puede recibir modificaciones o mejoras futuras.

Entre las posibles mejoras se encuentran:

- Mayor control sobre los parámetros de extracción.
- Mejor manejo de diferentes códecs y formatos de vídeo.
- Optimización del proceso de extracción.
- Incorporación de una interfaz gráfica más completa.
- Opciones adicionales para la organización de los fotogramas.
- Incorporación de más información al reporte de procesamiento.

---

## Licencia

Este repositorio no incluye actualmente una licencia específica.

Si el proyecto se distribuye públicamente, se recomienda definir una licencia de acuerdo con las necesidades del proyecto.