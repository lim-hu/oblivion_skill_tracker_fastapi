from fastapi import FastAPI
from . import models
from .database import engine
from .router import skill
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(skill.router)


@app.get('/')
@app.get('/home')
def home():
    return {'message': 'Home Page'}
