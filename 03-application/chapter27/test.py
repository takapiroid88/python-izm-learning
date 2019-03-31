# セットを比較
test_set_1 = set({'python', 'izm', 'com'})

## セットと共通の要素をもたないときにTrue
print(test_set_1.isdisjoint({'python', 'izm'})) # False
print(test_set_1.isdisjoint({1,2,3})) # True

## セットの全要素が引数のセットに含まれている
print(test_set_1.issubset({'python', 'izm'})) # False
print(test_set_1.issubset({'python', 'izm', 'com', 'www'})) # True
print(test_set_1 <= ({'python', 'izm'})) # False
print(test_set_1 <= ({'python', 'izm', 'com', 'www'})) # True

## 引数のセット全要素がセットに含まれる時
print(test_set_1.issuperset({'python', 'izm', 'com', 'www'})) # False
print(test_set_1.issuperset({'python', 'izm', 'com'})) # True
print(test_set_1.issuperset({'python', 'izm'})) # True
print(test_set_1 >= ({'python', 'izm', 'com', 'www'})) # False
print(test_set_1 >= ({'python', 'izm', 'com'})) # True
print(test_set_1 >= ({'python', 'izm'})) # True

# セットを比較して作成
test_set_2 = {'python', 'izm', 'com'}

## union: セットと引数の反復要素を合わせる
print(test_set_2.union({'www', 'python'}))
print(test_set_2 | ({'www', 'python'}))

## intersection: セットと引数の反復要素の共通要素でセットを生成
print(test_set_2.intersection({'python', 'com'}))
print(test_set_2 & ({'python', 'com'}))

## differene: セットに対し引数の反復要素に含まれない要素でセットを生成
print(test_set_2.difference({'izm'}))
print(test_set_2 - ({'izm'}))

## symmetric_difference: セットと引数の反復要素で合致しない要素でセットを生成
print(test_set_2.symmetric_difference({'python', 'com', 'www'}))
print(test_set_2 ^ ({'python', 'com', 'www'}))


# セットを比較して更新

## intersection_update: セットと引数の反復要素に含まれる要素のセットへ更新
test_set_3 = set({'python', 'izm', 'com'})
test_set_3.intersection_update({'www', 'python'})
print(test_set_3) # {'python'}
test_set_3 = set({'python', 'izm', 'com'})
test_set_3 &= ({'www', 'python'})
print(test_set_3) # {'python'}

## difference_update: セットと引数の反復要素に含まれない要素のセットへ更新
test_set_3 = set({'python', 'izm', 'com'})
test_set_3.difference_update({'www', 'python'})
print(test_set_3)
test_set_3 = set({'python', 'izm', 'com'})
test_set_3 -= ({'www', 'python'})
print(test_set_3)

## symmetric_difference_update: セットと引数の反復要素で合致しない要素のセットへ更新
test_set_3 = set({'python', 'izm', 'com'})
test_set_3.symmetric_difference_update({'www', 'python'})
print(test_set_3)
test_set_3 = set({'python', 'izm', 'com'})
test_set_3 ^= ({'www', 'python'})
print(test_set_3)

