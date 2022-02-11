from fileinput import filename
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse


app = FastAPI()
@app.get('/')
async def view(model: int):
    page_name = 'view' + str(model) + '.html'
    with open(page_name, 'r') as file:
        return HTMLResponse(file.read())


@app.get('/model/{model_name}')
async def get_model(model_name: str):
    return FileResponse('models/' + model_name, filename=model_name ,media_type='application/octet-stream')


@app.get('/storage/{filename}')
async def view(filename: str):
    return FileResponse(filename, filename=filename ,media_type='application/octet-stream')
