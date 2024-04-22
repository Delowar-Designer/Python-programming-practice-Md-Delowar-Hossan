# Map Function
import math

def area(r):
    return math.pi * (r ** 2)

radius = [2,3,5,7,3.7,6.9]
areas = []
for r in radius:
    areas.append(area(r))

print(areas)


result = list(map(area, radius))
print(result)


