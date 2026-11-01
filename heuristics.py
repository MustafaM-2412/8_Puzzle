def berechne_hamming(brett, goal) -> int:
    """
    Hammin distance ausrechnen -> für jeden wert der auf der Falschen stelle steht geht der counting +1 (ausser 0)
    """
    h = 0
    for i in range(0, len(brett)):
        #null ignorieren
        if brett[i] == 0:
            continue
        if not brett[i] == goal[i]:
            h += 1
    return h

def berechne_manhattan(brett, goal) -> int:
    """
    Manhattan distance ausrechnen -> zählt für jeden wert wie viele schritte (zeile + spalte) er vom ziel weg ist (ausser 0)
    """
    h = 0
    for i in range(0, len(brett)):
        #null ignorieren
        if brett[i] == 0:
            continue
        ziel_i = goal.index(brett[i])
        zeile_aktuell = i // 3
        spalte_aktuell = i % 3
        zeile_ziel = ziel_i // 3
        spalte_ziel = ziel_i % 3
        h = h + abs(zeile_aktuell - zeile_ziel) + abs(spalte_aktuell - spalte_ziel)
    return h