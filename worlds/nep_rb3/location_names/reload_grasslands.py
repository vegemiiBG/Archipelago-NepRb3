import typing
from ..LocationData import LocationData

ReloadGrasslands: typing.List[LocationData] = (
LocationData("Reload Grasslands","Gather 1", 42_1, 0),
LocationData("Reload Grasslands","Gather 2", 42_2, 0),
LocationData("Reload Grasslands","Gather 3", 42_3, 0),
LocationData("Reload Grasslands","Gather 4", 42_4, 0),
LocationData("Reload Grasslands","Gather 5", 42_5, 0),
LocationData("Reload Grasslands","Gather 6", 42_6, 0),
)

ReloadGrasslandsTreasures: typing.List[LocationData] = (
LocationData("Reload Grasslands","Treasure 1", 42_1, "Treasure"),
LocationData("Reload Grasslands","Treasure 2", 42_2, "Treasure"),
LocationData("Reload Grasslands","Treasure 3", 42_3, "Treasure"),
LocationData("Reload Grasslands","Treasure 4", 42_4, "Treasure"),
LocationData("Reload Grasslands","Treasure 5", 42_5, "Treasure"),
)
ReloadGrasslandsEnemies: typing.List[LocationData] = (
LocationData("Reload Grasslands","Nanovader", 153, "Enemy"),
LocationData("Reload Grasslands","Earth Golem", 158, "Enemy"),
LocationData("Reload Grasslands","Viral Earth Golem", 166, "Enemy"),
LocationData("Reload Grasslands","Aluna", 245, "Enemy"),
LocationData("Reload Grasslands","Viral Aluna", 252, "Enemy"),
LocationData("Reload Grasslands","Strange Person", 240, "Enemy"),
LocationData("Reload Grasslands","Self-Defense System ", 420, "Big Enemy"),
)