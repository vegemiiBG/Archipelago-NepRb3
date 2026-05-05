import typing
from ..LocationData import LocationData

UnderInverse: typing.List[LocationData] = (
LocationData("Under Inverse","Gather 1", 56_1, 0),
LocationData("Under Inverse","Gather 2", 56_2, 0),
LocationData("Under Inverse","Gather 3", 56_3, 0),
LocationData("Under Inverse","Gather 4", 56_4, 0),
LocationData("Under Inverse","Gather 5", 56_5, 0),
)

UnderInverseTreasures: typing.List[LocationData] = (
LocationData("Under Inverse","Treasure 1", 56_1, "Treasure"),
LocationData("Under Inverse","Treasure 2", 56_2, "Treasure"),
LocationData("Under Inverse","Treasure 3", 56_3, "Treasure"),
LocationData("Under Inverse","Treasure 4", 56_4, "Treasure"),
)
UnderInverseEnemies: typing.List[LocationData] = (
LocationData("Under Inverse","Nanovader", 153, "Enemy"),
LocationData("Under Inverse","Earth Golem", 158, "Enemy"),
LocationData("Under Inverse","Viral Earth Golem", 166, "Enemy"),
LocationData("Under Inverse","Aluna", 245, "Enemy"),
LocationData("Under Inverse","Viral Aluna", 252, "Enemy"),
LocationData("Under Inverse","Strange Person", 240, "Enemy"),
LocationData("Under Inverse","Self-Defense System ", 420, "Big Enemy"),
)