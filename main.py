from fastapi import FastAPI
from routes import archivo_router

app = FastAPI()

# Incluir el enrutador para las rutas de la API
app.include_router(archivo_router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)