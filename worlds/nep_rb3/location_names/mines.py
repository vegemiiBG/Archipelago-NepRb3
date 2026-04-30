import typing
from ..LocationData import LocationData

Mines: typing.List[LocationData] = (
LocationData("Mines - Gather 1", 21_1, 0),
LocationData("Mines - Gather 2", 21_2, 0),
LocationData("Mines - Gather 3", 21_3, 0),
LocationData("Mines - Gather 4", 21_4, 0),
LocationData("Mines - Gather 5", 21_5, 0),
LocationData("Mines - Gather 6", 21_6, 0),
LocationData("Mines - Gather 7", 21_7, 0),
LocationData("Mines - Gather 8", 21_8, 0),
)

MinesTreasures: typing.List[LocationData] = (
LocationData("Mines - Treasure 1", 21_1, "Treasure"),
LocationData("Mines - Treasure 2", 21_2, "Treasure"),
LocationData("Mines - Treasure 3", 21_3, "Treasure"),
LocationData("Mines - Treasure 4", 21_4, "Treasure"),
LocationData("Mines - Treasure 5", 21_5, "Treasure"),
)
