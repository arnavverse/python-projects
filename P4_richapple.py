''' CAN YOU AFFORD AN APPLE ? '''
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