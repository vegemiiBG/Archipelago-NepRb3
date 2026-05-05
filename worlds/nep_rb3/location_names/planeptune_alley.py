import typing
from ..LocationData import LocationData

PlaneptuneAlley: typing.List[LocationData] = (
LocationData("Planeptune Alley","Gather 1", 58_1, 0),
LocationData("Planeptune Alley","Gather 2", 58_2, 0),
LocationData("Planeptune Alley","Gather 3", 58_3, 0),
LocationData("Planeptune Alley","Gather 4", 58_4, 0),
LocationData("Planeptune Alley","Gather 5", 58_5, 0),
)

PlaneptuneAlleyTreasures: typing.List[LocationData] = (
LocationData("Planeptune Alley","Treasure 1", 58_1, "Treasure"),
LocationData("Planeptune Alley","Treasure 2", 58_2, "Treasure"),
LocationData("Planeptune Alley","Treasure 3", 58_3, "Treasure"),
LocationData("Planeptune Alley","Treasure 4", 58_4, "Treasure"),
)
PlaneptuneAlleyEnemies: typing.List[LocationData] = (
LocationData("Planeptune Alley","Nanovader", 153, "Enemy"),
LocationData("Planeptune Alley","Earth Golem", 158, "Enemy"),
LocationData("Planeptune Alley","Viral Earth Golem", 166, "Enemy"),
LocationData("Planeptune Alley","Aluna", 245, "Enemy"),
LocationData("Planeptune Alley","Viral Aluna", 252, "Enemy"),
LocationData("Planeptune Alley","Strange Person", 240, "Enemy"),
LocationData("Planeptune Alley","Self-Defense System ", 420, "Big Enemy"),



)