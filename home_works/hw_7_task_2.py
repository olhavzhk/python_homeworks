stock_input = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices_input = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


def stock_price(stock, price):
    total_price = 0
    for item, item_price in stock.items():
        if item in price:
            total_price += item_price *price[item]
        else:
            print(f"Price for {item} is not available")
    return total_price


result = stock_price(stock_input, prices_input)
print(result)
