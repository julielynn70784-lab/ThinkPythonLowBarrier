"""
Chapter 2 - Exercise 01
Making mistakes on purpose with variables and statements.
Lines that cause errors are commented out so the file still runs.
"""

# n = 42 is legal. What about 42 = n?
n = 42
# 42 = n
# SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?

# x = y = 1 -> assigns the same value to both variables. This is legal.
x = y = 1
print(f"x: {x}  y: {y}")

# Ending a statement with a semicolon is allowed (Python just ignores it)
z = 3;
print(z)

# Ending a statement with a period usually is NOT allowed
# print(z).
# SyntaxError: invalid syntax
# But w = 3. actually works, because "3." is read as the float 3.0
w = 3.
print(w, type(w))

# Misspelling a module name
# import maath
# ModuleNotFoundError: No module named 'maath'

# In math, xy means x times y. What about Python?
# print(xy)
# NameError: name 'xy' is not defined  -> Python thinks xy is one variable name
print(x * y)  # you need the * operator
