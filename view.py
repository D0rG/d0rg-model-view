from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
@app.get('/view')
async def view():
    with open('view.html', 'r') as file:
        return HTMLResponse(file.read())
