from data.database import database
from typing import Annotated

from data.dao.dao_artisatas import DaoArtistas

from data.modelo.menu import Menu

from typing import Union

from fastapi import FastAPI, Request,Form



from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="./static"), name="static")


templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse(
        request= request, name="index_steven.html"
    )

@app.get("/Linkin Park")
def plantilla(request: Request):
    return templates.TemplateResponse(
        request= request, name="Linkin_Park.html"
    )

@app.get("/Duki")
def plantilla(request: Request):
    return templates.TemplateResponse(
        request= request, name="Duki.html"
    )

@app.get("/Quevedo")
def plantilla(request: Request):
    return templates.TemplateResponse(
        request= request, name="Quevedo.html"
    )

@app.get("/Milo J")
def plantilla(request: Request):
    return templates.TemplateResponse(
        request= request, name="Milo_J.html"
    )

@app.get("/Ramma")
def plantilla(request: Request):
    return templates.TemplateResponse(
        request= request, name="Ramma.html"
    )

@app.get("/database")
def get_artistas(request: Request, nombre : str = "pepe", otro : int = 1):
    menu = Menu(True, True)

    artistas = DaoArtistas().get_all(database)

    return templates.TemplateResponse(
        request=request, name="database.html", context={"menu": menu,"artistas": artistas,"nombre": nombre}
    )

@app.get("/deleteartistas/{artista_id}")
def delete_aritstas(request: Request,artista_id:str):
    dao = DaoArtistas()
    dao.delete(database, artista_id)
    
    artistas =  dao.get_all(database)
    return templates.TemplateResponse(
    request=request, name="database.html", context={"artistas": artistas}                                                      
)

@app.post("/delartistas")
def del_artistas(request: Request,artista_id:Annotated[str, Form()] ):
    print("hlhl")
    dao = DaoArtistas()
    dao.delete(database, artista_id)
    
    alumnos =  dao.get_all(database)
    return templates.TemplateResponse(
    request=request, name="database.html", context={"artistas": alumnos} )

@app.get("/formaddartistas")
def form_add_artistas(request: Request):
    return templates.TemplateResponse(
    request=request, name="formaddAlumnos.html"
    )

@app.post("/addartistas")
def add_artistas(request: Request, nombre: Annotated[str, Form()] = None):
    if nombre is None:
        return templates.TemplateResponse(
        request=request, name="database.html", context={"nombre": "pepe"}
        )
    
    dao = DaoArtistas()
    dao.insert(database, nombre)
    
    artistas =  dao.get_all(database)
    return templates.TemplateResponse(
    request=request, name="formaddAlumnos.html", context={"artistas": artistas}
)