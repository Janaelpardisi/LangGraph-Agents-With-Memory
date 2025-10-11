from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from Agents import run_agent

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "response": None})

@app.post("/", response_class=HTMLResponse)
async def post_topic(request: Request, topic: str = Form(...)):
    result = run_agent(topic)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "response": result,
        "topic": topic
    })
