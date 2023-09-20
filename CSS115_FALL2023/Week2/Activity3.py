import random
import math

radius = random.randint(1,100)
area = math.pi*radius**2
circumference = 2*math.pi*radius

print("Radius is:", radius)
print("Area is:", f'{area:.2f}')
print("circumference is:", f'{circumference:.2f}')
