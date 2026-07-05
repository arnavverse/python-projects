"""
🛒 Fruit Shopping Cart

A Python mini-project that simulates a simple fruit shopping system
based on the user's budget and selected fruit.

Available Fruits:
• Apples
• Mangoes
• Oranges
• Bananas

Features:
• Displays a fruit menu with prices.
• Accepts the user's budget and choice.
• Verifies whether the purchase is possible.
• Shows the remaining balance or additional amount required.
• Handles invalid menu selections.

Concepts Practiced:
• Nested if-else
• User input
• Variables
• Arithmetic operations
• Decision making
"""

budget = int(input("ENTER YOUR BUDGET : ₹"))

apple_price = 100
mango_price = 80
orange_price = 60
banana_price = 90

print('''LIST OF FRUITS :
(1) Apples 🍎 (₹100/kg)
(2) Mangoes 🥭 (₹80/kg)
(3) Oranges 🍊 (₹60/kg)
(4) Bananas 🍌 (₹90/dozen)''')

wish = int(input("TYPE THE NUMBER MENTIONED ON THE FRUIT OF YOUR CHOICE : "))
if (wish == 1):
    if (budget >= apple_price):
        print('''PAYMENT SUCCESSFUL!
    ADDED 1KG APPLE TO THE CART.
        MONEY LEFT = ₹''', (budget) - (apple_price))
    else:
        print('''PAYMENT UNSUCCESSFUL!
        YOU NEED ₹''', (apple_price) - (budget), "MORE.")
if (wish == 2):
    if (budget >= mango_price):
        print('''PAYMENT SUCCESSFUL!
    ADDED 1KG MANGO TO THE CART.
        MONEY LEFT = ₹''', (budget) - (mango_price))
    else:
        print('''PAYMENT UNSUCCESSFUL!
        YOU NEED ₹''', (mango_price) - (budget), "MORE.")
if (wish<=0):
    print("GHEE KHTM💔".center(40))
if (wish == 3):
    if (budget >= orange_price):
        print('''PAYMENT SUCCESSFUL!
    ADDED 1KG ORANGE TO THE CART.
        MONEY LEFT = ₹''', (budget) - (orange_price))
    else:
        print('''PAYMENT UNSUCCESSFUL!
        YOU NEED ₹''', (orange_price) - (budget), "MORE.")
if (wish > 4):
    print("GHEE KHTM🥀".center(40))
if (wish == 4):
    if (budget >= banana_price):
        print('''PAYMENT SUCCESSFUL!
    ADDED 1KG BANANA TO THE CART.
        MONEY LEFT = ₹''', (budget) - (banana_price))
    else:
        print('''PAYMENT UNSUCCESSFUL!
        YOU NEED ₹''', (banana_price) - (budget), "MORE.")
print("THANKS!".center(40))