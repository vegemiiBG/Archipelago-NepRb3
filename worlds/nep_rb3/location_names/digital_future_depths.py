import typing
from ..LocationData import LocationData

DigitalFutureDepths: typing.List[LocationData] = (
LocationData("Digital Future Depths","Gather 1", 68_1, 0),
LocationData("Digital Future Depths","Gather 2", 68_2, 0),
LocationData("Digital Future Depths","Gather 3", 68_3, 0),
LocationData("Digital Future Depths","Gather 4", 68_4, 0),
LocationData("Digital Future Depths","Gather 5", 68_5, 0),
)

DigitalFutureDepthsTreasures: typing.List[LocationData] = (
LocationData("Digital Future Depths","Treasure 1", 68_1, "Treasure"),
LocationData("Digital Future Depths","Treasure 2", 68_2, "Treasure"),
LocationData("Digital Future Depths","Treasure 3", 68_3, "Treasure"),
LocationData("Digital Future Depths","Treasure 4", 68_4, "Treasure"),
)
#DigitalFutureDepthsEnemies: typing.List[LocationData] = (                     \\ Same Exact Enemies as Depths
#LocationData("Digital Future Depths","Shampuru Loner", 153, "Enemy"),
#LocationData("Digital Future Depths","Dokidoki Sister", 158, "Enemy"),
#LocationData("Digital Future Depths","NP-02v", 166, "Enemy"),
#LocationData("Digital Future Depths","Bug Butterfly", 245, "Enemy"),
#LocationData("Digital Future Depths","Wolf Blaze", 420, "Big Enemy"),
#)