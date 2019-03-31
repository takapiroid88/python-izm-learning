# インデックスと値を同時に取り出す
test_list = ['python', 'izm', 'com']
for i, value in enumerate(test_list):
  print(i, value)
print(enumerate(test_list))

# 開始値を指定
# index値の開始が変わるだけでvalueは先頭から取得
test_list = ['python', 'izm', 'com']
for i, value in enumerate(test_list, 1):
  print(i, value)