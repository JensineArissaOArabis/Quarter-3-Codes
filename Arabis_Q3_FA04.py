import os
os.system('cls')

import numpy as jn

names = ["Me", "Lia", "Jake"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = jn.array([[4500,200,4800,5000,5300],
                   [4000,4100,3900,4200,4600],
                   [6000,5800,5900,6100,6200]])

totals = jn.sum(steps, axis=1)

max_index = jn.argmax(totals)
print(f"Person with the highest total steps: {names[max_index]} with {totals[max_index]} steps")

min_total = jn.min(totals)
max_total = jn.max(totals)
difference = max_total - min_total
print(f"Difference between highest and lowest total steps: {difference}")