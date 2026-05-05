import typing
from ..LocationData import LocationData

VirtuaForestDepths: typing.List[LocationData] = (
LocationData("Virtua Forest Depths","Gather 1", 55_1, 0),
LocationData("Virtua Forest Depths","Gather 2", 55_2, 0),
LocationData("Virtua Forest Depths","Gather 3", 55_3, 0),
LocationData("Virtua Forest Depths","Gather 4", 55_4, 0),
LocationData("Virtua Forest Depths","Gather 5", 55_5, 0),
)

VirtuaForestDepthsTreasures: typing.List[LocationData] = (
LocationData("Virtua Forest Depths","Treasure 1", 55_1, "Treasure"),
LocationData("Virtua Forest Depths","Treasure 2", 55_2, "Treasure"),
LocationData("Virtua Forest Depths","Treasure 3", 55_3, "Treasure"),
LocationData("Virtua Forest Depths","Treasure 4", 55_4, "Treasure"),
LocationData("Virtua Forest Depths","Treasure 5", 55_5, "Treasure"),
)
#VirtuaForestDepthsEnemies: typing.List[LocationData] = (           Enemies are exactly the same as in VF
#LocationData("Virtua Forest","Invader", 155, "Enemy"),
#LocationData("Virtua Forest","Jellyfish Dogoo", 110, "Enemy"),
#LocationData("Virtua Forest","Forest Guardian", 162, "Enemy"),
#LocationData("Virtua Forest","Viral Forest Guardian", 170, "Enemy"),
#LocationData("Virtua Forest","Sentientree", 232, "Enemy"),
#LocationData("Virtua Forest","Viral Sentientree", 236, "Enemy"),
#LocationData("Virtua Forest","Forest Lord", 433, "Big Enemy"),
#)