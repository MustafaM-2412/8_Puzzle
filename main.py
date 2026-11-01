import time
import statistics
from puzzle_state import zufalls_start
from search import a_star

def main():
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    anzahl_test = 100
    start_zustaende = []

    print(f"Generiere {anzahl_test} Startzustände")

    while len(start_zustaende) < anzahl_test:
        neuer_start = zufalls_start(goal)
        if neuer_start not in start_zustaende:
            start_zustaende.append(neuer_start)

    for algo in ["hamming", "manhattan"]:
        print(f"Start test for: {algo.capitalize()}")
        zeiten = []
        knoten_liste = []

        for start in start_zustaende:
            start_zeit = time.time()
            ergebnis = a_star(start, goal, algo)
            end_zeit = time.time()

            zeiten.append(end_zeit - start_zeit)
            knoten_liste.append(ergebnis["knoten"])

        mean_zeit = statistics.mean(zeiten)
        stdev_zeit = statistics.stdev(zeiten)

        mean_knoten = statistics.mean(knoten_liste)
        stdev_knoten = statistics.stdev(knoten_liste)

        print(f"Ergebnisse für {algo.capitalize()}")
        print(f"Speicher (Knoten) -> Mittelwert: {mean_knoten:.1f} | Standardabweichung: {stdev_knoten:.1f}")
        print(f"Speicher (Sek.) -> Mittelwert: {mean_zeit:.4f} | Standardabweichung: {stdev_zeit:.4f}")

if __name__ == "__main__":
    main()