#importar fastapi
from fastapi import FastAPI

app = FastAPI()

#peticion http
@app.get("/")
#crar una funcion llamada read_root
def read_root(): #la funcion puede ser asincrona = async def read_root()
    #retorna un valor
    return "Hello Fastapi"

@app.get("/url")
def url():
    return {"url-projecto":"https://github:Gamastore"}

#peticion GET: Son las que interpreta el explorador por defecto. Un get es obtener.

#Peticion POST: crear datos.
#Peticion PUT: para actualizar datos
#Peticion DELETE: eliminar datos.
