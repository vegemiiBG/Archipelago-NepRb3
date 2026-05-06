import typing
from ..LocationData import LocationData

JetSetPeak: typing.List[LocationData] = (
LocationData("Jet Set Peak","Gather 1", 5_1, "Gather"),
LocationData("Jet Set Peak","Gather 2", 5_2, "Gather"),
LocationData("Jet Set Peak","Gather 3", 5_3, "Gather"),
LocationData("Jet Set Peak","Gather 4", 5_4, "Gather"),
LocationData("Jet Set Peak","Gather 5", 5_5, "Gather"),
)

JetSetPeakTreasures: typing.List[LocationData] = (
LocationData("Jet Set Peak","Treasure 1", 5_1, "Treasure"),
LocationData("Jet Set Peak","Treasure 2", 5_2, "Treasure"),
LocationData("Jet Set Peak","Treasure 3", 5_3, "Treasure"),
LocationData("Jet Set Peak","Treasure 4", 5_4, "Treasure"),
LocationData("Jet Set Peak","Treasure 5", 5_5, "Treasure"),
)
JetSetPeakEnemies: typing.List[LocationData] = (
LocationData("Jet Set Peak","Pal Shell", 153, "Enemy"), 
LocationData("Jet Set Peak","Fungus", 158, "Enemy"),
LocationData("Jet Set Peak","Shoebill", 166, "Enemy"),
LocationData("Jet Set Peak","Viral Shoebill", 245, "Enemy"),
LocationData("Jet Set Peak","Alraune", 252, "Enemy"),
LocationData("Jet Set Peak","Viral Alraune", 240, "Enemy"),
LocationData("Jet Set Peak","Ancient Dragon", 420, "Big Enemy"),
)