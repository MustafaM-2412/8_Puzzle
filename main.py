import heapq as hq

start = (1,2,3,0,4,6,7,5,8)
goal = (1,2,3,4,5,6,7,8,0)

h = 0
g = 0
f = 0
for i in range(0,len(start)):
    if start[i] == 0:
        continue
    if not start[i] == goal[i]:
        h = h + 1

print (h)
f = h + g

open_list = []
start_paket = (f, g, start)
hq.heappush(open_list, start_paket)
print("Offene Liste:", open_list)

test = []

while open_list:

    aktuelles_f, aktuelles_g, aktuelles_brett = hq.heappop(open_list)

    # Ziel erreicht?
    if aktuelles_brett == goal:
        print("Ziel erreicht")
        print("g:", aktuelles_g)
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
