"""
Chapter 1 - Exercise 02
Making mistakes on purpose. The lines that cause a SyntaxError are commented out,
because one syntax error stops the WHOLE file from running. The error message
I got is written under each one.
"""
print(+2)      # 2  -> a plus sign in front of a number is allowed ("unary plus")
print(2++2)    # 4  -> Python reads this as 2 + (+2), so it is not an error
print(2--2)    # 4  -> same idea: 2 - (-2)

# print(4 2)
# SyntaxError: invalid syntax. Perhaps you forgot a comma?
# Two values next to each other with no operator between them.

# print(round(42.5)
# SyntaxError: '(' was never closed

# print(round 42.5)
# SyntaxError: invalid syntax. Perhaps you forgot a comma?
# Same error as 4 2 because "round" and "42.5" are also just two values
# sitting next to each other (a function name and a number).

print(round)   # No error! Without parentheses the function isn't called,
               # Python just shows the function itself: <built-in function round>
