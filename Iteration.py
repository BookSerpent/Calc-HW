import math

n = 0
precision = 4
startingValue = 1
x = startingValue

def thingToIterate(x):
    return math.acos(math.exp(-x))

iteration = 1
previousIteration = ""

print("\n\tIteration\tValue")
while iteration != previousIteration:
    x = thingToIterate(x)
    print("\t", n, "\t\t", iteration)
    n += 1
    previousIteration = iteration
    iteration = round(x, precision)

print()
print("Answer:", iteration)
print("Took", n-1, "iterations to find,", n, "to prove.")
print()
