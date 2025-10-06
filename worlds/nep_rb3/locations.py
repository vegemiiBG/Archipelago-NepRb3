import typing
from BaseClasses import Location
from .location_names.virtua_forest_safe_zone import VirtuaForestSafeZone
from .LocationData import LocationData

ap_location_base_id = 696969
class NepRb3Location(Location):
    game = "Hyperdimension Neptunia Re;Birth3 V GENERATION"
    
gathers: typing.List[LocationData] = (
VirtuaForestSafeZone
)
all_locations: typing.List[LocationData] = (
    gathers
)

location_table: typing.Dict[str, int] = {location.name: location.id for location in all_locations}