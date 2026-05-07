from BaseClasses import List,Dict
from ..names.DungeonIDs import all_dungeons
from ..names.DungeonNames import *

class RegionData:
    def __init__(self,name:str,power:int, defense:int, level:int,partnerRegion:str = None):
        self.name = name
        self.power = power
        self.defense = defense
        self.level = level
        self.partnerDungeon = partnerRegion 

all_dungeon_regions:List[RegionData] = [
    #planeptune
    RegionData(jet_set_range,                       1,      0,  000,    jet_set_peak                    ),
    RegionData(otori_forest,                        1,      0,  000                                     ),
    RegionData(zeca_ruins_no1,                      250,    0,  000                                     ),
    RegionData(zeca_ruins_no2,                      500,    0,  000                                     ),
    RegionData(haneda_mountain_range,               1350,   0,  000,    haneda_mountain_peak            ),
    RegionData(haneda_mountain_peak,                1050,   0,  000,    haneda_mountain_range           ),
    RegionData(otori_cave,                          1300,   0,  000                                     ),
    RegionData(powerlevel_island,                   3050,   0,  000,    powerlevel_island_interior      ),
    RegionData(powerlevel_island_interior,          3050,   0,  000,    powerlevel_island               ),
    RegionData(digital_future_land,                 8050,   0,  000,    digital_future_depths           ),
    RegionData(digital_future_depths,               8050,   0,  000,    digital_future_land             ),

    #laststation
    RegionData(jet_set_peak,                        150,    0,  000,    jet_set_range                   ),
    RegionData(rud_arms_sewer_n,                    250,    0,  000,    rud_arms_sewer_s                ),
    RegionData(vida_dimension,                      2050,   0,  000                                     ),
    RegionData(gigo_main_entrance,                  900,    0,  000,    gigo_depths                     ),
    RegionData(gigo_depths,                         350,    0,  000,    gigo_main_entrance              ),
    RegionData(anonydeaths_lab,                     1950,   0,  000,    anonydeaths_lab_depths          ),
    RegionData(anonydeaths_lab_depths,              650,    0,  000,    anonydeaths_lab                 ),
    RegionData(soni_wetlands,                       600,    0,  000                                     ),
    RegionData(wanderers_cave,                      400,    0,  000,    wanderers_cave_depths           ),
    RegionData(wanderers_cave_depths,               250,    0,  000,    wanderers_cave                  ),
    RegionData(kuzarat_facility_1,                  600,    0,  000,    kuzarat_facility_2              ),
    RegionData(kuzarat_facility_2,                  250,    0,  000,    kuzarat_facility_1              ),
    RegionData(bandicrash,                          750,    0,  000                                     ),
    RegionData(national_factory,                    1000,   0,  000                                     ),
    RegionData(ps_dimension,                        1300,   0,  000                                     ),

    #lowee
    RegionData(rud_arms_sewer_s,                    650,    0,  000,    rud_arms_sewer_n                ),
    RegionData(ario_plateau,                        1530,   0,  000                                     ),
    RegionData(castle_chambers,                     350,    0,  000                                     ),
    RegionData(lowee_castle_exterior,               300,    0,  000,    lowee_castle_interior           ),
    RegionData(lowee_castle_interior,               300,    0,  000,    lowee_castle_exterior           ),
    RegionData(lowee_castle_northern_space,         3500,   0,  000,    lowee_castle_southern_space     ),
    RegionData(lowee_castle_southern_space,         750,    0,  000,    lowee_castle_northern_space     ),
    RegionData(luji_plateau,                        1250,   0,  000                                     ),
    RegionData(metroid_shelter,                     1350,   0,  000,    metroid_shelter_depths          ),
    RegionData(metroid_shelter_depths,              600,    0,  000,    metroid_shelter                 ),
    RegionData(reload_grasslands,                   1100,   0,  000                                     ),
    RegionData(underground_cave,                    350,    0,  000,    castle_chambers                 ),
    RegionData(mines,                               1100,   0,  000                                     ),

    #leanbox
    RegionData(halo_forest,                         350,    0,  000                                     ),
    RegionData(zega_forest,                         650,    0,  000                                     ),
    RegionData(em_es_magma_cave,                    5500,   0,  000,    em_es_magma_cave_depths         ),
    RegionData(em_es_magma_cave_depths,             1500,   0,  000,    em_es_magma_cave                ),
    RegionData(kobaba_ruins,                        2145,   0,  000                                     ),
    RegionData(nekutoki_forest,                     2150,   0,  000                                     ),
    
    #pc continent
    RegionData(adaldik_forest,                      1450,   0,  000                                     ),
    RegionData(pii_shii_game_factory,               3250,   0,  000                                     ),
    RegionData(do_temple,                           4675,   0,  000                                     ),

    #hello
    RegionData(keraga_dimension,                    2750,   0,  000                                     ),
    RegionData(suaho_mountain_range,                2750,   0,  000,    suaho_mountain_peak             ),
    RegionData(suaho_mountain_peak,                 1200,   0,  000,    suaho_mountain_range            ),
    RegionData(so_shal_forest,                      2750,   0,  000                                     ),

    #eden
    RegionData(magma_cave,                          2750,   0,  000,    magma_cave_depths               ),
    RegionData(magma_cave_depths,                   2750,   0,  000,    magma_cave                      ),
    RegionData(extradimensional_space,              2750,   0,  000                                     ),
    RegionData(graphic_pass,                        2750,   0,  000,    graphic_pass_peak               ),
    RegionData(graphic_pass_peak,                   2750,   0,  000,    graphic_pass                    ),
    RegionData(duo_r_ruins,                         2750,   0,  000                                     ),
    RegionData(koagura_plateau,                     2750,   0,  000                                     ),
    
    #hyperdimension
    RegionData(city_center,                         5080,   0,  000                                     ),
    RegionData(virtua_forest_safe_zone,             0,      0,  000                                     ),
    RegionData(station_area,                        0,      0,  000                                     ),
    RegionData(virtua_forest,                       2250,   0,  000,    virtua_forest_depths            ),
    RegionData(virtua_forest_depths,                1200,   0,  000,    virtua_forest                   ),
    RegionData(under_inverse,                       5500,   0,  000,    under_inverse_depths            ),
    RegionData(under_inverse_depths,                4500,   0,  000,    under_inverse                   ),
    RegionData(planeptune_alley,                    3050,   0,  000                                     ),
    #RegionData(32650,0,0,planeptune_alley),treasure ruins
    
    #RegionData(,0,0,),
]

all_dungeon_regions_dict ={ k.name:k for k in all_dungeon_regions}
