import math

leg1 = float(input("Enter the length of leg 1:"))
leg2 = float(input("Enter the length of leg 2:"))
hypotenuse =  math.sqrt(leg1**2 + leg2**2)

print("Leg 1 is", leg1)
print("Leg 2 is", leg2)
print(f"Hypotenuse is {hypotenuse:.2f}")
