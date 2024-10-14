import os
from fastapi import APIRouter, UploadFile, File, HTTPException
from utils import extraer_texto_pdf, leer_hoja_calculo, leer_archivo_texto

# Crear el enrutador
archivo_router = APIRouter()

# Asegurarse de que la carpeta 'data' exista
if not os.path.exists('data'):
    os.makedirs('data')

@archivo_router.post("/extraer-texto-pdf/")
async def extraer_texto_pdf_endpoint(file: UploadFile = File(...)):
    file_path = os.path.join('data', file.filename)
    try:
        contenido = await file.read()
        with open(file_path, 'wb') as f:
            f.write(contenido)
        texto = extraer_texto_pdf(file_path)
        if texto is None:
            raise HTTPException(status_code=500, detail="Error al extraer texto del PDF")
        return {"texto": texto}
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

@archivo_router.post("/leer-hoja-calculo/")
async def leer_hoja_calculo_endpoint(file: UploadFile = File(...)):
    file_path = os.path.join('data', file.filename)
    try:
        contenido = await file.read()
        with open(file_path, 'wb') as f:
            f.write(contenido)
        df = leer_hoja_calculo(file_path)
        if df is None:
            raise HTTPException(status_code=500, detail="Error al leer la hoja de cálculo")
        return {"data": df.to_dict(orient='records')}
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

@archivo_router.post("/leer-archivo-texto/")
async def leer_archivo_texto_endpoint(file: UploadFile = File(...)):
    file_path = os.path.join('data', file.filename)
    try:
        contenido = await file.read()
        with open(file_path, 'wb') as f:
            f.write(contenido)
        texto = leer_archivo_texto(file_path)
        if texto is None:
            raise HTTPException(status_code=500, detail="Error al leer el archivo de texto")
        return {"texto": texto}
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)