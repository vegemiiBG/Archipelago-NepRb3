from typing import NamedTuple, Optional

from BaseClasses import Item, ItemClassification


class NepRb3Item(Item):
    game = "Hyperdimension Neptunia Re;Birth3 V GENERATION"


class NepRb3ItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler


item_data: dict[str, NepRb3ItemData] = {
    # fmt: off
    "Herb":  NepRb3ItemData(69696969, ItemClassification.progression),
    "Dogoo Jelly":  NepRb3ItemData(69696968, ItemClassification.progression),
    "Coin Fragment": NepRb3ItemData(69696967),
    "Lizard Scale": NepRb3ItemData(69696966),
    "Yellow Petal": NepRb3ItemData(69696965),
    "Sunflowery Seed": NepRb3ItemData(69696964)
    # fmt: on
}
