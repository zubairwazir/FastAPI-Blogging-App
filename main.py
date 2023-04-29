from fastapi_offline import FastAPIOffline as FastAPI
from app.config.database import engine
from app.models.models import Base
from app.routers import user, blog


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(blog.router)
