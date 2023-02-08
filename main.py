from fastapi import FastAPI

from models.users import users_model
from routers.users import users_router
from routers.auth import authen_router
from routers.items import items_router
from models.database import engine

app = FastAPI()


app.include_router(users_router.router)
app.include_router(authen_router.router)
app.include_router(items_router.router)

# users_model.Base.metadata.create_all(engine)
