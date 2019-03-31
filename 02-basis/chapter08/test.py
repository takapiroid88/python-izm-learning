# セットの基本
test_set = {'python', '-', 'izm', '.', 'com', 'python'}
print(test_set)
for i in test_set:
  print(i)

# 要素の追加
test_set = set()
test_set.add('python')
test_set.update({'-', 'izm', '.', 'com'})
print(test_set)

# 要素の削除
test_set = {'python', '-', 'izm', '.', 'com'}
test_set.remove('-') # 存在しないばあいエラーになる
test_set.discard('.')
print(test_set)

# frozenset
# remove/discard/add/updateを行えなくする(AttributeErrorになる)
test_set = frozenset({'python', '-', 'izm', '.', 'com'})
print(test_set)