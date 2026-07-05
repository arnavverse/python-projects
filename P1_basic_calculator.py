"""
Simple calculator project.

Features:
- Addition
- Subtraction
- Multiplication
- Division
- Floor Division
- Remainder
- Exponents
"""

x = input("enter the first number (x): ")
y = input("enter the second number (y): ")
print("ADD:",int(x) + int(y))
print("SUB:",int(x) - int(y))
print("PRODUCT:",int(x) * int(y))
print("DIVISION:",int(x) / int(y))
print("FLOOR DIVISION:",int(x) // int(y))
print("REMAINDER:",int(x) % int(y))
print("x^y:",int(x) ** int(y))
print("x^x:", int(x)**int(x))
print("y^y:", int(y)**int(y))