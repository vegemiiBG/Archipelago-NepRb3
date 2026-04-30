import typing
from ..LocationData import LocationData

CastleChambers: typing.List[LocationData] = (
LocationData("Castle Chambers - Gather 1", 16_1, 0),
LocationData("Castle Chambers - Gather 2", 16_2, 0),
LocationData("Castle Chambers - Gather 3", 16_3, 0),
LocationData("Castle Chambers - Gather 4", 16_4, 0),
LocationData("Castle Chambers - Gather 5", 16_5, 0),
)

CastleChambersTreasures: typing.List[LocationData] = (
LocationData("Castle Chambers - Treasure 1", 16_1, "Treasure"),
LocationData("Castle Chambers - Treasure 2", 16_2, "Treasure"),
LocationData("Castle Chambers - Treasure 3", 16_3, "Treasure"),
LocationData("Castle Chambers - Treasure 4", 16_4, "Treasure"),
LocationData("Castle Chambers - Treasure 5", 16_5, "Treasure"),
)
