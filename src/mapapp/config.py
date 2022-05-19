import pydantic

class MapAppSettings(pydantic.BaseSettings):
    """
    MapAppSettings class
    
    Application config/settings values for MapApp
    """
    deta_base_name: str = 'mapapp_places'