import math

r = float(input("Enter the radius of a circle: "))
circ = 2 * r * math.pi
print(f"The circumference is: {round(circ,2)}cm")
area = pow(r,2) * math.pi
print(f"The area is: {round(area,2)}cm2")

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Side C is {c}cm")
