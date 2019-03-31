# all
# 反復可能オブジェクトが保有している要素が全て真かチェック
test_list_1 = [0,1,2]
test_list_2 = ([],[],[])
test_list_3 = (['python'], ['izm'])
print(all(test_list_1))
print(all(test_list_2))
print(all(test_list_3))

# any
# 反復可能オブジェクトが保有している要素に真があるかチェック
test_list_1 = [0,1,2]
test_list_2 = ([],[],[])
test_list_3 = (['python'], ['izm'])
print(any(test_list_1))
print(any(test_list_2))
print(any(test_list_3))