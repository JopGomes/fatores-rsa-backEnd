

import uvicorn
from fastapi import Depends, FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from core.schemas.primo import *

from database.db import BancoDados


app = FastAPI(
    title='RSA API',
    version='1.0.0'
)


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_methods=["*"],
    allow_headers=["*"]
)



@app.get('/')
async def root():
    return RedirectResponse(url='/docs')

@app.get(
    path='/primo/{number}',
    response_model=RSAOut,
    description=(
            '# Retorna o RSAOut \n\n'
            ''
            ''
    )
)
def get_primo(db = BancoDados(), number = int):
    primo = db.buscarFatores(n=number)
    if not primo:
        output = RSACreate(fator1=-1,fator2=-1,produto=-1)
        return output
    output = RSACreate(fator1=primo.fator1,fator2=primo.fator2,produto=primo.produto)
    return output

if __name__ == '__main__':
    
    # Run server
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
