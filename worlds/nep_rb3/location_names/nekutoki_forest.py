import typing
from ..LocationData import LocationData

NekutokiForest: typing.List[LocationData] = (
LocationData("Nekutoki Forest","Gather 1", 47_1, "Gather"),
LocationData("Nekutoki Forest","Gather 2", 47_2, "Gather"),
LocationData("Nekutoki Forest","Gather 3", 47_3, "Gather"),
LocationData("Nekutoki Forest","Gather 4", 47_4, "Gather"),
LocationData("Nekutoki Forest","Gather 5", 47_5, "Gather"),
)

NekutokiForestTreasures: typing.List[LocationData] = (
LocationData("Nekutoki Forest","Treasure 1", 47_1, "Treasure"),
LocationData("Nekutoki Forest","Treasure 2", 47_2, "Treasure"),
LocationData("Nekutoki Forest","Treasure 3", 47_3, "Treasure"),
LocationData("Nekutoki Forest","Treasure 4", 47_4, "Treasure"),
LocationData("Nekutoki Forest","Treasure 5", 47_5, "Treasure"),
)
NekutokiForestEnemies: typing.List[LocationData] = (
#LocationData("Kobaba Ruins","Leanbox Soldier", 295, "Enemy"),   These enemies appear in Kobaba Ruins
#LocationData("Kobaba Ruins","Crack Tail", 201, "Enemy"),
#LocationData("Kobaba Ruins","Missile Golem", 160, "Enemy"),
#LocationData("Kobaba Ruins","Viral Missile Golem", 168, "Enemy"),
LocationData("Nekutoki Forest","Strange Person", 252, "Enemy"),
LocationData("Nekutoki Forest","Forest Crab", 437, "Big Enemy"),
)