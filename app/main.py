from fastapi import FastAPI
from .routes import router  # IMPORTANTE

app = FastAPI()

# registra as rotas definidas em routes.py
app.include_router(router)
