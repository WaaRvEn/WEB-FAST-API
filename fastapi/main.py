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
        request= request, name="steven.html"
    )

@app.get("/plantilla")
def plantilla(request: Request):
    return templates.TemplateResponse(
        request= request, name="index.html"
    )
