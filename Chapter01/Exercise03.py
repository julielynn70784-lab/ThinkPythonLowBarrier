"""
Chapter 1 - Exercise 03
Guess the type of each value, then check with type().

Expression   My guess     Actual
765          int          int
2.718        float        float
'2 pi'       str          str
abs(-7)      int          int
abs(-7.0)    float        float
abs          function     builtin_function_or_method
int          type         type
type         function     type   <- surprise
"""
values = [765, 2.718, '2 pi', abs(-7), abs(-7.0), abs, int, type]
labels = ['765', '2.718', "'2 pi'", 'abs(-7)', 'abs(-7.0)', 'abs', 'int', 'type']

for label, value in zip(labels, values):
    print(f"{label:<10} {type(value)}")

# Why is type(type) equal to type? Because int, float, str, and type itself are all
# classes, and every class in Python is an object whose type is "type".
