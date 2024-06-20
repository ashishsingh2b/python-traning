from deep_translator import GoogleTranslator
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')

def translate_to_spanish(english_text):
    translator = GoogleTranslator(source='en', target='es')
    spanish_text = translator.translate(english_text)
    return spanish_text

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "translated_text": None})

@app.post("/", response_class=HTMLResponse)
async def translate_text(request: Request, english_input: str = Form(...)):
    translated_text = translate_to_spanish(english_input)
    return templates.TemplateResponse("home.html", {"request": request, "translated_text": translated_text})
