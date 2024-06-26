import uvicorn
from fastapi import FastAPI
from app.routers import rota_cadastro, rota_busca_info, rota_delete


app_topaz = FastAPI()

app_topaz.include_router(rota_cadastro.rota)
app_topaz.include_router(rota_busca_info.rota)
app_topaz.include_router(rota_delete.rota)

if __name__ == '__main__':
    uvicorn.run(app_topaz, host='127.0.0.1', port=8000)