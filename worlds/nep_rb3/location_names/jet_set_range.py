import typing
from ..LocationData import LocationData

JetSetRange: typing.List[LocationData] = (
LocationData("Jet Set Range","Gather 1", 4_1, 0),
LocationData("Jet Set Range","Gather 2", 4_2, 0),
LocationData("Jet Set Range","Gather 3", 4_3, 0),
LocationData("Jet Set Range","Gather 4", 4_4, 0),
LocationData("Jet Set Range","Gather 5", 4_5, 0),
)
JetSetRangeTreasures: typing.List[LocationData] = (
LocationData("Jet Set Range","Treasure 1", 4_1, "Treasure"),
LocationData("Jet Set Range","Treasure 2", 4_2, "Treasure"),
LocationData("Jet Set Range","Treasure 3", 4_3, "Treasure"),
LocationData("Jet Set Range","Treasure 4", 4_4, "Treasure"),
)
JetSetRangeEnemies: typing.List[LocationData] = (
LocationData("Jet Set Range","Cardbird", 172, "Enemy"),
LocationData("Jet Set Range","Sunflowery", 227, "Enemy"),
LocationData("Jet Set Range","Pal Shell", 195, "Enemy"),
LocationData("Jet Set Range","Alraune", 244, "Enemy"),
LocationData("Jet Set Range","Viral Alraune", 251, "Enemy"),
LocationData("Jet Set Range","Ancient Dragon", 401, "Big Enemy"),
)
