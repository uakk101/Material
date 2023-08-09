cart = []
num_items = int(input("Enter the number of items in the cart: "))

for i in range(num_items):
    name = input(f"Enter the name of item {i+1}: ")
    price = float(input(f"Enter the price of item {i+1}: "))
    cart.append((name, price))

subtotal = sum(item[1] for item in cart)

if subtotal >= 100:
    discount = 0.1 * subtotal
elif subtotal >= 50:
    discount = 0.05 * subtotal
else:
    discount = 0

final_amount = subtotal - discount



print(f"\nSubtotal: ${subtotal}")
print(f"Discount: ${discount}".format(discount))
print(f"Final Amount: ${final_amount}")



# print("\nSubtotal: ${:.2f}".format(subtotal))
# print("Discount: ${:.2f}".format(discount))
# print("Final Amount: ${:.2f}".format(final_amount))
