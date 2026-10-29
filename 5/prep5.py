def max_of_three(x, y, z):
    return max(x, y, z)

def format_price(amount, currency = "Kč"):
    return(f"{amount:.2f} {currency}")


print(max_of_three(3,9,5))
print(max_of_three(-1,-8,-3))
print(format_price(1800))
print(format_price(72.5, currency="€"))