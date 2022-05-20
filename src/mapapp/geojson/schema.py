"""
GeoJSON schema as Pydantic models
"""
import enum
import pydantic
import typing
import uuid


# Types
LocationID = typing.NewType('LocationID', uuid.UUID)
    
class GeoJsonTypes(enum.Enum):
    """
    class GeoJsonTypes
    
    - this is just a convenient place (well, object) in which
      to store this data
      
    - these four GeoJSON data types are the only GeoJSON types I 
      anticipate needing for this app; time will tell ...
    """
    POINT = 'Point'
    MULTIPOINT = 'MultiPoint'
    FEATURE = 'Feature'
    FEATURE_COLLECTION = 'FeatureCollection'


class Position(pydantic.BaseModel):
    """
    GeoJSON's most fundamental object -- Position has:
    (1)  Longtitude (easting)   -- x
    (2)  Latitude (northing)    -- y  
    (3)  Altitude (elevation)   -- z (optional)
    """
    longitude: float
    latitude: float
    altitude: float
    
    
class BaseGeometry(pydantic.BaseModel):
    """
    Base class for GeoJSON geometry objects
    """
    type: str
    coordinates: Position
    

class Point(BaseGeometry):
    """
    """
    type: GeoJsonTypes.POINT.value
    coordinates: Position
    
    
class MultiPoint(BaseGeometry):
    """
    """
    type: GeoJsonTypes.MULTIPOINT.value
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
    id: LocationID
    type: GeoJsonTypes.FEATURE.value
    geometry: GeoJsonTypes.POINT.value
    properties: typing.Dict
    
    
class FeatureCollection(pydantic.BaseModel):
    """
    """
    id: LocationID
    type: GeoJsonTypes.FEATURE_COLLECTION
    features: typing.List[Feature]