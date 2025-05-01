def calculate_total_price(prices, tax_rate):
    total = 0
    for price in prices:
        total += price
    total_with_tax = total * tax_rate
    return total_with_tax

items = [29.99, 9.99, 4.99, 14.99]
tax = 0.08

final_price = calculate_total_price(item, tax)  # Typo here: 'item' instead of 'items'
print("Total Price with Tax:", final_price)
