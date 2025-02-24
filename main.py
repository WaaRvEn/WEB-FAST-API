from httpx import request
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

@app.get("/test")
def test(request: Request):
    menu = Menu(True, True)
    return templates.TemplateResponse(request= request, name="test.html", context={"menu": menu})

@app.get("/")
def read_root(request: Request):

    menu = Menu(True, True)

    artistas = DaoArtistas().get_all(database)

    return templates.TemplateResponse(
        request= request, name="index.html", context={"menu": menu,"artistas": artistas}
    )

@app.get("/")
def read_root(request: Request):

    menu = Menu(True, True)

    artistas = DaoArtistas().get_all(database)

    return templates.TemplateResponse(
        request= request, name="index_steven.html", context={"menu": menu,"artistas": artistas}
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


######################################################## DATA BASE ##############################################################


@app.get("/database")
def get_artistas(request: Request, nombre : str = "Steven"):

    menu = Menu(True, True)

    artistas = DaoArtistas().get_all(database)

    return templates.TemplateResponse(
        request=request, name="database.html", context={"menu": menu,"artistas": artistas}
    )

@app.get("/formaddartistas")
def form_add_artistas(request: Request):
    menu = Menu(True, True)

    artistas = DaoArtistas().get_all(database)

    return templates.TemplateResponse(
        request=request, name="formaddartistas.html", context={"menu": menu,"artistas": artistas}
    )

@app.post("/addartistas")
def add_artistas(request: Request, nombre: Annotated[str, Form()] = None):
    if nombre is None:
        return templates.TemplateResponse(
        request=request, name="formaddartistas.html", context={"artistas": artistas}
        )
    
    dao = DaoArtistas()
    dao.insert(database, nombre)
    
    artistas =  dao.get_all(database)
    menu = Menu(True, True)
    return templates.TemplateResponse(
    request=request, name="database.html", context={"menu" : menu, "artistas": artistas}
)
    
@app.get("/delartista")
def form_delete_artistas(request: Request):
    menu = Menu(True, True)
    dao = DaoArtistas()
    
    artistas =  dao.get_all(database)
    return templates.TemplateResponse(
        request=request, name="formdelartistas.html", context={"menu" : menu, "artistas" :artistas}
    )

@app.post("/delartistas")
def del_artistas(request: Request,artista_id:Annotated[str, Form()] ):
    dao = DaoArtistas()
    dao.delete(database, artista_id)
    artistas =  dao.get_all(database)
    menu = Menu(True, True)
    return templates.TemplateResponse(
    request=request, name="database.html", context={"menu" : menu, "artistas": artistas} )

@app.get("/formupdateartista")
def form_update_artista(request: Request):
    menu = Menu(True, True)
    dao = DaoArtistas()
    artistas = dao.get_all(database)
    
    return templates.TemplateResponse(
        request=request,
        name="formupdateartista.html",
        context={"menu": menu, "artistas": artistas}
    )

@app.post("/updateartista")
def update_artista(request: Request, artista_id: Annotated[str, Form()], nuevo_nombre: Annotated[str, Form()]):
    menu = Menu(True, True)
    dao = DaoArtistas()

    artistas = dao.get_all(database)
    
    return templates.TemplateResponse(
        request=request,
        name="database.html",
        context={"menu": menu, "artistas": artistas}
    )