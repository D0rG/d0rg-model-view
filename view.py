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
    model_name = ''
    if model == 1:
        model_name += 'test.glb'
    elif model == 2:
        model_name += 'test.usdz'

    return FileResponse('models/' + model_name, filename=model_name ,media_type='application/octet-stream')
