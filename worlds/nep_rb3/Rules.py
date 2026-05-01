from worlds.generic.Rules import set_rule, forbid_items_for_player
from . import NepRb3World



def set_location_rules(world: "NepRb3World") -> None:
    player = world.player

    set_rule(world.multiworld.get_location("Dungeon Unlock - City Center", player), lambda state: state.has("dungeon_unlock_34", player))