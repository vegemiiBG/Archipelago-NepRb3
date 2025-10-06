from dataclasses import dataclass

from Options import Choice, DefaultOnToggle, PerGameCommonOptions, StartInventoryPool, Toggle

@dataclass
class NepRb3Options(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool

    # DeathLink is always on. Always.
    # death_link: DeathLink
