import typing
from ..LocationData import LocationData

MagmaCaveDepths: typing.List[LocationData] = (
LocationData("Magma Cave Depths","Gather 1", 32_1, 0),
LocationData("Magma Cave Depths","Gather 2", 32_2, 0),
LocationData("Magma Cave Depths","Gather 3", 32_3, 0),
LocationData("Magma Cave Depths","Gather 4", 32_4, 0),
LocationData("Magma Cave Depths","Gather 5", 32_5, 0),
)

MagmaCaveDepthsTreasures: typing.List[LocationData] = (
LocationData("Magma Cave Depths","Treasure 1", 32_1, "Treasure"),
LocationData("Magma Cave Depths","Treasure 2", 32_2, "Treasure"),
LocationData("Magma Cave Depths","Treasure 3", 32_3, "Treasure"),
LocationData("Magma Cave Depths","Treasure 4", 32_4, "Treasure"),
)
MagmaCaveDepthsEnemies: typing.List[LocationData] = (
#LocationData("Magma Cave Depths","King Cardbird ", 153, "Enemy"),    SAME ENEMIES AS IN AREA 1
#LocationData("Magma Cave Depths","Magma Crab ", 158, "Enemy"),
#LocationData("Magma Cave Depths","Viral Magma Crab ", 166, "Enemy"),
LocationData("Magma Cave Depths","Flame Skeleton", 135, "Enemy"),
LocationData("Magma Cave Depths","Rafflesia", 247, "Enemy"),
LocationData("Magma Cave Depths","Viral Rafflesia", 254, "Enemy"),
LocationData("Magma Cave Depths","Dolichorhynchops", 410, "Big Enemy"),
)