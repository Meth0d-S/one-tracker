import random
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

@app.get('/')
def hello():
    items = [
        'Pi (1997)',
        'Achtste-groepers huilen niet (2012)',
        'Witness for the Prosecution (1957)',
        'The Roaring Twenties (1939)'
    ]
    random.shuffle(items)
    return items

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://95.214.63.182"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)