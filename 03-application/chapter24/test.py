# zip
item_list = ['desktop', 'laptop', 'tablet', 'smartphone']
stock_list = [12, 83, 55, 0]
for item_name, stock_count in zip(item_list, stock_list):
  print(item_name, stock_count)

# zip_longest
from itertools import zip_longest
item_list = ['desktop', 'laptop', 'tablet', 'smartphone']
stock_list = [12, 83, 55]
for item_name, stock_count in zip_longest(item_list, stock_list):
  print(item_name, stock_count)

# Noneを他の値で保管: fillvalue=xxx
for item_name, stock_count in zip_longest(item_list, stock_list, fillvalue='no stock'):
  print(item_name, stock_count)
