import typing
from ..LocationData import LocationData

SoniWetlands: typing.List[LocationData] = (
LocationData("Soni Wetlands","Gather 1", 39_1, 0),
LocationData("Soni Wetlands","Gather 2", 39_2, 0),
LocationData("Soni Wetlands","Gather 3", 39_3, 0),
LocationData("Soni Wetlands","Gather 4", 39_4, 0),
LocationData("Soni Wetlands","Gather 5", 39_5, 0),
LocationData("Soni Wetlands","Gather 6", 39_6, 0),
)

SoniWetlandsTreasures: typing.List[LocationData] = (
LocationData("Soni Wetlands","Treasure 1", 39_1, "Treasure"),
LocationData("Soni Wetlands","Treasure 2", 39_2, "Treasure"),
LocationData("Soni Wetlands","Treasure 3", 39_3, "Treasure"),
LocationData("Soni Wetlands","Treasure 4", 39_4, "Treasure"),
LocationData("Soni Wetlands","Treasure 5", 39_5, "Treasure"),
LocationData("Soni Wetlands","Treasure 6", 39_6, "Treasure"),
)
SoniWetlandsEnemies: typing.List[LocationData] = (
LocationData("Soni Wetlands","Nanovader", 153, "Enemy"),
LocationData("Soni Wetlands","Earth Golem", 158, "Enemy"),
LocationData("Soni Wetlands","Viral Earth Golem", 166, "Enemy"),
LocationData("Soni Wetlands","Aluna", 245, "Enemy"),
LocationData("Soni Wetlands","Viral Aluna", 252, "Enemy"),
LocationData("Soni Wetlands","Strange Person", 240, "Enemy"),
LocationData("Soni Wetlands","Self-Defense System ", 420, "Big Enemy"),
)