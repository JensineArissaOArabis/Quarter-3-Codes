import os
os.system('cls')

import numpy as jn

names = ["Me", "Lia", "Jake"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = jn.array([[4500,200,4800,5000,5300],
                   [4000,4100,3900,4200,4600],
                   [6000,5800,5900,6100,6200]])



daily_totals = jn.sum(steps, axis=0)


print("Total steps per day:")
for j in range(len(days)):
    print(f"{days[j]}: {daily_totals[j]} steps")

max_day_index = jn.argmax(daily_totals)
print(f"\nMost active day: {days[max_day_index]} with {daily_totals[max_day_index]} total steps")
