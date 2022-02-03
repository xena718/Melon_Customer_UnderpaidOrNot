orders = open ("customer-orders.txt")
melon_cost = 1.00
for line in orders:
    line = line.rstrip() #each line is a string. remove any white spaces at the end of each line.
    order_L = line.split("|") # string split method, output is a list of strings
    customer_name = order_L[1]
    expected_price = int(order_L[2])*melon_cost
    paid_price = float(order_L[3])
    if expected_price > paid_price:
        print(f"{customer_name} paid ${paid_price:.2f}, expected ${expected_price:.2f}, Underpaid")
    elif expected_price < paid_price:
        print(f"{customer_name} paid ${paid_price:.2f}, expected ${expected_price:.2f}, Overpaid")
    else:
        print(f"{customer_name} paid ${paid_price:.2f}, expected ${expected_price:.2f}, Paid exact amount")
# if __name__ == "__main__":