import random
balls = [1, 2, 3, 4, 5]
draw = random.choices(balls, k=3)

print("Вытащенные шары:", draw)


help(random.choices)