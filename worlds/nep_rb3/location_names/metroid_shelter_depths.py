import typing
from ..LocationData import LocationData

MetroidShelterDepths: typing.List[LocationData] = (
LocationData("Metroid Shelter Depths","Gather 1", 26_1, 0),
LocationData("Metroid Shelter Depths","Gather 2", 26_2, 0),
LocationData("Metroid Shelter Depths","Gather 3", 26_3, 0),
LocationData("Metroid Shelter Depths","Gather 4", 26_4, 0),
LocationData("Metroid Shelter Depths","Gather 5", 26_5, 0),
LocationData("Metroid Shelter Depths","Gather 6", 26_6, 0),
LocationData("Metroid Shelter Depths","Gather 7", 26_7, 0),
)

MetroidShelterDepthsTreasures: typing.List[LocationData] = (
LocationData("Metroid Shelter Depths","Treasure 1", 26_1, "Treasure"),
LocationData("Metroid Shelter Depths","Treasure 2", 26_2, "Treasure"),
LocationData("Metroid Shelter Depths","Treasure 3", 26_3, "Treasure"),
LocationData("Metroid Shelter Depths","Treasure 4", 26_4, "Treasure"),
)
MetroidShelterDepthsEnemies: typing.List[LocationData] = (
#LocationData("Metroid Shelter","Magma Stone", 153, "Enemy"),         Commented Enemies are Same as first area
#LocationData("Metroid Shelter","Blinky", 158, "Enemy"),
#LocationData("Metroid Shelter","Ms. Blinky", 166, "Enemy"),
LocationData("Metroid Shelter Depths","Volcano Crab", 300, "Enemy"),
LocationData("Metroid Shelter Depths","Viral Volcano Crab", 303, "Enemy"),
#LocationData("Metroid Shelter","Flame Fenrir ", 420, "Big Enemy"),
)