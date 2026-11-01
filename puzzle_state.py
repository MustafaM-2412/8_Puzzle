import random

def ist_loesbar(brett):
    """
    Prüft, ob das Puzzle überhaupt lösbar ist.
    Wenn Inversionen keine gerade Zahl ist, ist das Puzzle nicht Lösbar
    """
    inversionen = 0
    for i in range(0, len(brett)):
        for j in range(i + 1, len(brett)):
            # Die 0 wird ignoriert
            if brett[i] != 0 and brett[j] != 0:
                if brett[i] > brett[j]:
                    inversionen += 1
    return inversionen % 2 == 0

def zug_machen(brett) -> list:
    index0 = brett.index(0)
    test = []

    if index0 >= 3: test.append(index0 - 3)
    if index0 < 6: test.append(index0 + 3)
    if index0 % 3 != 2: test.append(index0 + 1)
    if index0 % 3 != 0: test.append(index0 - 1)

    neuer_zustand = []
    for tausch_index in test:
        neues_brett = list (brett)
        neues_brett[index0], neues_brett[tausch_index] = neues_brett[tausch_index], neues_brett[index0]
        neuer_zustand.append(tuple(neues_brett))
    return neuer_zustand

def zufalls_start(goal) -> tuple:
    while True:
        brett_zufall = list(goal)
        random.shuffle(brett_zufall)
        brett_zufall = tuple(brett_zufall)
        if ist_loesbar(brett_zufall) and brett_zufall != goal:
            return brett_zufall