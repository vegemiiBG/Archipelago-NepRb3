location_base_id = 7489397493
treasure_base_id = 2000000
enemy_base_id = 3000000

class LocationData:
    def __init__(self, name, id_, itemType):
        self.name = name
        self.itemType = itemType
        self.id = id_

        if itemType == "Treasure":
            self.id = self.id + treasure_base_id
