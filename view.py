from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
@app.get('/')
async def view(model: int):
    model_name = ''

    if model == 1:
        model_name = 'view1.html'
    else:
        model_name = 'view2.html'

    with open(model_name, 'r') as file:
        return HTMLResponse(file.read())
