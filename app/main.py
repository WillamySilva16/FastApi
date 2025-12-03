from fastapi import FastAPI
from routes import router

app = FastAPI()

@app.get("/")
def root():
    return {"status": "API conectada ao SQL Server"}

pp.include_router(router)
