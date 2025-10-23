import typing

from BaseClasses import Item, ItemClassification
from .names import ItemNames
from . import DropTables

apItemBaseID = 80000000
treasureItemIDOffset = 1000
dungeonItemIDOffset = 4000
keyItemIDOffset = 5000
consumableItemIDOffset = 10000
apTreasureBaseID = apItemBaseID + treasureItemIDOffset
apKeyItemBaseID = apItemBaseID + keyItemIDOffset
apDungeonItemBaseID = apItemBaseID + dungeonItemIDOffset
apConsumableItemBaseID = apItemBaseID = consumableItemIDOffset

class ItemData(typing.NamedTuple):
    code: int
    itemName: str
    classification: ItemClassification
    table: DropTables.InternalItem

class Rb3Item(Item):
    game: str = "Hyperdimension Neptunia Re;Birth3 V GENERATION"

dungeonItemList: typing.List[ItemData] = [
    ItemData(apDungeonItemBaseID + 1, ItemNames.dungeon_unlock_1, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 2, ItemNames.dungeon_unlock_2, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 3, ItemNames.dungeon_unlock_3, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 4, ItemNames.dungeon_unlock_4, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 5, ItemNames.dungeon_unlock_6, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 6, ItemNames.dungeon_unlock_8, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 7, ItemNames.dungeon_unlock_9, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 8, ItemNames.dungeon_unlock_10, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 9, ItemNames.dungeon_unlock_11, ItemClassification.progression),
    #ItemData(apDungeonItemBaseID + 10, ItemNames.dungeon_unlock_12, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 11, ItemNames.dungeon_unlock_13, ItemClassification.progression),
    #ItemData(apDungeonItemBaseID + 12, ItemNames.dungeon_unlock_14, ItemClassification.progression),
    #ItemData(apDungeonItemBaseID + 13, ItemNames.dungeon_unlock_15, ItemClassification.progression),
    #ItemData(apDungeonItemBaseID + 14, ItemNames.dungeon_unlock_16, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 15, ItemNames.dungeon_unlock_17, ItemClassification.progression),
    #ItemData(apDungeonItemBaseID + 16, ItemNames.dungeon_unlock_18, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 17, ItemNames.dungeon_unlock_19, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 18, ItemNames.dungeon_unlock_20, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 19, ItemNames.dungeon_unlock_21, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 20, ItemNames.dungeon_unlock_22, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 21, ItemNames.dungeon_unlock_23, ItemClassification.progression),
    #ItemData(apDungeonItemBaseID + 22, ItemNames.dungeon_unlock_24, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 23, ItemNames.dungeon_unlock_25, ItemClassification.progression),
    #ItemData(apDungeonItemBaseID + 24, ItemNames.dungeon_unlock_26, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 25, ItemNames.dungeon_unlock_27, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 26, ItemNames.dungeon_unlock_28, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 27, ItemNames.dungeon_unlock_29, ItemClassification.progression),
    #ItemData(apDungeonItemBaseID + 28, ItemNames.dungeon_unlock_30, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 29, ItemNames.dungeon_unlock_31, ItemClassification.progression),
    #ItemData(apDungeonItemBaseID + 30, ItemNames.dungeon_unlock_32, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 31, ItemNames.dungeon_unlock_33, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 32, ItemNames.dungeon_unlock_34, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 33, ItemNames.dungeon_unlock_35, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 34, ItemNames.dungeon_unlock_36, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 35, ItemNames.dungeon_unlock_37, ItemClassification.progression),
    #ItemData(apDungeonItemBaseID + 36, ItemNames.dungeon_unlock_38, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 37, ItemNames.dungeon_unlock_39, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 38, ItemNames.dungeon_unlock_40, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 39, ItemNames.dungeon_unlock_41, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 40, ItemNames.dungeon_unlock_42, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 41, ItemNames.dungeon_unlock_43, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 42, ItemNames.dungeon_unlock_44, ItemClassification.progression),
    #ItemData(apDungeonItemBaseID + 43, ItemNames.dungeon_unlock_45, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 44, ItemNames.dungeon_unlock_46, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 45, ItemNames.dungeon_unlock_47, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 46, ItemNames.dungeon_unlock_48, ItemClassification.progression),
    #ItemData(apDungeonItemBaseID + 47, ItemNames.dungeon_unlock_49, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 48, ItemNames.dungeon_unlock_50, ItemClassification.progression),
    #ItemData(apDungeonItemBaseID + 49, ItemNames.dungeon_unlock_51, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 50, ItemNames.dungeon_unlock_52, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 51, ItemNames.dungeon_unlock_53, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 52, ItemNames.dungeon_unlock_54, ItemClassification.progression),
    #ItemData(apDungeonItemBaseID + 53, ItemNames.dungeon_unlock_55, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 54, ItemNames.dungeon_unlock_56, ItemClassification.progression),
    #ItemData(apDungeonItemBaseID + 55, ItemNames.dungeon_unlock_57, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 56, ItemNames.dungeon_unlock_58, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 57, ItemNames.dungeon_unlock_59, ItemClassification.progression),
    #ItemData(apDungeonItemBaseID + 58, ItemNames.dungeon_unlock_60, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 59, ItemNames.dungeon_unlock_61, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 60, ItemNames.dungeon_unlock_62, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 61, ItemNames.dungeon_unlock_63, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 62, ItemNames.dungeon_unlock_64, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 63, ItemNames.dungeon_unlock_65, ItemClassification.progression),
    ItemData(apDungeonItemBaseID + 64, ItemNames.dungeon_unlock_67, ItemClassification.progression),
    #ItemData(apDungeonItemBaseID + 65, ItemNames.dungeon_unlock_68, ItemClassification.progression)
]

treasureList: typing.List[ItemData] = [
    ItemData(apTreasureBaseID + 1, ItemNames.vfsz_treasure1, ItemClassification.filler, DropTables.vfsz_treasure1),
    ItemData(apTreasureBaseID + 2, ItemNames.vfsz_treasure2, ItemClassification.filler, DropTables.vfsz_treasure2),
    ItemData(apTreasureBaseID + 3, ItemNames.vfsz_treasure3, ItemClassification.filler, DropTables.vfsz_treasure3),
    ItemData(apTreasureBaseID + 4, ItemNames.vfsz_treasure4, ItemClassification.filler, DropTables.vfsz_treasure4),
    ItemData(apTreasureBaseID + 5, ItemNames.stationArea_treasure1, ItemClassification.filler, DropTables.stationArea_treasure1)
]

keyItemList: typing.List[ItemData] = [
    ItemData(apKeyItemBaseID + 1, ItemNames.neps_pudding, ItemClassification.progression_skip_balancing),
    ItemData(apKeyItemBaseID + 2, ItemNames.compas_syringe, ItemClassification.progression_skip_balancing),
    ItemData(apKeyItemBaseID + 3, ItemNames.ifs_notebook, ItemClassification.progression_skip_balancing),
    ItemData(apKeyItemBaseID + 4, ItemNames.peashys_drawing, ItemClassification.progression_skip_balancing),
    ItemData(apKeyItemBaseID + 5, ItemNames.plutia_doll, ItemClassification.progression_skip_balancing)
]

consumableItemList: typing.List[ItemData] = [
    ItemData(apConsumableItemBaseID + 1, ItemNames.healing_grass, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 2, ItemNames.healing_pod, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 3, ItemNames.healing_drink, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 4, ItemNames.healing_bottle, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 5, ItemNames.nepbull, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 6, ItemNames.nepbull_c, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 7, ItemNames.nepbull_sp, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 8, ItemNames.nepbull_ex, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 9, ItemNames.nepbull_ex2, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 10, ItemNames.healing_circle, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 11, ItemNames.healing_rain, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 12, ItemNames.healing_field, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 13, ItemNames.healing_light, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 14, ItemNames.spcharger, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 15, ItemNames.pspcharger, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 16, ItemNames.pspcharger_2, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 17, ItemNames.hero_drink, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 18, ItemNames.hero_drink_c, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 19, ItemNames.hero_sausage, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 20, ItemNames.blanc_manju, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 21, ItemNames.plump_dogoo, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 22, ItemNames.horsebird_sashimi, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 23, ItemNames.detoxin, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 24, ItemNames.paralaxin, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 25, ItemNames.reflex, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 26, ItemNames.tuffmil, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 27, ItemNames.anti_venom, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 28, ItemNames.anti_paralysis, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 29, ItemNames.anti_seal, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 30, ItemNames.anti_virus, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 31, ItemNames.panacea, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 32, ItemNames.super_panacea, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 33, ItemNames.int_booster, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 34, ItemNames.int_booster_z, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 35, ItemNames.agi_booster, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 36, ItemNames.agi_booster_z, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 37, ItemNames.str_booster, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 38, ItemNames.str_booster_z, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 39, ItemNames.life_fragment, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 40, ItemNames.exuberant_fragment, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 41, ItemNames.exuberant_lump, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 42, ItemNames.angel_wings, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 43, ItemNames.real_angel_wings, ItemClassification.filler),
    ItemData(apConsumableItemBaseID + 44, ItemNames.eject_button, ItemClassification.filler)
]
