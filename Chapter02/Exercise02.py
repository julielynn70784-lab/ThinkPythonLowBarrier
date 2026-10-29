"""
Chapter 2 - Exercise 02
Using Python as a calculator.
"""
import math

# 1. Volume of a sphere with radius 5:  V = 4/3 * pi * r^3
radius = 5
volume = 4 / 3 * math.pi * radius ** 3
print(f"1. Volume of a sphere with radius {radius}: {volume:.2f}")

# 2. Check that cos(x)^2 + sin(x)^2 = 1 for x = 42
x = 42
result = math.cos(x) ** 2 + math.sin(x) ** 2
print(f"2. cos({x})^2 + sin({x})^2 = {result}")
# Floats can be off by a tiny amount (for some x you get 0.9999999999999999),
# so compare with math.isclose instead of ==
print(f"   Is it (close enough to) 1? {math.isclose(result, 1)}")

# 3. e squared, three different ways
print(f"3. math.e ** 2     = {math.e ** 2}")
print(f"   math.pow(e, 2)  = {math.pow(math.e, 2)}")
print(f"   math.exp(2)     = {math.exp(2)}")
# math.exp(2) is the most accurate: it computes e^2 directly, while the other two
# start from math.e, which is already a rounded value, and square that rounding error.
