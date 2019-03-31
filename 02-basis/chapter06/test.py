# 基本
test_list = ['python', '-', 'izm', 'com']
print(test_list)
for i in test_list:
  print(i)

# 要素の追加
test_list = []
test_list.append('python')
test_list.append('-')
test_list.append('izm')
test_list.append('.')
test_list.append('com')
print(test_list)

# インデックス指定して追加
test_list = ['python', 'izm', 'com']
test_list.insert(1, '-')
test_list.insert(3, '.')
test_list.insert(0, 'http://www.')
print(test_list)

# 要素の削除（要素一致）
test_list = ['1', '2', '3', '2', '1']
test_list.remove('2')
# はじめにヒットした要素のみ削除される
print(test_list)

# 要素の削除（インデックス指定）
test_list = ['1', '2', '3', '2', '1']
test_list.pop(1)
print(test_list)
test_list.pop()
print(test_list)

# 要素のインデックスを取得
test_list = [100, 200, 300, 400]
i = test_list.index(200)
print(i)

# リスト内での要素数を取得
test_list = [100, 200, 300, 200, 400]
count = test_list.count(200)
print(count)


