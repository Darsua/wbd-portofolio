from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home():
    with open("pages/index.html") as f:
        return f.read()

@app.get("/projects", response_class=HTMLResponse)
async def projects():
    return RedirectResponse(url="https://github.com/Darsua?tab=repositories")

@app.get("/contact", response_class=HTMLResponse)
async def contact():
    return RedirectResponse(url="https://mail.google.com/mail/u/0/?to=darrelyanuar@gmail.com&tf=cm")
