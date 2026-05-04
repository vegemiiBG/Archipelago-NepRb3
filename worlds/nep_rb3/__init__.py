import logging
import os
import pkgutil
import typing
import settings
from .items import dungeonItemList, filler_items, useful_items,characterItemList
from typing import Set, Dict, Any, Callable, Optional

from BaseClasses import CollectionState, Region
from worlds.AutoWorld import World
from worlds.LauncherComponents import Component, Type, components, launch_subprocess

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
from .names import ItemNames,progressiveGear
from .Regions import Nep3RegionDef
from .Rules import *

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
        set_all_planeptune_dungeons(self)
        set_all_lastation_dungeons(self)
        set_all_lowee_dungeons(self)
        set_all_leanbox_dungeons(self)
        set_all_hyper_dungeons(self)
        set_all_hello_dungeons(self)
        set_all_pc_dungeons(self)
        set_all_eden_dungeons(self)
        set_win_condition(self)


    def create_items(self) -> None:
        item_pool= []
        item_pool.append(self.create_item(ItemNames.neps_pudding))
        item_pool.append(self.create_item(ItemNames.compas_syringe))
        item_pool.append(self.create_item(ItemNames.ifs_notebook))
        item_pool.append(self.create_item(ItemNames.plutia_doll))
        item_pool.append(self.create_item(ItemNames.peashys_drawing))
        for DungeonName in dungeonItemList.keys():
            item_pool.append(self.create_item(DungeonName))
        # Starting Character
        starting_character = CharacterNames.neptune
        self.multiworld.push_precollected(self.create_item(starting_character))

        for CharacterName in characterItemList.keys():
            if starting_character == CharacterName: continue
            item_pool.append(self.create_item(CharacterName))
            
        for i in range(0,6):
            item_pool.append(self.create_item(progressiveGear.neptune_progressive_gear))
        for i in range(0,6):
            item_pool.append(self.create_item(progressiveGear.noire_progressive_gear))
        for i in range(0,6):
            item_pool.append(self.create_item(progressiveGear.plutia_progressive_gear))
        for i in range(0,5):
            item_pool.append(self.create_item(progressiveGear.blanc_progressive_gear))
        for i in range(0,5):
            item_pool.append(self.create_item(progressiveGear.vert_progressive_gear))
        for i in range(0,5):
            item_pool.append(self.create_item(progressiveGear.nepgear_progressive_gear))
        for i in range(0,5):
            item_pool.append(self.create_item(progressiveGear.peashy_progressive_gear))
        for i in range(0,3):
            item_pool.append(self.create_item(progressiveGear.uni_progressive_gear))
        for i in range(0,4):
            item_pool.append(self.create_item(progressiveGear.rom_progressive_gear))
        for i in range(0,4):
            item_pool.append(self.create_item(progressiveGear.ram_progressive_gear))
        for i in range(0,6):
            item_pool.append(self.create_item(progressiveGear.progressive_armor))

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
        
        return

    def fill_slot_data(self) -> dict:
        return
