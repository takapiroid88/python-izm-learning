# ディクショナリの基本
test_dict = { 'year': '2010', 'month': '1', 'day': '1'}
for i in test_dict:
  print(i)
  print(test_dict[i])

# valueの取得
test_dict = { 'year': '2010', 'month': '1', 'day': '1'}
print(test_dict['year'])
print(test_dict.get('year'))
print(test_dict.get('year_none')) # NONE
print(test_dict.get('year_none', 'NOT_FOUND'))

# 要素の追加
test_dict = {}
test_dict['year'] = '2010'
print(test_dict)

# 要素の削除
test_dict = { 'year': '2010', 'month': '1', 'day': '1'}
del test_dict['year']
print(test_dict)

# key or valueの取得
test_dict = { 'year': '2010', 'month': '1', 'day': '1'}
print(test_dict.keys())
print(test_dict.values())

# key, valueの同時取得
test_dict = { 'year': '2010', 'month': '1', 'day': '1'}
for key, value in test_dict.items():
  print(key, value)

# keyを保持しているか確認
test_dict = { 'year': '2010', 'month': '1', 'day': '1'}
print('year' in test_dict) # True
print('year_none' in test_dict) # False