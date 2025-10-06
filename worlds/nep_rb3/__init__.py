from typing import Callable

from BaseClasses import CollectionState, Region
from worlds.AutoWorld import World

from .items import NepRb3Item, item_data
from .locations import NepRb3Location, location_table, location_table
from .options import NepRb3Options
from .locations import all_locations

class NepRb3World(World):
    """Nep."""

    game = "Hyperdimension Neptunia Re;Birth3 V GENERATION"
    options: NepRb3Options
    options_dataclass = NepRb3Options
    location_name_to_id = {loc_data.name: loc_data.id for loc_data in all_locations}

    item_name_to_id = {name: data.code for name, data in item_data.items()}
    item_pool: list[NepRb3Item] = []

    def create_item(self, name: str) -> NepRb3Item:
        return NepRb3Item(name, item_data[name].type, item_data[name].code, self.player)

    def create_regions(self) -> None:
        # Create regions.
        region = Region("Menu", self.player, self.multiworld)
        for index, location in enumerate(all_locations):
            if "Herb" in location.name:
                self.item_pool.append(self.create_item("Herb"))

            if "Dogoo Jelly" in location.name:
                self.item_pool.append(self.create_item("Dogoo Jelly"))

            if "Coin Fragment" in location.name:
                self.item_pool.append(self.create_item("Coin Fragment"))

            if "Sunflowery Seed" in location.name:
                self.item_pool.append(self.create_item("Sunflowery Seed"))

            if "Yellow Petal" in location.name:
                self.item_pool.append(self.create_item("Yellow Petal"))

            if "Lizard Scale" in location.name:
                self.item_pool.append(self.create_item("Lizard Scale"))

            region.add_locations({location.name: location.id}, NepRb3Location)

        self.multiworld.itempool += self.item_pool
        self.multiworld.regions.append(region)

    def get_filler_item_name(self) -> str:
        return

    def set_rules(self) -> None:
        return

    def fill_slot_data(self) -> dict:
        return