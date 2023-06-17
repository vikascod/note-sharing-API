from fastapi import FastAPI
from app.database import Base, engine
from app import models
from app.router import user, note, auth, share

models.Base.metadata.create_all(engine)

app = FastAPI()

@app.get('/')
def home():
    return 'Hello World'


app.include_router(user.router)
app.include_router(note.router)
app.include_router(auth.router)
app.include_router(share.router)