import numpy as jn

names = ["Me", "Lia", "Jake"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = jn.array([[4500,200,4800,5000,5300],
                   [4000,4100,3900,4200,4600],
                   [6000,5800,5900,6100,6200]])

for i in range(len(names)):
    total = 0
    for daily_steps in steps[i]:
        total += daily_steps
    print(f"{names[i]} Total Steps: {total}")
    

    avg = total / len(steps[i])
    print(f"{names[i]} Average Steps: {avg:.2f}")
    print()

overall_max = steps.max()
overall_min = steps.min()

print(f"Overall Maximum Steps: {overall_max}")
print(f"Overall Minimum Steps: {overall_min}")

# Using numpy functions and creating arrays made it easier because it allowed us coders to turn a "pile of data" into a structured grid which made coding easier.
# Summarizing data itself was easy due to the fuctions available but the hard part is understanding these functions.