prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}
#note zip creates an iterator that caan only be used once
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)
# min_price is (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)
# max_price is (612.78, 'AAPL')
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

#or values directly
min_price = min(prices.values())
print(min_price)

max_price = max(prices.values())
print(max_price)

prices_sorted = sorted(prices.values())
print(prices_sorted)