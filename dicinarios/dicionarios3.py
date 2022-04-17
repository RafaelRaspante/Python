import time,random
data = {}
for c in range (0,4):
    player_id = "player "+str(c+1)
    data[player_id] = random.randint(1,6)
    time.sleep(.5)
    print(f'The {player_id} has {data[player_id]}')
n = 1
for c in range(0,7):
    for p,v in data.items():
        if v == (6 - c):
            time.sleep(.5)
            print(f"The {n}º position is the {p} with {v}")
            n += 1