from dataclasses import dataclass

from Options import Choice, DefaultOnToggle, PerGameCommonOptions, StartInventoryPool, Toggle

class PostGameRequired(DefaultOnToggle):
    """If enabled, Post Game Dungeons may hold key progression items."""
    display_name = "Post Game Required"



@dataclass
class NepRb3Options(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    post_game_required: PostGameRequired

    # DeathLink is always on. Always.
    # death_link: DeathLink
