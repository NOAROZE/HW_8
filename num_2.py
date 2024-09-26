import statistics
from itertools import count
players_height: list[float] = []
count_players:int = 0
taller_player: float = None
smallest_player: float = None
avg_height: float = None
players_over_2: float = 0
SENTINEL: int =-999
count_over_avg: int = 0
while True:
    height: float = float(input("enter your height:"))
    if SENTINEL:
        break
    if not 1.6 < height < 3:
        continue
    players_height.append(height)
    count_players += 1
    if height > 2:
        players_over_2 += 1
if len(players_height) > 0:
    taller_player = max(players_height)
    smallest_player = min(players_height)
    avg_height = statistics.mean(players_height)
    print(f"The number of players taken is: {count_players}")
    print(f"The tallest player is: {taller_player}")
    print(f"The smallest player is: {smallest_player}")
    print(f"the average of players height is: {avg_height}")
    print(f"The number of players who are taller than 2 meters is: {players_over_2}")
    for i in range(len(players_height)):
        if players_height[i] > avg_height:
            count_over_avg += 1
    print(f"the players who taller from the average is: {count_over_avg}")