import math


try:
    radius = float(input("Enter the radius: "))
except:
    radius = float(input("The radius must be an integer, with optional floating-point numbers, \nbut no spaces:    "))

print(f'The circle_area = {math.pi*(radius**2)}')