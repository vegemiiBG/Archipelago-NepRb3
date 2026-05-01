import typing
from ..LocationData import LocationData

CityCenter: typing.List[LocationData] = (
LocationData("City Center","Gather 1", 34_1, 0),
LocationData("City Center","Gather 2", 34_2, 0),
LocationData("City Center","Gather 3", 34_3, 0),
LocationData("City Center","Gather 4", 34_4, 0),
LocationData("City Center","Gather 5", 34_5, 0),
)

CityCenterTreasures: typing.List[LocationData] = (
LocationData("City Center","Treasure 1", 34_1, "Treasure"),
LocationData("City Center","Treasure 2", 34_2, "Treasure"),
LocationData("City Center","Treasure 3", 34_3, "Treasure"),
LocationData("City Center","Treasure 4", 34_4, "Treasure"),
LocationData("City Center","Treasure 5", 34_5, "Treasure"),
)
