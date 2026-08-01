from BaseClasses import List,Dict
from ..names.DungeonIDs import all_dungeons
from ..names.DungeonNames import *
from ..names.ItemNames import *
class RegionData:
    def __init__(self,name:str,power:int, defense:int, level:int,partnerRegion:str = None,changeDungeon:str = None,bigChangeDungeon:str = None,):
        self.name = name
        self.power = power
        self.defense = defense
        self.level = level
        self.partnerDungeon = partnerRegion
        self.changeDungeon = changeDungeon
        self.bigChangeDungeon = bigChangeDungeon 

all_dungeon_regions:List[RegionData] = [
    #planeptune
    RegionData(jet_set_range,                       250,    1,   0,    jet_set_peak                    ,changeDungeon=dungeon_change_jet_set_range_plan),
    RegionData(otori_forest,                        1,      0,  000                                    ),
    RegionData(zeca_ruins_no1,                      250,    0,  000                                    ),
    RegionData(zeca_ruins_no2,                      500,    1,  10                                     ),
    RegionData(haneda_mountain_range,               2750,   2,  50,    haneda_mountain_peak            ),
    RegionData(haneda_mountain_peak,                2750,   2,  50,    haneda_mountain_range           ),
    RegionData(otori_cave,                          2300,   2,  50                                     ),
    RegionData(powerlevel_island,                   3050,   3,  60,    powerlevel_island_interior      ,changeDungeon=dungeon_change_powerlevel_island_plan,bigChangeDungeon=big_dungeon_change_powerlevel_island_plan),
    RegionData(powerlevel_island_interior,          3050,   3,  60,    powerlevel_island               ,changeDungeon=dungeon_change_powerlevel_island_plan,bigChangeDungeon=big_dungeon_change_powerlevel_island_plan),
    RegionData(digital_future_land,                 5050,   4,  90,    digital_future_depths           ),
    RegionData(digital_future_depths,               5050,   4,  90,    digital_future_land             ),

    #laststation
    RegionData(jet_set_peak,                        250,    1,  000,    jet_set_range                  ),
    RegionData(rud_arms_sewer_n,                    950,    1,  20,    rud_arms_sewer_s                ),
    RegionData(vida_dimension,                      3050,   4,  70                                     ),
    RegionData(gigo_main_entrance,                  900,    1,  30,    gigo_depths                     ),
    RegionData(gigo_depths,                         900,    1,  30,    gigo_main_entrance              ),
    RegionData(anonydeaths_lab,                     4550,   4,  50,    anonydeaths_lab_depths          ),
    RegionData(anonydeaths_lab_depths,              4550,   4,  50,    anonydeaths_lab                 ),
    RegionData(soni_wetlands,                       400,    1,  20                                     ),
    RegionData(wanderers_cave,                      400,    1,  10,    wanderers_cave_depths           ),
    RegionData(wanderers_cave_depths,               450,    1,  10,    wanderers_cave                  ),
    RegionData(kuzarat_facility_1,                  400,    1,  10,    kuzarat_facility_2              ),
    RegionData(kuzarat_facility_2,                  450,    1,  10,    kuzarat_facility_1              ),
    RegionData(bandicrash,                          400,    1,  10                                     ),
    RegionData(national_factory,                    1000,   2,  40                                     ),
    RegionData(ps_dimension,                        1300,   2,  40                                     ),

    #lowee
    RegionData(rud_arms_sewer_s,                    950,    1,  20,    rud_arms_sewer_n                ),
    RegionData(ario_plateau,                        3530,   2,  50                                     ),
    RegionData(castle_chambers,                     350,    1,  20                                     ),
    RegionData(lowee_castle_exterior,               300,    1,  20,    lowee_castle_interior           ),
    RegionData(lowee_castle_interior,               300,    1,  20,    lowee_castle_exterior           ),
    RegionData(lowee_castle_northern_space,         3500,   4,  70,    lowee_castle_southern_space     ),
    RegionData(lowee_castle_southern_space,         2550,   3,  50,    lowee_castle_northern_space     ),
    RegionData(luji_plateau,                        1250,   2,  50                                     ),
    RegionData(metroid_shelter,                     1350,   2,  40,    metroid_shelter_depths          ),
    RegionData(metroid_shelter_depths,              600,    2,  40,    metroid_shelter                 ),
    RegionData(reload_grasslands,                   1100,   2,  20                                     ),
    RegionData(underground_cave,                    350,    1,  20,    castle_chambers                 ),
    RegionData(mines,                               1100,   3,  40                                     ),

    #leanbox
    RegionData(halo_forest,                         350,    1,  30                                     ),
    RegionData(zega_forest,                         650,    2,  40                                     ),
    RegionData(em_es_magma_cave,                    4250,   4,  70,    em_es_magma_cave_depths         ),
    RegionData(em_es_magma_cave_depths,             4250,   4,  70,    em_es_magma_cave                ),
    RegionData(kobaba_ruins,                        3145,   4,  50                                     ),
    RegionData(nekutoki_forest,                     3150,   4,  50                                     ),
    
    #pc continent
    RegionData(adaldik_forest,                      1450,   2,  30                                     ),
    RegionData(pii_shii_game_factory,               5050,   3,  60                                     ),
    RegionData(do_temple,                           4675,   4,  90                                     ),

    #hello
    RegionData(keraga_dimension,                    3750,   4,  50                                     ),
    RegionData(suaho_mountain_range,                1750,   2,  30,    suaho_mountain_peak             ),
    RegionData(suaho_mountain_peak,                 1750,   2,  30,    suaho_mountain_range            ),
    RegionData(so_shal_forest,                      3250,   4,  70                                     ),

    #eden
    RegionData(magma_cave,                          2750,   2,  50,    magma_cave_depths               ),
    RegionData(magma_cave_depths,                   2750,   2,  50,    magma_cave                      ),
    RegionData(extradimensional_space,              2750,   3,  60                                     ),
    RegionData(graphic_pass,                        3750,   3,  60,    graphic_pass_peak               ),
    RegionData(graphic_pass_peak,                   3750,   3,  60,    graphic_pass                    ),
    RegionData(duo_r_ruins,                         3750,   4,  80                                     ),
    RegionData(koagura_plateau,                     4750,   4,  90                                     ),
    
    #hyperdimension
    RegionData(city_center,                         5080,   5,  60                                     ),
    RegionData(virtua_forest_safe_zone,             0,      0,  000                                    ),
    RegionData(station_area,                        0,      0,  000                                    ),
    RegionData(virtua_forest,                       3650,   3,  60,    virtua_forest_depths            ),
    RegionData(virtua_forest_depths,                3650,   3,  60,    virtua_forest                   ),
    RegionData(under_inverse,                       5550,   4,  90,    under_inverse_depths            ),
    RegionData(under_inverse_depths,                5550,   4,  90,    under_inverse                   ),
    RegionData(planeptune_alley,                    9000,   5,  90                                     ),
    #RegionData(32650,0,0,planeptune_alley),treasure ruins
    
    #RegionData(,0,0,),
]

all_dungeon_regions_dict ={ k.name:k for k in all_dungeon_regions}
