from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse(
        request= request, name="index.html"
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