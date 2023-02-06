from fastapi import FastAPI

from api.routes.routes import router
from api.models import Base
from api.utils.database import engine


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Rhodes API",description="Rhodes backend documentation",license="MIT License",version="1.0.0")


app.include_router(router, prefix="/users", tags=["users"])
