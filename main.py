

import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware


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

init =

@app.on_event('startup')
async def app_startup():
    init.run()



@app.get('/')
async def root():
    return RedirectResponse(url='/docs')

@router.get(
    path='/primo/{number}',
    response_model=RSAOut,
    description=(
            '# Get all wallets strategy options \n\n'
            ''
            'This route will return all wallet\'s strategy'
    )
)
def get_primo(db=Depends(RSADb.get_db) ):
    primo
    return primo

if __name__ == '__main__':
    
    # Run server
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
