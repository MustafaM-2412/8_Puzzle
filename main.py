import heapq as hq
import random
import time

goal = (1,2,3,4,5,6,7,8,0)

def berechne_hamming(brett, goal):
    """
    Hammin distance ausrechnen -> für jeden wert der auf der Falschen stelle steht geht der counting +1 (ausser 0)
    """
    h = 0
    for i in range(0, len(brett)):
        #null ignorieren
        if brett[i] == 0:
            continue
        if not brett[i] == goal[i]:
            h = h + 1
    return h

def berechne_manhattan(brett, goal):
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
                    inversionen = inversionen + 1

    if inversionen % 2 == 0:
        return True
    else:
        return False


start = (1,2,3,0,4,6,7,5,8)
g = 0
h = berechne_hamming(start, goal)
f = g + h

#offene leere liste die wir befüllen werden
open_list = []
closed_list = set() # merkt sich bereits besuchte bretter
start_paket = (f, g, start)
hq.heappush(open_list, start_paket)
print("Offene Liste:", open_list)


#hier will ich ein loop erstellen welches alle möglichen zahlen wechsel macht und dann F berechnet der niedrigste f soll weiter kommen
test = []

while open_list:

    aktuelles_f, aktuelles_g, aktuelles_brett = hq.heappop(open_list)

    if aktuelles_brett in closed_list:
        continue
    closed_list.add(aktuelles_brett)

    # Ziel erreicht?
    if aktuelles_brett == goal:
        print("Ziel erreicht")
        print("g:", aktuelles_g)
        print("Knoten (Speicher):", len(closed_list) + len(open_list))
        break

    #0 finden
    for i in range(0, len(aktuelles_brett)):
        if aktuelles_brett[i] == 0:
            index0 = i

    test = []

    if index0 >= 3:
        test.append(index0 - 3)

    if index0 < 6:
        test.append(index0 + 3)

    if index0 % 3 != 2:
        test.append(index0 + 1)

    if index0 % 3 != 0:
        test.append(index0 - 1)

    # zahlen wechseln für alle möglichen richtungen in test
    for tausch_index in test:
        neues_brett = list(aktuelles_brett)
        neues_brett[index0] = neues_brett[tausch_index]
        neues_brett[tausch_index] = 0
        neues_brett = tuple(neues_brett)

        if neues_brett not in closed_list:
            neues_g = aktuelles_g + 1
            neues_h = berechne_hamming(neues_brett, goal)
            neues_f = neues_g + neues_h
            hq.heappush(open_list, (neues_f, neues_g, neues_brett))



print("Starte 100 zufällige Läufe (Hamming vs. Manhattan)")
random.seed(1)

# 100 lösbare startbretter erstellen
zufalls_liste = []
while len(zufalls_liste) < 100:
    brett_zufall = [0,1,2,3,4,5,6,7,8]
    random.shuffle(brett_zufall)
    brett_zufall = tuple(brett_zufall)
    if ist_loesbar(brett_zufall) and brett_zufall != goal:
        zufalls_liste.append(brett_zufall)

for algo in ["hamming", "manhattan"]:
    knoten_liste = []
    zeit_liste = []

    for start in zufalls_liste:
        start_zeit = time.time()

        g = 0
        if algo == "hamming":
            h = berechne_hamming(start, goal)
        else:
            h = berechne_manhattan(start, goal)
        f = g + h

        open_list = []
        closed_list = set()
        start_paket = (f, g, start)
        hq.heappush(open_list, start_paket)

        while open_list:
            aktuelles_f, aktuelles_g, aktuelles_brett = hq.heappop(open_list)

            if aktuelles_brett in closed_list:
                continue
            closed_list.add(aktuelles_brett)

            # Ziel erreicht?
            if aktuelles_brett == goal:
                dauer = time.time() - start_zeit
                knoten = len(closed_list) + len(open_list)
                knoten_liste.append(knoten)
                zeit_liste.append(dauer)
                break

            #0 finden
            for i in range(0, len(aktuelles_brett)):
                if aktuelles_brett[i] == 0:
                    index0 = i

            test = []

            if index0 >= 3:
                test.append(index0 - 3)

            if index0 < 6:
                test.append(index0 + 3)

            if index0 % 3 != 2:
                test.append(index0 + 1)

            if index0 % 3 != 0:
                test.append(index0 - 1)

            for tausch_index in test:
                neues_brett = list(aktuelles_brett)
                neues_brett[index0] = neues_brett[tausch_index]
                neues_brett[tausch_index] = 0
                neues_brett = tuple(neues_brett)

                if neues_brett not in closed_list:
                    neues_g = aktuelles_g + 1
                    if algo == "hamming":
                        neues_h = berechne_hamming(neues_brett, goal)
                    else:
                        neues_h = berechne_manhattan(neues_brett, goal)
                    neues_f = neues_g + neues_h
                    hq.heappush(open_list, (neues_f, neues_g, neues_brett))

    # Mittelwert und Varianz ausrechnen
    mean_knoten = sum(knoten_liste) / len(knoten_liste)
    var_knoten = sum((x - mean_knoten) ** 2 for x in knoten_liste) / len(knoten_liste)

    mean_zeit = sum(zeit_liste) / len(zeit_liste)
    var_zeit = sum((x - mean_zeit) ** 2 for x in zeit_liste) / len(zeit_liste)

    print("\nAlgorithmus:", algo)
    print("  Knoten (Speicher) -> Mittelwert:", round(mean_knoten, 1), "| Varianz:", round(var_knoten, 1))
    print("  Laufzeit (Sek.)   -> Mittelwert:", round(mean_zeit, 4), "| Varianz:", round(var_zeit, 6))