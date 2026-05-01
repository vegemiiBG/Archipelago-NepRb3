import typing
from ..LocationData import LocationData

MagmaCave: typing.List[LocationData] = (
LocationData("Magma Cave","Gather 1", 31_1, 0),
LocationData("Magma Cave","Gather 2", 31_2, 0),
LocationData("Magma Cave","Gather 3", 31_3, 0),
LocationData("Magma Cave","Gather 4", 31_4, 0),
LocationData("Magma Cave","Gather 5", 31_5, 0),
)

MagmaCaveTreasures: typing.List[LocationData] = (
LocationData("Magma Cave","Treasure 1", 31_1, "Treasure"),
LocationData("Magma Cave","Treasure 2", 31_2, "Treasure"),
LocationData("Magma Cave","Treasure 3", 31_3, "Treasure"),
LocationData("Magma Cave","Treasure 4", 31_4, "Treasure"),
)
