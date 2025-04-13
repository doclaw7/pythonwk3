price = float(input("Enter the price: "))
discount_percentage = float(input("Enter the discount percentage: "))
def calculate_discount(price, discount_percentage):
   if discount_percentage>=20:
    return price - (price * discount_percentage / 100)
   else:
    return price
print( calculate_discount(price, discount_percentage))