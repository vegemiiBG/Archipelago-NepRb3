import typing
from ..LocationData import LocationData

HaloForest: typing.List[LocationData] = (
LocationData("Halo Forest","Gather 1", 19_1, 0),
LocationData("Halo Forest","Gather 2", 19_2, 0),
LocationData("Halo Forest","Gather 3", 19_3, 0),
LocationData("Halo Forest","Gather 4", 19_4, 0),
LocationData("Halo Forest","Gather 5", 19_5, 0),
)

HaloForestTreasures: typing.List[LocationData] = (
LocationData("Halo Forest","Treasure 1", 19_1, "Treasure"),
LocationData("Halo Forest","Treasure 2", 19_2, "Treasure"),
LocationData("Halo Forest","Treasure 3", 19_3, "Treasure"),
LocationData("Halo Forest","Treasure 4", 19_4, "Treasure"),
LocationData("Halo Forest","Treasure 5", 19_5, "Treasure"),
)
HaloForestEnemies: typing.List[LocationData] = (
LocationData("Halo Forest","Moulin Rogue ", 228, "Enemy"),
LocationData("Halo Forest","Rukh", 115, "Enemy"),
LocationData("Halo Forest","Viral Rukh ", 120, "Enemy"),
LocationData("Halo Forest","Tarantula", 311, "Enemy"),
LocationData("Halo Forest","Wolf", 180, "Enemy"),
LocationData("Halo Forest","Viral Wolf ", 186, "Enemy"),
LocationData("Halo Forest","Phoenix ", 414, "Big Enemy"),
)