

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule
from .names import DungeonNames, CharacterNames, progressiveGear, DungeonIDs, ItemNames
from BaseClasses import CollectionState
from .items import apDungeonItemBaseID, item_id_to_name, NepRb3ItemData
if TYPE_CHECKING:
    from . import NepRb3World

def hasDungeonUnlocked(state:CollectionState,player:int,DungeonName:str):
    id = DungeonIDs.all_dungeons[DungeonName]
    return state.has(item_id_to_name[id+apDungeonItemBaseID],player)

#def hasJumpingStar(State:CollectionState,player:int,ItemNames:str): Dont know how to properly define this yet
    id = ItemNames.all_dungeons[ItemNames]
    return state.has(item_id_to_name[id+608],player)

## Should have logic reflect as glitched so players arent outright thinking they can't even obtain treasures or gathers in dungeons like DFL or other postgame dungeons


def StartingCharactersStrength(ProgressiveTier:int):   # Neptune, Plutia, Noire
    if ProgressiveTier == 1:
        return 400
    elif ProgressiveTier == 2:
        return 750
    elif ProgressiveTier == 3:
        return 1050
    elif ProgressiveTier == 4:
        return 1450
    elif ProgressiveTier == 5:
        return 2150
    elif ProgressiveTier == 6:
        return 2350
    return 50

def MidCharactersStrength(ProgressiveTier:int):     # Blanc, Vert, Nepgear
    if ProgressiveTier == 1:
        return 550
    elif ProgressiveTier == 2:
        return 900
    elif ProgressiveTier == 3:
        return 1150
    elif ProgressiveTier == 4:
        return 1500
    elif ProgressiveTier == 5:
        return 2200
    return 275


def freakingPeashyStrength(ProgressiveTier:int): #Peashy
    if ProgressiveTier == 1:
        return 1200
    elif ProgressiveTier == 2:
        return 1450
    elif ProgressiveTier == 3:
        return 1800
    elif ProgressiveTier == 4:
        return 1800
    elif ProgressiveTier == 5:
        return 2200
    return 1050

def HyperCandidatesStrength(ProgressiveTier:int): # Uni, Rom, Ram
    if ProgressiveTier == 1:
        return 1300
    elif ProgressiveTier == 2:
        return 1450
    elif ProgressiveTier == 3:
        return 2100
    elif ProgressiveTier == 4:
        return 2350
    return 1150

def ArmorStrength(ArmorTier:int, combatTeam:int):
    if ArmorTier == 1:
        return combatTeam * 1.3
    elif ArmorTier == 2:
        return combatTeam * 1.9
    elif ArmorTier == 3:
        return combatTeam * 2.6
    elif ArmorTier == 4:
        return combatTeam * 3.2
    elif ArmorTier == 5:
        return combatTeam * 4
    elif ArmorTier == 6:
        return combatTeam * 5
    return combatTeam * 1



def checkDungeonRequirements (Difficulty: int, state:CollectionState, player:int):
    playerStrength = 0
    unlockedCharacters = 0
    characterStrength = []
    if state.has(CharacterNames.neptune, player):
        unlockedCharacters +=1
        characterStrength.append(StartingCharactersStrength(state.count(progressiveGear.neptune_progressive_gear,player)))
    if state.has(CharacterNames.nepgear, player):
        unlockedCharacters +=1
        characterStrength.append(MidCharactersStrength(state.count(progressiveGear.nepgear_progressive_gear,player)))
    if state.has(CharacterNames.plutia, player):
        unlockedCharacters +=1
        characterStrength.append(StartingCharactersStrength(state.count(progressiveGear.plutia_progressive_gear,player)))
    if state.has(CharacterNames.noire, player):
        unlockedCharacters +=1
        characterStrength.append(StartingCharactersStrength(state.count(progressiveGear.noire_progressive_gear,player)))
    if state.has(CharacterNames.blanc,player):
        unlockedCharacters +=1
        characterStrength.append(MidCharactersStrength(state.count(progressiveGear.blanc_progressive_gear,player)))
    if state.has(CharacterNames.vert,player):
        unlockedCharacters +=1
        characterStrength.append(MidCharactersStrength(state.count(progressiveGear.vert_progressive_gear,player)))
    if state.has(CharacterNames.peashy,player):
        unlockedCharacters +=1
        characterStrength.append(freakingPeashyStrength(state.count(progressiveGear.peashy_progressive_gear,player)))
    if state.has(CharacterNames.uni,player):
        unlockedCharacters +=1
        characterStrength.append(HyperCandidatesStrength(state.count(progressiveGear.uni_progressive_gear,player)))
    if state.has(CharacterNames.rom,player):
        unlockedCharacters +=1
        characterStrength.append(HyperCandidatesStrength(state.count(progressiveGear.rom_progressive_gear,player)))
    if state.has(CharacterNames.ram,player):
        unlockedCharacters +=1
        characterStrength.append(HyperCandidatesStrength(state.count(progressiveGear.ram_progressive_gear,player)))

    if unlockedCharacters > 4:
        unlockedCharacters = 4
        characterStrength.sort(reverse=True)

    for i in range(0,4):
        if i >= len(characterStrength): break
        playerStrength += characterStrength[i]
    playerStrength +=ArmorStrength(state.count(progressiveGear.progressive_armor,player),unlockedCharacters)
    
    return playerStrength >= Difficulty


def set_all_planeptune_dungeons(world: "NepRb3World") -> None:
    planeptune_to_lastation = world.get_entrance(DungeonNames.jet_set_range)
    planeptune_otori_forest = world.get_entrance(DungeonNames.otori_forest)
    planeptune_zeca_ruins1 = world.get_entrance(DungeonNames.zeca_ruins_no1)
    planeptune_zeca_ruins2 = world.get_entrance(DungeonNames.zeca_ruins_no2)
    planeptune_haneda_mountain_range = world.get_entrance(DungeonNames.haneda_mountain_range)
    #planeptune_haneda_mountain_peak = world.get_entrance(DungeonNames.haneda_mountain_peak)
    planeptune_otori_cave = world.get_entrance(DungeonNames.otori_cave)
    planeptune_powerlevel_island = world.get_entrance(DungeonNames.powerlevel_island)
    planeptune_powerlevel_island_interior = world.get_entrance(DungeonNames.powerlevel_island_interior)
    planeptune_digital_future_land = world.get_entrance(DungeonNames.digital_future_land)
    planeptune_digital_future_depths = world.get_entrance(DungeonNames.digital_future_depths)

    world.set_rule(planeptune_otori_forest, lambda state: checkDungeonRequirements(1, state, world.player)                   and hasDungeonUnlocked(state,world.player,DungeonNames.otori_forest))
    world.set_rule(planeptune_zeca_ruins1, lambda state: checkDungeonRequirements(1, state, world.player)                    and hasDungeonUnlocked(state,world.player,DungeonNames.zeca_ruins_no1))
    world.set_rule(planeptune_to_lastation, lambda state:checkDungeonRequirements(250,state,world.player)                    and hasDungeonUnlocked(state,world.player,DungeonNames.jet_set_range))
    world.set_rule(planeptune_zeca_ruins2, lambda state: checkDungeonRequirements(500, state, world.player)                  and hasDungeonUnlocked(state,world.player,DungeonNames.zeca_ruins_no2))
    world.set_rule(planeptune_haneda_mountain_range, lambda state: checkDungeonRequirements(1350, state, world.player)       and hasDungeonUnlocked(state,world.player,DungeonNames.haneda_mountain_range))
    #world.set_rule(planeptune_haneda_mountain_peak, lambda state: checkDungeonRequirements(1050, state, world.player)        and hasDungeonUnlocked(state,world.player,DungeonNames.haneda_mountain_range))
    world.set_rule(planeptune_otori_cave, lambda state: checkDungeonRequirements(1300, state, world.player)                  and hasDungeonUnlocked(state,world.player,DungeonNames.otori_cave))
    world.set_rule(planeptune_powerlevel_island, lambda state: checkDungeonRequirements(3050, state, world.player)           and hasDungeonUnlocked(state,world.player,DungeonNames.powerlevel_island))
    #world.set_rule(planeptune_powerlevel_island_interior, lambda state: checkDungeonRequirements(3050, state, world.player)  and hasDungeonUnlocked(state,world.player,DungeonNames.powerlevel_island_interior))
    world.set_rule(planeptune_digital_future_land,lambda state:checkDungeonRequirements(8050,state,world.player)             and hasDungeonUnlocked(state,world.player,DungeonNames.digital_future_land))
    #world.set_rule(planeptune_digital_future_depths,lambda state:checkDungeonRequirements(2500,state,world.player)          and hasDungeonUnlocked(state,world.player,DungeonNames.digital_future_depths))
##
def set_all_lastation_dungeons(world: "NepRb3World") -> None:
    #lastation_to_planeptune = world.get_entrance(DungeonNames.jet_set_peak)
    lastation_to_lowee = world.get_entrance(DungeonNames.rud_arms_sewer_n)
    lastation_vida_dimension = world.get_entrance(DungeonNames.vida_dimension)
    lastation_gigo = world.get_entrance(DungeonNames.gigo_main_entrance)
    lastation_gigo_depths = world.get_entrance(DungeonNames.gigo_depths)
    lastation_anonydeath_lab = world.get_entrance(DungeonNames.anonydeaths_lab)
    lastation_anonydeath_depths = world.get_entrance(DungeonNames.anonydeaths_lab_depths)
    lastation_soni_wetlands = world.get_entrance(DungeonNames.soni_wetlands)
    lastation_wanderers_cave = world.get_entrance(DungeonNames.wanderers_cave)
    lastation_wanderers_depths = world.get_entrance(DungeonNames.wanderers_cave_depths)
    lastation_kuzarat = world.get_entrance(DungeonNames.kuzarat_facility_1)
    lastation_kuzarat_inner = world.get_entrance(DungeonNames.kuzarat_facility_2)
    lastation_bandicrash = world.get_entrance(DungeonNames.bandicrash)
    lastation_national_factory = world.get_entrance(DungeonNames.national_factory)
    lastation_ps_dimension = world.get_entrance(DungeonNames.ps_dimension)

    #world.set_rule(lastation_to_planeptune, lambda state: checkDungeonRequirements(150, state, world.player)                and hasDungeonUnlocked(state,world.player,DungeonNames.jet_set_peak))
    #world.set_rule(lastation_to_lowee, lambda state: checkDungeonRequirements(250, state, world.player)                     and hasDungeonUnlocked(state,world.player,DungeonNames.rud_arms_sewer_n))
    world.set_rule(lastation_vida_dimension, lambda state: checkDungeonRequirements(2050, state, world.player)             and hasDungeonUnlocked(state,world.player,DungeonNames.vida_dimension))
    world.set_rule(lastation_gigo, lambda state: checkDungeonRequirements(900, state, world.player)                        and hasDungeonUnlocked(state,world.player,DungeonNames.gigo_main_entrance))
    #world.set_rule(lastation_gigo_depths, lambda state: checkDungeonRequirements(350, state, world.player)                  and hasDungeonUnlocked(state,world.player,DungeonNames.gigo_depths))
    world.set_rule(lastation_anonydeath_lab, lambda state: checkDungeonRequirements(1950, state, world.player)             and hasDungeonUnlocked(state,world.player,DungeonNames.anonydeaths_lab))
    #world.set_rule(lastation_anonydeath_depths, lambda state: checkDungeonRequirements(650, state, world.player)            and hasDungeonUnlocked(state,world.player,DungeonNames.anonydeaths_lab_depths))
    world.set_rule(lastation_soni_wetlands, lambda state: checkDungeonRequirements(600, state, world.player)               and hasDungeonUnlocked(state,world.player,DungeonNames.soni_wetlands))
    world.set_rule(lastation_wanderers_cave, lambda state: checkDungeonRequirements(400, state, world.player)              and hasDungeonUnlocked(state,world.player,DungeonNames.wanderers_cave))
    #world.set_rule(lastation_wanderers_depths, lambda state: checkDungeonRequirements(250, state, world.player)             and hasDungeonUnlocked(state,world.player,DungeonNames.wanderers_cave_depths))
    world.set_rule(lastation_kuzarat, lambda state: checkDungeonRequirements(600, state, world.player)                     and hasDungeonUnlocked(state,world.player,DungeonNames.kuzarat_facility_1))
    #world.set_rule(lastation_kuzarat_inner, lambda state: checkDungeonRequirements(250, state, world.player)                and hasDungeonUnlocked(state,world.player,DungeonNames.kuzarat_facility_2))
    world.set_rule(lastation_bandicrash, lambda state: checkDungeonRequirements(750, state, world.player)                  and hasDungeonUnlocked(state,world.player,DungeonNames.bandicrash))
    world.set_rule(lastation_national_factory, lambda state: checkDungeonRequirements(1000, state, world.player)           and hasDungeonUnlocked(state,world.player,DungeonNames.national_factory))
    world.set_rule(lastation_ps_dimension, lambda state: checkDungeonRequirements(1300, state, world.player)               and hasDungeonUnlocked(state,world.player,DungeonNames.ps_dimension))
                   
##
def set_all_lowee_dungeons(world: "NepRb3World") -> None:
    lowee_to_lastation = world.get_entrance(DungeonNames.rud_arms_sewer_s)
    lowee_ario_plateau = world.get_entrance(DungeonNames.ario_plateau)
    lowee_castle_chambers = world.get_entrance(DungeonNames.castle_chambers)
    lowee_castle_exterior = world.get_entrance(DungeonNames.lowee_castle_exterior)
    lowee_castle_interior = world.get_entrance(DungeonNames.lowee_castle_interior)
    lowee_castle_northern_space = world.get_entrance(DungeonNames.lowee_castle_northern_space)
    lowee_castle_southern_space = world.get_entrance(DungeonNames.lowee_castle_southern_space)
    lowee_luji_plateau = world.get_entrance(DungeonNames.luji_plateau)
    lowee_metroid_shelter = world.get_entrance(DungeonNames.metroid_shelter)
    lowee_metroid_shelter_depths = world.get_entrance(DungeonNames.metroid_shelter_depths)
    lowee_reload_grasslands = world.get_entrance(DungeonNames.reload_grasslands)
    lowee_underground_cave = world.get_entrance(DungeonNames.underground_cave)
    lowee_mines = world.get_entrance(DungeonNames.mines)

    world.set_rule(lowee_to_lastation, lambda state: checkDungeonRequirements(650, state, world.player)             and hasDungeonUnlocked(state,world.player,DungeonNames.rud_arms_sewer_s))
    world.set_rule(lowee_ario_plateau, lambda state: checkDungeonRequirements(1530, state, world.player)             and hasDungeonUnlocked(state,world.player,DungeonNames.ario_plateau))
    #world.set_rule(lowee_castle_chambers, lambda state: checkDungeonRequirements(350, state, world.player)          and hasDungeonUnlocked(state,world.player,DungeonNames.castle_chambers))
    world.set_rule(lowee_castle_exterior, lambda state: checkDungeonRequirements(300, state, world.player)          and hasDungeonUnlocked(state,world.player,DungeonNames.lowee_castle_exterior))
    #world.set_rule(lowee_castle_interior, lambda state: checkDungeonRequirements(300, state, world.player)          and hasDungeonUnlocked(state,world.player,DungeonNames.lowee_castle_interior))
    world.set_rule(lowee_castle_northern_space, lambda state: checkDungeonRequirements(3500, state, world.player)    and hasDungeonUnlocked(state,world.player,DungeonNames.lowee_castle_northern_space))
    #world.set_rule(lowee_castle_southern_space, lambda state: checkDungeonRequirements(750, state, world.player)    and hasDungeonUnlocked(state,world.player,DungeonNames.lowee_castle_southern_space))
    world.set_rule(lowee_luji_plateau, lambda state: checkDungeonRequirements(1250, state, world.player)             and hasDungeonUnlocked(state,world.player,DungeonNames.luji_plateau))
    world.set_rule(lowee_metroid_shelter, lambda state: checkDungeonRequirements(1350, state, world.player)          and hasDungeonUnlocked(state,world.player,DungeonNames.metroid_shelter))
    #world.set_rule(lowee_metroid_shelter_depths, lambda state: checkDungeonRequirements(600, state, world.player)   and hasDungeonUnlocked(state,world.player,DungeonNames.metroid_shelter_depths))
    world.set_rule(lowee_reload_grasslands, lambda state: checkDungeonRequirements(1100, state, world.player)        and hasDungeonUnlocked(state,world.player,DungeonNames.reload_grasslands))
    #world.set_rule(lowee_underground_cave, lambda state: checkDungeonRequirements(350, state, world.player)         and hasDungeonUnlocked(state,world.player,DungeonNames.underground_cave))
    world.set_rule(lowee_mines, lambda state: checkDungeonRequirements(1100, state, world.player)                    and hasDungeonUnlocked(state,world.player,DungeonNames.mines))

##
def set_all_leanbox_dungeons(world: "NepRb3World") -> None:
    leanbox_halo_forest = world.get_entrance(DungeonNames.halo_forest)
    leanbox_zega_forest = world.get_entrance(DungeonNames.zega_forest)
    leanbox_emes_magma_cave = world.get_entrance(DungeonNames.em_es_magma_cave)
    leanbox_emes_magma_depths = world.get_entrance(DungeonNames.em_es_magma_cave_depths)
    leanbox_kobaba_ruins = world.get_entrance(DungeonNames.kobaba_ruins)
    leanbox_nekutoki_forest = world.get_entrance(DungeonNames.nekutoki_forest)

    world.set_rule(leanbox_halo_forest, lambda state: checkDungeonRequirements(350, state, world.player)            and hasDungeonUnlocked(state,world.player,DungeonNames.halo_forest))
    world.set_rule(leanbox_zega_forest, lambda state: checkDungeonRequirements(650, state, world.player)            and hasDungeonUnlocked(state,world.player,DungeonNames.zega_forest))
    world.set_rule(leanbox_emes_magma_cave, lambda state: checkDungeonRequirements(5500, state, world.player)       and hasDungeonUnlocked(state,world.player,DungeonNames.em_es_magma_cave))
    #world.set_rule(leanbox_emes_magma_depths, lambda state: checkDungeonRequirements(1500, state, world.player)     and hasDungeonUnlocked(state,world.player,DungeonNames.em_es_magma_cave_depths))
    world.set_rule(leanbox_kobaba_ruins, lambda state: checkDungeonRequirements(2145, state, world.player)           and hasDungeonUnlocked(state,world.player,DungeonNames.kobaba_ruins))
    world.set_rule(leanbox_nekutoki_forest, lambda state: checkDungeonRequirements(2150, state, world.player)        and hasDungeonUnlocked(state,world.player,DungeonNames.nekutoki_forest))

##
def set_all_pc_dungeons(world: "NepRb3World") -> None:
    pc_adaldik_forest = world.get_entrance(DungeonNames.adaldik_forest)
    pc_piishii = world.get_entrance(DungeonNames.pii_shii_game_factory)
    pc_do_temple = world.get_entrance(DungeonNames.do_temple)

    world.set_rule(pc_adaldik_forest, lambda state: checkDungeonRequirements(1450, state, world.player)              and hasDungeonUnlocked(state,world.player,DungeonNames.adaldik_forest))
    world.set_rule(pc_piishii, lambda state: checkDungeonRequirements(3250, state, world.player)                     and hasDungeonUnlocked(state,world.player,DungeonNames.pii_shii_game_factory))
    world.set_rule(pc_do_temple, lambda state: checkDungeonRequirements(4675, state, world.player)                   and hasDungeonUnlocked(state,world.player,DungeonNames.do_temple))

##
def set_all_hello_dungeons(world: "NepRb3World") -> None:
    hello_suaho_mountain_range = world.get_entrance(DungeonNames.suaho_mountain_range)
    hello_suaho_mountain_peak = world.get_entrance(DungeonNames.suaho_mountain_peak)
    hello_so_shal_forest = world.get_entrance(DungeonNames.so_shal_forest)
    hello_keraga_dimension = world.get_entrance(DungeonNames.keraga_dimension)

    world.set_rule(hello_keraga_dimension, lambda state: checkDungeonRequirements(2750, state, world.player)        and hasDungeonUnlocked(state,world.player,DungeonNames.keraga_dimension))
    world.set_rule(hello_suaho_mountain_range, lambda state: checkDungeonRequirements(2750, state, world.player)    and hasDungeonUnlocked(state,world.player,DungeonNames.suaho_mountain_range))
    #world.set_rule(hello_suaho_mountain_peak, lambda state: checkDungeonRequirements(2750, state, world.player)     and hasDungeonUnlocked(state,world.player,DungeonNames.suaho_mountain_peak))
    world.set_rule(hello_so_shal_forest, lambda state: checkDungeonRequirements(2750, state, world.player)          and hasDungeonUnlocked(state,world.player,DungeonNames.so_shal_forest))

##
def set_all_hyper_dungeons(world: "NepRb3World") -> None:
    hyper_city = world.get_entrance(DungeonNames.city_center)
    hyper_game_dimension = world.get_entrance(DungeonNames.game_dimension)
    hyper_virtua_forest_sz = world.get_entrance(DungeonNames.virtua_forest_safe_zone)
    hyper_station_area = world.get_entrance(DungeonNames.station_area)
    hyper_virtua_forest = world.get_entrance(DungeonNames.virtua_forest)
    hyper_city_virtua_depths = world.get_entrance(DungeonNames.virtua_forest_depths)
    hyper_under_inverse = world.get_entrance(DungeonNames.under_inverse)
    hyper_under_depths = world.get_entrance(DungeonNames.under_inverse_depths)
    hyper_planeptune_alley = world.get_entrance(DungeonNames.planeptune_alley)
    hyper_dlc_treasure_ruins = world.get_entrance(DungeonNames.treasure_ruins)

    world.set_rule(hyper_city, lambda state: checkDungeonRequirements(5080, state, world.player)                    and hasDungeonUnlocked(state,world.player,DungeonNames.city_center))
    #world.set_rule(hyper_game_dimension, lambda state: checkDungeonRequirements(1200, state, world.player)          and hasDungeonUnlocked(state,world.player,DungeonNames.game_dimension))
    world.set_rule(hyper_virtua_forest_sz, lambda state: checkDungeonRequirements(1, state, world.player)        and hasDungeonUnlocked(state,world.player,DungeonNames.virtua_forest_safe_zone))
    world.set_rule(hyper_station_area, lambda state: checkDungeonRequirements(1, state, world.player)            and hasDungeonUnlocked(state,world.player,DungeonNames.station_area))
    world.set_rule(hyper_virtua_forest, lambda state: checkDungeonRequirements(2250, state, world.player)           and hasDungeonUnlocked(state,world.player,DungeonNames.virtua_forest))
    #world.set_rule(hyper_city_virtua_depths, lambda state: checkDungeonRequirements(1200, state, world.player)      and hasDungeonUnlocked(state,world.player,DungeonNames.virtua_forest_depths))
    world.set_rule(hyper_under_inverse, lambda state: checkDungeonRequirements(5500, state, world.player)           and hasDungeonUnlocked(state,world.player,DungeonNames.under_inverse))
    #world.set_rule(hyper_under_depths, lambda state: checkDungeonRequirements(1200, state, world.player)            and hasDungeonUnlocked(state,world.player,DungeonNames.under_inverse_depths))
    world.set_rule(hyper_planeptune_alley, lambda state: checkDungeonRequirements(5305, state, world.player)        and hasDungeonUnlocked(state,world.player,DungeonNames.planeptune_alley))
    #world.set_rule(hyper_dlc_treasure_ruins, lambda state: checkDungeonRequirements(32650, state, world.player)     and hasDungeonUnlocked(state,world.player,DungeonNames.city_center))

##
