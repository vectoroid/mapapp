"""
"""
import fastapi
from deta import Deta

from .src.mapapp.geojson.schema import Feature

# config - for now, just put everything in a single file, until errors are eliminated.
db_config = {
    # DB naming convention: "project_app_items", where `items` = whatever is to be stored.
	'locations': "execas_mapapp_locations"
}
deta = Deta()
async_db = deta.AsyncBase(db_config["locations"])
app = fastapi.FastAPI()


# define root route
# (i.e. the home page, or "/")
@app.get("/")
async def root():
    return "Hello world!"

@app.post("/features/new")
async def create_new_feature(feature: Feature) -> dict:
    return feature
    