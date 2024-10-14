import PyPDF2
import pandas as pd
import numpy as np

# Función para extraer texto de archivos PDF
def extraer_texto_pdf(ruta_archivo):
    try:
        with open(ruta_archivo, 'rb') as archivo:
            pdf = PyPDF2.PdfReader(archivo)
            texto = ''
            for pagina in pdf.pages:
                texto += pagina.extract_text()
        return texto
    except Exception as e:
        print(f'Error al extraer texto de {ruta_archivo}: {e}')
        return None

# Función para leer archivos de hoja de cálculo (Excel, CSV, ODS, XLS)
def leer_hoja_calculo(ruta_archivo):
    try:
        if ruta_archivo.endswith('.csv'):
            df = pd.read_csv(ruta_archivo)
        elif ruta_archivo.endswith('.xlsx'):
            df = pd.read_excel(ruta_archivo)
        elif ruta_archivo.endswith('.ods'):
            df = pd.read_excel(ruta_archivo, engine='odf')
        elif ruta_archivo.endswith('.xls'):
            df = pd.read_excel(ruta_archivo, engine='xlrd')
        else:
            raise ValueError(f'Formato de archivo no soportado: {ruta_archivo}')
        
        # Reemplazar valores NaN y inf por None
        df = df.replace({np.nan: None, np.inf: None, -np.inf: None})
        return df
    except Exception as e:
        print(f'Error al leer {ruta_archivo}: {e}')
        return None

# Función para leer archivos de texto
def leer_archivo_texto(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            texto = archivo.read()
        return texto
    except Exception as e:
        print(f'Error al leer {ruta_archivo}: {e}')
        return None