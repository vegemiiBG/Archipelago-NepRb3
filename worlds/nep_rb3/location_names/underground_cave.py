import typing
from ..LocationData import LocationData

UndergroundCave: typing.List[LocationData] = (
LocationData("Underground Cave","Gather 1", 15_1, 0),
LocationData("Underground Cave","Gather 2", 15_2, 0),
LocationData("Underground Cave","Gather 3", 15_3, 0),
LocationData("Underground Cave","Gather 4", 15_4, 0),
LocationData("Underground Cave","Gather 5", 15_5, 0),
LocationData("Underground Cave","Gather 6", 15_6, 0),
LocationData("Underground Cave","Gather 7", 15_7, 0),
)

UndergroundCaveTreasures: typing.List[LocationData] = (
LocationData("Underground Cave","Treasure 1", 15_1, "Treasure"),
LocationData("Underground Cave","Treasure 2", 15_2, "Treasure"),
LocationData("Underground Cave","Treasure 3", 15_3, "Treasure"),
LocationData("Underground Cave","Treasure 4", 15_4, "Treasure"),
LocationData("Underground Cave","Treasure 5", 15_5, "Treasure"),
)
UndergroundCaveEnemies: typing.List[LocationData] = (
LocationData("Underground Cave","Nanovader", 153, "Enemy"),
LocationData("Underground Cave","Earth Golem", 158, "Enemy"),
LocationData("Underground Cave","Viral Earth Golem", 166, "Enemy"),
LocationData("Underground Cave","Aluna", 245, "Enemy"),
LocationData("Underground Cave","Viral Aluna", 252, "Enemy"),
LocationData("Underground Cave","Strange Person", 240, "Enemy"),
LocationData("Underground Cave","Self-Defense System ", 420, "Big Enemy"),
)