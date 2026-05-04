import typing
from ..LocationData import LocationData

from .adaldik_forest import *
from .anonydeaths_lab import *
from .anonydeaths_lab_depths import *
from .ario_plateau import *
from .bandicrash import *
from .castle_chambers import *
from .city_center import *
from .digital_future_land import *
from .digital_future_depths import *
from .do_temple import *
from .duo_r_ruins import *
from .em_es_magma_cave import *
from .em_es_magma_cave_depths import *
from .extradimensional_space import *
from .gigo_depths import *
from .gigo_main_entrance import *
from .graphic_pass import *
from .graphic_pass_peak import *
from .halo_forest import *
from .haneda_mountain_range import *
from .haneda_mountain_peak import *
from .jet_set_range import *
from .jet_set_peak import *
from .keraga_dimension import *
from .koagura_plateau import *
from .kobaba_ruins import *
from .kuzarat_facility_1 import *
from .kuzarat_facility_2 import *
from .lowee_castle_exterior import *
from .lowee_castle_interior import *
from .lowee_castle_northern_space import *
from .lowee_castle_southern_space import *
from .luji_plateau import *
from .magma_cave import *
from .magma_cave_depths import *
from .metroid_shelter import *
from .metroid_shelter_depths import *
from .mines import *
from .national_factory import *
from .nekutoki_forest import *
from .otori_cave import *
from .otori_forest import *
from .pii_shii_game_factory import *
from .planeptune_alley import *
from .powerlevel_island import *
from .powerlevel_island_interior import *
from .ps_dimension import *
from .reload_grasslands import *
from .rud_arms_sewer_n import *
from .rud_arms_sewer_s import *
from .so_shal_forest import *
from .soni_wetlands import *
from .station_area import *
from .suaho_mountain_range import *
from .suaho_mountain_peak import *
from .under_inverse import *
from .under_inverse_depths import *
from .underground_cave import *
from .vida_dimension import *
from .virtua_forest import *
from .virtua_forest_depths import *
from .virtua_forest_safe_zone import *
from .wanderers_cave import *
from .wanderers_cave_depths import *
from .zeca_ruins_no1 import *
from .zeca_ruins_no2 import *
from .zega_forest import *

gathers: typing.List[LocationData] = (
    AdaldikForest,
    AnonydeathsLab,
    AnonydeathsLabDepths,
    ArioPlateau,
    Bandicrash,
    CastleChambers,
    CityCenter,
    DigitalFutureLand,
    DigitalFutureDepths,
    DoTemple,
    DuoRRuins,
    EmEsMagmaCave,
    EmEsMagmaCaveDepths,
    ExtradimensionalSpace,
    GigoMainEntrance,
    GigoDepths,
    GraphicPass,
    GraphicPassPeak,
    HaloForest,
    HanedaMountainRange,
    HanedaMountainPeak,
    JetSetRange,
    JetSetPeak,
    KeragaDimension,
    KoaguraPlateau,
    KobabaRuins,
    KuzaratFacility1,
    KuzaratFacility2,
    LoweeCastleExterior,
    LoweeCastleInterior,
    LoweeCastleNorthernSpace,
    LoweeCastleSouthernSpace,
    LujiPlateau,
    MagmaCave,
    MagmaCaveDepths,
    MetroidShelter,
    MetroidShelterDepths,
    Mines,
    NationalFactory,
    NekutokiForest,
    OtoriCave,
    OtoriForest,
    PiiShiiGameFactory,
    PlaneptuneAlley,
    PowerlevelIsland,
    PowerlevelIslandInterior,
    PSDimension,
    ReloadGrasslands,
    RudArmsSewerN,
    RudArmsSewerS,
    SoShalForest,
    SoniWetlands,
    StationArea,
    SuahoMountainRange,
    SuahoMountainPeak,
    UnderInverse,
    UnderInverseDepths,
    UndergroundCave,
    VidaDimension,
    VirtuaForest,
    VirtuaForestDepths,
    VirtuaForestSafeZone,
    WanderersCave,
    WanderersCaveDepths,
    ZecaRuinsNo1,
    ZecaRuinsNo2,
    ZegaForest,
)

treasures: typing.List[LocationData] = (
    AdaldikForestTreasures,
    AnonydeathsLabTreasures,
    AnonydeathsLabDepthsTreasures,
    ArioPlateauTreasures,
    BandicrashTreasures,
    CastleChambersTreasures,
    CityCenterTreasures,
    DigitalFutureLandTreasures,
    DigitalFutureDepthsTreasures,
    DoTempleTreasures,
    DuoRRuinsTreasures,
    EmEsMagmaCaveTreasures,
    EmEsMagmaCaveDepthsTreasures,
    ExtradimensionalSpaceTreasures,
    GigoMainEntranceTreasures,
    GigoDepthsTreasures,
    GraphicPassTreasures,
    GraphicPassPeakTreasures,
    HaloForestTreasures,
    HanedaMountainRangeTreasures,
    HanedaMountainPeakTreasures,
    JetSetRangeTreasures,
    JetSetPeakTreasures,
    KeragaDimensionTreasures,
    KoaguraPlateauTreasures,
    KobabaRuinsTreasures,
    KuzaratFacility1Treasures,
    KuzaratFacility2Treasures,
    LoweeCastleExteriorTreasures,
    LoweeCastleInteriorTreasures,
    LoweeCastleNorthernSpaceTreasures,
    LoweeCastleSouthernSpaceTreasures,
    LujiPlateauTreasures,
    MagmaCaveTreasures,
    MagmaCaveDepthsTreasures,
    MetroidShelterTreasures,
    MetroidShelterDepthsTreasures,
    MinesTreasures,
    NationalFactoryTreasures,
    NekutokiForestTreasures,
    OtoriCaveTreasures,
    OtoriForestTreasures,
    PiiShiiGameFactoryTreasures,
    PlaneptuneAlleyTreasures,
    PowerlevelIslandTreasures,
    PowerlevelIslandInteriorTreasures,
    PSDimensionTreasures,
    ReloadGrasslandsTreasures,
    RudArmsSewerNTreasures,
    RudArmsSewerSTreasures,
    SoShalForestTreasures,
    SoniWetlandsTreasures,
    StationAreaTreasures,
    SuahoMountainRangeTreasures,
    SuahoMountainPeakTreasures,
    UnderInverseTreasures,
    UnderInverseDepthsTreasures,
    UndergroundCaveTreasures,
    VidaDimensionTreasures,
    VirtuaForestTreasures,
    VirtuaForestDepthsTreasures,
    VirtuaForestSafeZoneTreasures,
    WanderersCaveTreasures,
    WanderersCaveDepthsTreasures,
    ZecaRuinsNo1Treasures,
    ZecaRuinsNo2Treasures,
    ZegaForestTreasures,
)

goalLocation: typing.List[LocationData] = (
    CityCenterGoal,
)
