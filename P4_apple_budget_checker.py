"""
🍎 Can You Afford an Apple?

A beginner-friendly Python project that checks whether the user's
budget is enough to buy 1 kg of apples.

Features:
• Takes the user's budget as input.
• Compares the budget with the apple price.
• Displays whether the purchase is successful.
• Shows the remaining amount or the extra money required.

Concepts Practiced:
• input()
• Variables
• if-elif-else
• Comparison operators
• Arithmetic operations
"""

# Applicable for the budget < 100 / > 100 / = 100.
print("CAN YOU AFFORD AN APPLE ?".center(35))
print("Per kg apple costs ₹100.")
budget = int(input("Enter your budget : ₹"))
apple_price = 100
if ((apple_price) > (budget)):
          print('''Overpriced!
          Money left = ₹''',(budget)) 
elif ((budget) - (apple_price) < (budget)):
    print('''Added 1kg apple to the cart.
          Money left = ₹''',(budget) - (apple_price))