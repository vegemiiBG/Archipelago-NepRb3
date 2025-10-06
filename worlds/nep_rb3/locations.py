import typing
from BaseClasses import Location
from .location_names.virtua_forest_safe_zone import VirtuaForestSafeZone
from .LocationData import LocationData

ap_location_base_id = 696969
class NepRb3Location(Location):
    game = "Hyperdimension Neptunia Re;Birth3 V GENERATION"
    
all_locations: typing.List[LocationData] = (
VirtuaForestSafeZone
)
location_table: dict[str, int] = {
    # fmt: off
    "The Button":    69696969,
    # fmt: on
}
