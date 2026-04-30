import typing
from ..LocationData import LocationData

GraphicPass: typing.List[LocationData] = (
LocationData("Graphic Pass - Gather 1", 50_1, 0),
LocationData("Graphic Pass - Gather 2", 50_2, 0),
LocationData("Graphic Pass - Gather 3", 50_3, 0),
LocationData("Graphic Pass - Gather 4", 50_4, 0),
LocationData("Graphic Pass - Gather 5", 50_5, 0),
LocationData("Graphic Pass - Gather 6", 50_6, 0),
)

GraphicPassTreasures: typing.List[LocationData] = (
LocationData("Graphic Pass - Treasure 1", 50_1, "Treasure"),
LocationData("Graphic Pass - Treasure 2", 50_2, "Treasure"),
LocationData("Graphic Pass - Treasure 3", 50_3, "Treasure"),
LocationData("Graphic Pass - Treasure 4", 50_4, "Treasure"),
)
