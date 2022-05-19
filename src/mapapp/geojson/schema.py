"""
GeoJSON schema as Pydantic models
"""
import enum
import pydantic
import typing
import uuid

    
class GeoJsonTypes(enum.Enum):
    """
    """
    POINT = 'Point'
    MULTIPOINT = 'MultiPoint'
    FEATURE = 'Feature'
    FEATURE_COLLECTION = 'FeatureCollection'


class Position(pydantic.BaseModel):
    """
    GeoJSON's most fundamental object -- Position has:
    (1)  Longtitude (easting)
    (2)  Latitude (northing)
    (3)  Altitude (elevation)
    """
    longitude: float
    latitude: float
    altitude: float
    
    
class BaseGeometry(typing.TypedDict):
    """
    Base class for GeoJSON geometry objects
    """
    type: str
    coordinates: Position
    

class Point(BaseGeometry):
    """
    """
    type: GeoJsonTypes.POINT
    coordinates: Position
    
    
class MultiPoint(BaseGeometry):
    """
    """
    type: GeoJsonTypes.MULTIPOINT
    coordinates: typing.List[Position]
    
    
class LocationProperties(pydantic.BaseModel):
    """
    Bespoke properties (i.e. metadata) about each location saved in the database.
    """
    name: str = pydantic.Field()
    
    
    
class Feature(pydantic.BaseModel):
    """
    Represents a single location in the MapApp map
    
    note: in the GeoJSON specification, this is not true; the geometry of a feature can be set to any of the geometry types.
          however, in this application, I anticipate needing to save only single-point locations.
          naturally, if that changes, some refactoring will be needed.
    """
    id: uuid.uuid4
    type: GeoJsonTypes.FEATURE
    geometry: Point
    properties: typing.Dict
    
    
class FeatureCollection(pydantic.BaseModel):
    """
    """
    id: uuid.uuid4
    type: GeoJsonTypes.FEATURE_COLLECTION
    features: typing.List[Feature]