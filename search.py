import heapq as hq
from heuristics import berechne_hamming, berechne_manhattan
from puzzle_state import zug_machen

def a_star(start, goal, algo) -> dict:
    open_list = []
    closed_list = set()

    g = 0
    if algo == "hamming":
        h = berechne_hamming(start, goal)
    else:
        h = berechne_manhattan(start, goal)
    f = g + h

    hq.heappush(open_list, (f, g, start))

    while open_list:
        aktuelles_f, aktuelles_g, aktuelles_brett = hq.heappop(open_list)

        #bugfix: aktuelles_f -> aktuelles_brett
        if aktuelles_brett in closed_list:
            continue
        closed_list.add(aktuelles_brett)

        if aktuelles_brett == goal:
            knoten = len(closed_list) + len(open_list)
            return {"kosten": aktuelles_g, "knoten": knoten}

        neue_zustaende = zug_machen(aktuelles_brett)

        for neues_brett in neue_zustaende:
            if neues_brett not in closed_list:
                neues_g = aktuelles_g + 1
                if algo == "hamming":
                    neues_h = berechne_hamming(neues_brett, goal)
                else:
                    neues_h = berechne_manhattan(neues_brett, goal)
                neues_f = neues_g + neues_h
                hq.heappush(open_list, (neues_f, neues_g, neues_brett))
    return {"kosten": -1, "knoten": len(closed_list) + len(open_list)}
