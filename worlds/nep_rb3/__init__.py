import logging
import os
import pkgutil
import typing
import settings
from .items import dungeonItemList, filler_items, useful_items
from typing import Set, Dict, Any, Callable, Optional

from BaseClasses import CollectionState, Region
from worlds.AutoWorld import World
from worlds.LauncherComponents import Component, Type, components, launch_subprocess
from Rules import set_location_rules


def launch_client():
    """Launch a Rb3 client"""
    from .client import launch
    launch_subprocess(launch, name="NepRb3Client")

components.append(Component(
    "Hyperdimension Neptunia Re;Birth3 V GENERATION Client",
    "NepRb3Client",
    func=launch_client,
    component_type=Type.CLIENT
))

from .items import NepRb3Item, item_data, allItemData
from .locations import NepRb3Location
from .options import NepRb3Options
from .locations import all_locations, gathers, location_table
from .Regions import Nep3RegionDef

class NepRb3World(World):
    """Nep."""

    game = "Hyperdimension Neptunia Re;Birth3 V GENERATION"
    options: NepRb3Options
    options_dataclass = NepRb3Options
    location_name_to_id = {loc_data.name: loc_data.id for loc_data in all_locations}

    item_name_to_id = {name: data.code for name, data in allItemData.items()}
    item_pool: list[NepRb3Item] = []

    disabled_locations = Set[str]

    def create_item(self, name: str) -> NepRb3Item:
        return NepRb3Item(name, allItemData[name].type, allItemData[name].code, self.player)

    def create_regions(self) -> None:
        self.disabled_locations = set()
        # Create regions.
        devin = Nep3RegionDef(self.multiworld,self.player,self.options)
        devin.setup_region_and_locations()
        devin.create_dungeon_exits()


    def create_items(self) -> None:
        item_pool= []
        item_pool.append(self.create_item("KEYITEM_PUDDING"))
        item_pool.append(self.create_item("KEYITEM_SYRINGE"))
        item_pool.append(self.create_item("KEYITEM_NOTEBOOK"))
        item_pool.append(self.create_item("KEYITEM_DOLL"))
        item_pool.append(self.create_item("KEYITEM_DRAWING"))

        for DungeonName in dungeonItemList.keys():
            item_pool.append(self.create_item(DungeonName))
##...
##item_pool length == total number of locations   
##...
##...
        numbersOfItemsInTheGame = len(self.multiworld.get_unfilled_locations(self.player))
        while numbersOfItemsInTheGame > len(item_pool):
            if self.random.randrange(0,100) > 55:
                item_pool.append(self.create_item(useful_items[self.random.randrange(0,len(useful_items))]))
            else:
                item_pool.append(self.create_item(filler_items[self.random.randrange(0,len(filler_items))]))
        self.multiworld.itempool += item_pool
    
    def get_filler_item_name(self) -> str:
        return

    def set_rules(self) -> None:
        set_location_rules(self)
        self.multiworld.completion_condition[self.player] = lambda state: state.can_reach_region("City Center",self.player)
        return

    def fill_slot_data(self) -> dict:
        return