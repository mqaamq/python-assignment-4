#a1
name = input("Enter customer name: ")
total = 0
count = 0

while True:
    product = input("Enter product name (or 'done' to finish): ")
    if product == "done":
        break
    
    price = float(input("Enter price: "))
    total = total + price
    count = count + 1

print("Customer :", name.upper())
print("Items :", count)
print("Subtotal :", total, "KZT")
#a2
if total < 3000:
    discount_rate = 0
    tier = "No discount"
elif total < 7000:
    discount_rate = 0.05
    tier = "5% discount"
else:
    discount_rate = 0.15
    tier = "15% discount"

discount = total * discount_rate
final_total = total - discount

print("Discount tier :", tier)
print("Discount :", discount, "KZT")
print("Total :", final_total, "KZT")
#a3
print("Name uppercase :", name.upper())
print("Name lowercase :", name.lower())
print("Name length :", len(name))

if len(name) > 5:
    print("Long name")
else:
    print("Short name")