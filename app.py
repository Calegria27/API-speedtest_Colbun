from fastapi import FastAPI
from routes.speed import router

app=FastAPI()


app.include_router(router)