from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home():
    with open("pages/index.html") as f:
        return f.read()

@app.get("/projects", response_class=HTMLResponse)
async def projects():
    with open("pages/projects.html") as f:
        return f.read()

@app.get("/contact", response_class=HTMLResponse)
async def contact():
    with open("pages/contact.html") as f:
        return f.read()
