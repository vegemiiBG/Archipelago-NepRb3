def hasNeptune(state, player):
    return state.has("Character - Neptune", player)

def hasNepgear(state, player):
    return state.has("Character - Nepgear", player)

def hasVert(state, player):
    return state.has("Character - Vert", player)

def hasBlanc(state, player):
    return state.has("Character - Blanc", player)

def hasNoire(state, player):
    return state.has("Character - Noire", player)

def hasPlutia(state, player):
    return state.has("Character - Plutia", player)

def hasPeashy(state, player):
    return state.has("Character - Peashy", player)

def hasRom(state, player):
    return state.has("Character - Rom", player)

def hasRam(state, player):
    return state.has("Character - Ram", player)

def hasUni(state, player):
    return state.has("Character - Uni", player)

def ch3Armor(state, player):
    return state.has("Progressive Armor", player, 1)

def ch6Armor(state, player):
    return state.has("Progressive Armor", player, 2)

def ch9Armor(state, player):
    return state.has("Progressive Armor", player, 3)

#This tier is finally better than base candidate armor
def charArmor(state, player):
    return state.has("Progressive Armor", player, 4)

def eventArmor(state, player):
    return state.has("Progressive Armor", player, 5)

def postgameArmor(state, player):
    return state.has("Progressive Armor", player, 6)

def neptuneT1(state, player):
    return state.has("Neptune - Progressive Weapons", player, 1)

def neptuneT2(state, player):
    return state.has("Neptune - Progressive Weapons", player, 2)

def neptuneT3(state, player):
    return state.has("Neptune - Progressive Weapons", player, 3)
#This tier is better than base candidate weapons
def neptuneT4(state, player):
    return state.has("Neptune - Progressive Weapons", player, 4)

def neptuneT5(state, player):
    return state.has("Neptune - Progressive Weapons", player, 5)

def neptuneT6(state, player):
    return state.has("Neptune - Progressive Weapons", player, 6)

def noireT1(state, player):
    return state.has("Noire - Progressive Weapons", player, 1)

def noireT2(state, player):
    return state.has("Noire - Progressive Weapons", player, 2)

def noireT3(state, player):
    return state.has("Noire - Progressive Weapons", player, 3)

def noireT4(state, player):
    return state.has("Noire - Progressive Weapons", player, 4)

def noireT5(state, player):
    return state.has("Noire - Progressive Weapons", player, 5)

def plutiaT1(state, player):
    return state.has("Plutia - Progressive Weapons", player, 1)

def plutiaT2(state, player):
    return state.has("Plutia - Progressive Weapons", player, 2)

def plutiaT3(state, player):
    return state.has("Plutia - Progressive Weapons", player, 3)

def plutiaT4(state, player):
    return state.has("Plutia - Progressive Weapons", player, 4)

def plutiaT5(state, player):
    return state.has("Plutia - Progressive Weapons", player, 5)

def plutiaT6(state, player):
    return state.has("Plutia - Progressive Weapons", player, 6)



def VirtuaForestSafeZone(state, player):
    return True

def StationArea(state, player):
    return True

def ZecaRuinsNo1(state, player):
    viable_members = 0
    if hasRam(state, player):
        return True

    if hasUni(state, player):
        return True

    if hasRom(state, player)
        return True

    if hasPeashy(state, player):
        return True

    if hasBlanc(state, player):
        return True

    if hasVert(state, player):
        return True

    if hasNepgear(state, player):
        return True

    if hasNeptune(state, player):
        if neptuneT1(state, player) and ch3Armor(state, player):
            viable_members += 1

    if hasNoire(state, player):
        if noireT1(state, player) and ch3Armor(state, player):
            viable_members += 1

    if hasPlutia(state, player):
        if plutiaT1(state, player) and ch3Armor(state, player):
            viable_members += 1

    if viable_members >= 2:
        return True