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
#SuahoMountainPeakEnemies: typing.List[LocationData] = (              Same Exact Enemies as Area 1
#LocationData("Suaho Mountain Range","Hyena", 179, "Enemy"), 
#LocationData("Suaho Mountain Range","Viral Hyena", 185, "Enemy"),
#LocationData("Suaho Mountain Range","Pinky", 208, "Enemy"),
#LocationData("Suaho Mountain Range","Ms. Pinky", 219, "Enemy"),
#LocationData("Suaho Mountain Range","Paradise Avian", 114, "Enemy"),
#LocationData("Suaho Mountain Range","Viral Paradise Avian", 119, "Enemy"),
#LocationData("Suaho Mountain Range","Roc", 413, "Big Enemy"),
#)