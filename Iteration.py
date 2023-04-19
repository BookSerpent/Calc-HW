import math

n=0
precision = 4
startingValue = 1
x = startingValue

def thingToIterate(x):
    return math.acos(math.pow(math.e, -x))



iteration = 1
previousIteration = ""

while iteration != previousIteration:
    x = thingToIterate(x)
    print(iteration)
    n += 1
    previousIteration = iteration
    iteration = round(x, precision)

print()
print("Answer:", iteration)
print("Took", n, "iterations")
print()
