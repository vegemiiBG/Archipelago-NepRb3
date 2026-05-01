import typing
from ..LocationData import LocationData

MetroidShelter: typing.List[LocationData] = (
LocationData("Metroid Shelter","Gather 1", 25_1, 0),
LocationData("Metroid Shelter","Gather 2", 25_2, 0),
LocationData("Metroid Shelter","Gather 3", 25_3, 0),
LocationData("Metroid Shelter","Gather 4", 25_4, 0),
LocationData("Metroid Shelter","Gather 5", 25_5, 0),
)

MetroidShelterTreasures: typing.List[LocationData] = (
LocationData("Metroid Shelter","Treasure 1", 25_1, "Treasure"),
LocationData("Metroid Shelter","Treasure 2", 25_2, "Treasure"),
LocationData("Metroid Shelter","Treasure 3", 25_3, "Treasure"),
LocationData("Metroid Shelter","Treasure 4", 25_4, "Treasure"),
)
