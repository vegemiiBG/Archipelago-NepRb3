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
    RegionData(jet_set_range,                       250,    0,  10,     jet_set_peak                    ),
    RegionData(otori_forest,                        1,      0,  000                                     ),
    RegionData(zeca_ruins_no1,                      250,    0,  000                                     ),
    RegionData(zeca_ruins_no2,                      500,    0,  20                                      ),
    RegionData(haneda_mountain_range,               3750,   0,  50,     haneda_mountain_peak            ),
    RegionData(haneda_mountain_peak,                3750,   0,  50,     haneda_mountain_range           ),
    RegionData(otori_cave,                          4300,   0,  60                                      ),
    RegionData(powerlevel_island,                   5050,   0,  70,     powerlevel_island_interior      ),
    RegionData(powerlevel_island_interior,          5050,   0,  70,     powerlevel_island               ),
    RegionData(digital_future_land,                 8050,   0,  90,     digital_future_depths           ),
    RegionData(digital_future_depths,               8050,   0,  90,     digital_future_land             ),

    #laststation
    RegionData(jet_set_peak,                        250,    0,  10,    jet_set_range                   ),
    RegionData(rud_arms_sewer_n,                    950,    0,  10,    rud_arms_sewer_s                ),
    RegionData(vida_dimension,                      5050,   0,  70                                     ),
    RegionData(gigo_main_entrance,                  900,    0,  30,    gigo_depths                     ),
    RegionData(gigo_depths,                         900,    0,  30,    gigo_main_entrance              ),
    RegionData(anonydeaths_lab,                     3950,   0,  60,    anonydeaths_lab_depths          ),
    RegionData(anonydeaths_lab_depths,              3650,   0,  60,    anonydeaths_lab                 ),
    RegionData(soni_wetlands,                       600,    0,  20                                     ),
    RegionData(wanderers_cave,                      400,    0,  10,    wanderers_cave_depths           ),
    RegionData(wanderers_cave_depths,               450,    0,  10,    wanderers_cave                  ),
    RegionData(kuzarat_facility_1,                  600,    0,  10,    kuzarat_facility_2              ),
    RegionData(kuzarat_facility_2,                  650,    0,  10,    kuzarat_facility_1              ),
    RegionData(bandicrash,                          600,    0,  10                                     ),
    RegionData(national_factory,                    1000,   0,  50                                     ),
    RegionData(ps_dimension,                        1300,   0,  60                                     ),

    #lowee
    RegionData(rud_arms_sewer_s,                    950,    0,  10,    rud_arms_sewer_n                ),
    RegionData(ario_plateau,                        3530,   0,  60                                     ),
    RegionData(castle_chambers,                     350,    0,  20                                     ),
    RegionData(lowee_castle_exterior,               300,    0,  20,    lowee_castle_interior           ),
    RegionData(lowee_castle_interior,               300,    0,  20,    lowee_castle_exterior           ),
    RegionData(lowee_castle_northern_space,         6500,   0,  80,    lowee_castle_southern_space     ),
    RegionData(lowee_castle_southern_space,         4550,   0,  50,    lowee_castle_northern_space     ),
    RegionData(luji_plateau,                        1250,   0,  40                                     ),
    RegionData(metroid_shelter,                     1350,   0,  50,    metroid_shelter_depths          ),
    RegionData(metroid_shelter_depths,              600,    0,  50,    metroid_shelter                 ),
    RegionData(reload_grasslands,                   1100,   0,  40                                     ),
    RegionData(underground_cave,                    350,    0,  20,    castle_chambers                 ),
    RegionData(mines,                               1100,   0,  40                                     ),

    #leanbox
    RegionData(halo_forest,                         350,    0,  30                                     ),
    RegionData(zega_forest,                         650,    0,  30                                     ),
    RegionData(em_es_magma_cave,                    5500,   0,  70,    em_es_magma_cave_depths         ),
    RegionData(em_es_magma_cave_depths,             5500,   0,  70,    em_es_magma_cave                ),
    RegionData(kobaba_ruins,                        3145,   0,  60                                     ),
    RegionData(nekutoki_forest,                     3150,   0,  60                                     ),
    
    #pc continent
    RegionData(adaldik_forest,                      1450,   0,  50                                     ),
    RegionData(pii_shii_game_factory,               5050,   0,  70                                     ),
    RegionData(do_temple,                           6675,   0,  80                                     ),

    #hello
    RegionData(keraga_dimension,                    3750,   0,  50                                     ),
    RegionData(suaho_mountain_range,                1750,   0,  30,    suaho_mountain_peak             ),
    RegionData(suaho_mountain_peak,                 1750,   0,  30,    suaho_mountain_range            ),
    RegionData(so_shal_forest,                      4250,   0,  80                                     ),

    #eden
    RegionData(magma_cave,                          4750,   0,  40,    magma_cave_depths               ),
    RegionData(magma_cave_depths,                   4750,   0,  40,    magma_cave                      ),
    RegionData(extradimensional_space,              4750,   0,  60                                     ),
    RegionData(graphic_pass,                        5750,   0,  70,    graphic_pass_peak               ),
    RegionData(graphic_pass_peak,                   5750,   0,  70,    graphic_pass                    ),
    RegionData(duo_r_ruins,                         5750,   0,  70                                     ),
    RegionData(koagura_plateau,                     6750,   0,  80                                     ),
    
    #hyperdimension
    RegionData(city_center,                         5080,   0,  80                                     ),
    RegionData(virtua_forest_safe_zone,             0,      0,  000                                    ),
    RegionData(station_area,                        0,      0,  000                                    ),
    RegionData(virtua_forest,                       5650,   0,  70,    virtua_forest_depths            ),
    RegionData(virtua_forest_depths,                5650,   0,  70,    virtua_forest                   ),
    RegionData(under_inverse,                       8550,   0,  100,   under_inverse_depths            ),
    RegionData(under_inverse_depths,                8550,   0,  100,   under_inverse                   ),
    RegionData(planeptune_alley,                    9000,   0,  100                                    ),
    #RegionData(32650,0,0,planeptune_alley),treasure ruins
    
    #RegionData(,0,0,),
]

all_dungeon_regions_dict ={ k.name:k for k in all_dungeon_regions}
