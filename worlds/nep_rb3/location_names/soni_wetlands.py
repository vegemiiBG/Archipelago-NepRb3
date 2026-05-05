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
#LocationData("Soni Wetlands","Matango ", 265, "Enemy"),     Same Enemy in another dungeon
LocationData("Soni Wetlands","Healing Dogoo", 106, "Enemy"),
LocationData("Soni Wetlands","Lean Tuna", 191, "Enemy"),
LocationData("Soni Wetlands","Heavy Dragoon", 267, "Enemy"),
LocationData("Soni Wetlands","Viral Heavy Dragoon", 277, "Enemy"),
LocationData("Soni Wetlands","Nidhogg", 420, "Big Enemy"),
)