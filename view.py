from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse

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


@app.get('/model/{model}')
async def get_model(model: int):
    model_name = '\models'
    if model == 1:
        model_name += '\model'
    else:
        model_name += '\model2'

    model_name += '.gltf'
    return FileResponse(model_name)
