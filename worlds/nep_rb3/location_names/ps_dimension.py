import typing
from ..LocationData import LocationData

PSDimension: typing.List[LocationData] = (
LocationData("PS Dimension - Gather 1", 40_1, 0),
LocationData("PS Dimension - Gather 2", 40_2, 0),
LocationData("PS Dimension - Gather 3", 40_3, 0),
LocationData("PS Dimension - Gather 4", 40_4, 0),
LocationData("PS Dimension - Gather 5", 40_5, 0),
)

PSDimensionTreasures: typing.List[LocationData] = (
LocationData("PS Dimension - Treasure 1", 40_1, "Treasure"),
LocationData("PS Dimension - Treasure 2", 40_2, "Treasure"),
LocationData("PS Dimension - Treasure 3", 40_3, "Treasure"),
LocationData("PS Dimension - Treasure 4", 40_4, "Treasure"),
LocationData("PS Dimension - Treasure 5", 40_5, "Treasure"),
LocationData("PS Dimension - Treasure 6", 40_6, "Treasure"),
)
