import typing
from ..LocationData import LocationData

GigoDepths: typing.List[LocationData] = (
LocationData("Gigo Depths","Gather 1", 18_1, 0),
LocationData("Gigo Depths","Gather 2", 18_2, 0),
LocationData("Gigo Depths","Gather 3", 18_3, 0),
LocationData("Gigo Depths","Gather 4", 18_4, 0),
LocationData("Gigo Depths","Gather 5", 18_5, 0),
)

GigoDepthsTreasures: typing.List[LocationData] = (
LocationData("Gigo Depths","Treasure 1", 18_1, "Treasure"),
LocationData("Gigo Depths","Treasure 2", 18_2, "Treasure"),
LocationData("Gigo Depths","Treasure 3", 18_3, "Treasure"),
LocationData("Gigo Depths","Treasure 4", 18_4, "Treasure"),
LocationData("Gigo Depths","Treasure 5", 18_5, "Treasure"),
)
GigoDepthsEnemies: typing.List[LocationData] = (
LocationData("Gigo Depths","Malvader", 154, "Enemy"),
#LocationData("Gigo Depths","SHDC", 327, "Enemy"), Cant find enemy
#LocationData("Gigo Depths","Swallowtail", 331, "Enemy"), Same enemies as area 1, only Malvader is a new enemy
#LocationData("Gigo Depths","Viral Swallowtail ", 335, "Enemy"),
#LocationData("Gigo Depths","Horsebird", 329, "Enemy"),
#LocationData("Gigo Depths","King Crab ", 436, "Big Enemy"),
)