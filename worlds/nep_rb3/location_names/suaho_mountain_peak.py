import typing
from ..LocationData import LocationData

SuahoMountainPeak: typing.List[LocationData] = (
LocationData("Suaho Mountain Peak","Gather 1", 60_1, 0),
LocationData("Suaho Mountain Peak","Gather 2", 60_2, 0),
LocationData("Suaho Mountain Peak","Gather 3", 60_3, 0),
LocationData("Suaho Mountain Peak","Gather 4", 60_4, 0),
LocationData("Suaho Mountain Peak","Gather 5", 60_5, 0),
)

SuahoMountainPeakTreasures: typing.List[LocationData] = (
LocationData("Suaho Mountain Peak","Treasure 1", 60_1, "Treasure"),
LocationData("Suaho Mountain Peak","Treasure 2", 60_2, "Treasure"),
LocationData("Suaho Mountain Peak","Treasure 3", 60_3, "Treasure"),
LocationData("Suaho Mountain Peak","Treasure 4", 60_4, "Treasure"),
LocationData("Suaho Mountain Peak","Treasure 5", 60_5, "Treasure"),
)
SuahoMountainPeakEnemies: typing.List[LocationData] = (
LocationData("Suaho Mountain Peak","Nanovader", 153, "Enemy"),
LocationData("Suaho Mountain Peak","Earth Golem", 158, "Enemy"),
LocationData("Suaho Mountain Peak","Viral Earth Golem", 166, "Enemy"),
LocationData("Suaho Mountain Peak","Aluna", 245, "Enemy"),
LocationData("Suaho Mountain Peak","Viral Aluna", 252, "Enemy"),
LocationData("Suaho Mountain Peak","Strange Person", 240, "Enemy"),
LocationData("Suaho Mountain Peak","Self-Defense System ", 420, "Big Enemy"),
)