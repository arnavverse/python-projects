"""
📐 Shape Area Calculator

A Python mini-project that calculates the area of common geometric
shapes using user-provided dimensions.

Supported Shapes:
• Parallelogram
• Right Triangle
• Circle
• Square

Concepts Practiced:
• input()
• int()
• Mathematical formulas
• Arithmetic operators
• print()
"""

# AREA OF PARALLELOGRAM
a = input("Base : ")
b = input("Height : ")
print("AREA OF PARALLELOGRAM =",int(a)*int(b),"square units")

# AREA OF RIGHT ANGLE TRIANGLE
c = input("Base : ")
d = input("Height : ")
print("AREA OF Δ =",0.5*int(c)*int(d), "square units")

# AREA OF CIRCLE
e = input("Radius : ")
print("AREA OF CIRCLE =",22/7*int(e)*int(e), "square units" )

# AREA OF SQUARE
d = input("edge : ")
print("AREA OF SQUARE =",int(d)*int(d), "square units")