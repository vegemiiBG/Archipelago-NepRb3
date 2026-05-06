from typing import List, Dict, TYPE_CHECKING, Optional,Set
import math
from BaseClasses import Region, Location,MultiWorld,Entrance,CollectionState,ItemClassification
from .LocationData import LocationData
from .locations import all_locations
from .location_names import levels
from .options import NepRb3Options
from .items import item_id_to_name,apDungeonItemBaseID,NepRb3Item
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
        self.monsterRegion:Dict[int,List[LocationData]] = {}

    def setup_region_and_locations(self):
        for loc in self.locations:
            if loc.region not in self.regions:
                newRegion = self.create_region(loc.region)
                self.regions[loc.region] = newRegion
                self.multiworld.regions.append(newRegion)
            region = self.regions[loc.region]

            if "Enemy" in loc.itemType:
                if loc.id in self.monsterRegion:
                    self.monsterRegion[loc.id].append(loc)
                else:
                    self.monsterRegion[loc.id] = [loc]
                continue
            newLocation = self.create_location(loc,region)
            region.locations.append(newLocation)
        
        # handle all enemies
        self.create_monster_regions_and_connect()
        self.multiworld.regions.append(Region("Menu", self.player, self.multiworld))
        self.create_level_events()

    def create_monster_regions_and_connect(self):
        for monsters in self.monsterRegion.values():
            if len(monsters) > 1:
                newMonsterRegion = self.create_region(monsters[0].objectiven_name)
                self.multiworld.regions.append(newMonsterRegion)
                for monster in monsters:
                    self.regions[monster.region].add_exits([newMonsterRegion.name],{newMonsterRegion.name:lambda _:True})
                monsters[0].name = monsters[0].objectiven_name
                newMonsterRegion.locations.append(self.create_location(monsters[0],newMonsterRegion))
            else:
                region = self.regions[monsters[0].region]
                region.locations.append(self.create_location(monsters[0],region))

    def create_level_events(self):
        dungeonGrindCapList:List[LocationData] =levels
        for grindSpot in dungeonGrindCapList:
            region = self.regions[grindSpot.region]
            location = Rb3Location(self.player,f"{grindSpot.name} {grindSpot.itemType} {grindSpot.id}",None,region)
            location.place_locked_item(NepRb3Item(f"{grindSpot.itemType} {grindSpot.id}",ItemClassification.progression,None,self.player))
            region.locations.append(location)

    def create_dungeon_exits(self):
        menu = self.multiworld.get_region("Menu", self.player)
        newExit:Entrance
        for region in self.regions.values():
            id = DungeonIDs.all_dungeons[region.name]

            newExit = menu.add_exits({region.name:region.name}) #missing rules

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

