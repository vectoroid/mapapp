"""
"""
import deta
import fastapi
from .src.mapapp import MapAppSettings

# initialization
settings = MapAppSettings()
deta = deta.Deta()
db = deta.Base(settings.deta_base_name)
app = fastapi.FastAPI()


@app.get("/")
async def root():
	return {"data": {"message": "Hello, world!"}}
