"""
Chapter 1 - Exercise 01
What does round() do when a number ends in .5?
"""
print(round(42.5))   # 42
print(round(43.5))   # 44
print(round(0.5))    # 0
print(round(1.5))    # 2
print(round(2.5))    # 2
print(round(-2.5))   # -2

# The rule: Python uses "round half to even" (banker's rounding).
# When a number is exactly halfway, it rounds to whichever neighbor is EVEN.
# So it doesn't always round up: 42.5 goes DOWN to 42, 43.5 goes UP to 44.
# This keeps rounding from being biased upward when you round lots of numbers.

# Extra thing I found: floats aren't always stored exactly, so this surprises people:
print(round(2.675, 2))  # 2.67, not 2.68, because 2.675 is really 2.67499999...
