from typing import List, Dict, TYPE_CHECKING, Optional
import math
from BaseClasses import Region, Location,MultiWorld,Entrance,CollectionState
from .LocationData import LocationData
from .locations import all_locations
from .options import NepRb3Options
from .items import item_id_to_name,apDungeonItemBaseID
from .names import DungeonIDs
if TYPE_CHECKING:
    from . import NepRb3World

class Rb3Location(Location):
    game: str = "Hyperdimension Neptunia Re;birth 3 V Generation"


class Nep3RegionDef:
    def __init__(self,world:MultiWorld,player:int, options:NepRb3Options):
        self.multiworld = world
        self.player = player
        self.option = options
        self.locations = all_locations #add option for dlc dungeons and include them in this list
        self.regions:Dict[str,Region]={}

    def setup_region_and_locations(self):
        for loc in self.locations:
            if loc.region not in self.regions:
                newRegion = self.create_region(loc.region)
                self.regions[loc.region] = newRegion
                self.multiworld.regions.append(newRegion)
            region = self.regions[loc.region]
            newLocation = self.create_location(loc,region)
            region.locations.append(newLocation)

        self.multiworld.regions.append(Region("Menu", self.player, self.multiworld))

    def hasAccessToDungeon(self,player:int,id):
        #if id == 32:
        #    return lambda state: state.has(dungeon_unlock_31,self.player)
        #elif id == otherdungeon:
        #    return basedungeon
        return lambda _: True  ## anything goes
        return lambda state: state.has(item_id_to_name[id+apDungeonItemBaseID],self.player)

    def create_dungeon_exits(self):
        menu = self.multiworld.get_region("Menu", self.player)
        newExit:Entrance
        for region in self.regions.values():
            id = DungeonIDs.all_dungeons[region.name]
            newExit = menu.add_exits([region.name],{region.name:self.hasAccessToDungeon(self.player,id)}) #missing rules

    def create_location(self,location_data: LocationData, region: Region) -> Location:
        location = Rb3Location(self.player, location_data.name, location_data.id, region)
        #create rule for location?
        return location

    def create_region(self, name: str) -> Region:
        region = Region(name, self.player, self.multiworld)
        return region

    def get_locations_per_region(self,locations: List[LocationData]) -> Dict[str, List[LocationData]]:
        per_region: Dict[str, List[LocationData]] = {}

        for location in locations:
            per_region.setdefault(location.region, []).append(location)

        return per_region

