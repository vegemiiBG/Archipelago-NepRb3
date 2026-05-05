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
LocationData("Under Inverse","Dogone", 322, "Enemy"),
LocationData("Under Inverse","Blaze Boy", 214, "Enemy"),
LocationData("Under Inverse","Blaze Girl", 225, "Enemy"),
LocationData("Under Inverse","Blaze Golem", 163, "Enemy"),
LocationData("Under Inverse","Viral Blaze Golem", 171, "Enemy"),
LocationData("Under Inverse","Volcano Turtle", 443, "Big Enemy"),
)