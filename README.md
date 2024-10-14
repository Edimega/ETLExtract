# ETL Extract Application

Esta aplicación es un servicio ETL (Extract, Transform, Load) que permite extraer texto de archivos PDF, hojas de cálculo (Excel, CSV) y archivos de texto. La aplicación expone una API utilizando FastAPI y se puede ejecutar en un contenedor Docker.

## Características

- **PDF**: Extrae texto de archivos PDF utilizando PyPDF2 o pdfplumber.
- **Hojas de Cálculo**: Lee archivos Excel y CSV utilizando pandas y openpyxl.
- **Archivos de Texto**: Lee archivos de texto directamente.

## Instalación

### Requisitos

- Docker
- Docker Compose

### Pasos

1. Clona el repositorio:
    ```sh
    git clone https://github.com/Edimega/ETLExtract
    cd ETLExtract
    ```

2. Construye y levanta los contenedores con Docker Compose:
    ```sh
    docker-compose up --build
    ```

3. La aplicación estará disponible en `http://localhost:8000`.

## Endpoints

### 1. Extraer Texto de PDF
**Endpoint:** `/extraer-texto-pdf/`  
**Método:** `POST`  
**Tipo de Contenido:** `multipart/form-data`  
**Parámetros:**  
- `file`: Archivo PDF a subir.

```sh
curl -X POST "http://localhost:8000/extraer-texto-pdf/" -F "file=@ruta/al/archivo.pdf"
```

### 2. Leer Hoja de Cálculo (Excel, ods, CSV)
**Endpoint:** `/leer-hoja-calculo/`  
**Método:** `POST`  
**Tipo de Contenido:** `multipart/form-data`  
**Parámetros:**  
- `file`: Archivo Excel o CSV a subir.

```sh
curl -X POST "http://localhost:8000/leer-hoja-calculo/" -F "file=@ruta/al/archivo.xlsx"
```

### 3. Leer Archivo de Texto
**Endpoint:** `/leer-archivo-texto/`  
**Método:** `POST`  
**Tipo de Contenido:** `multipart/form-data`  
**Parámetros:**  
- `file`: Archivo de texto a subir.

```sh
curl -X POST "http://localhost:8000/leer-archivo-texto/" -F "file=@ruta/al/archivo.txt"
```

## Contribución
Si deseas contribuir a este proyecto, por favor abre un issue o envía un pull request.
