"""
MapApp - save your favorite locations
"""
import datetime
import fastapi
import pydantic
import uuid
from deta import Deta

try:
    from src.mapapp.geojson.schema import NewFeature
except ImportError as e:
    print(e)

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
async def create_new_feature(new_feature: NewFeature) -> dict:
	try:
		# new_feature.id = uuid.uuid4()
		# new_feature.updated_at = datetime.datetime.now()
		# new_feature.created_at = datetime.datetime.now()
		return new_feature
	except pydantic.ValidationError as e:
		return e.json()
    