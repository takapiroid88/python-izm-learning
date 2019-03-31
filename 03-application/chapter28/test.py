# リスト内包表記
comp_list = [i for i in range(10)]
print(comp_list)
# 以下と同様の動作になる
#  comp_list = []
#  for i in range(10):
#    comp_list.append(i)

comp_list = [str(i * i) for i in range(10)]
print(comp_list)

# ディクショナリ内包表記
comp_dict = {str(i): i * i for i in range(10)}
print(comp_dict)

# セット内包表記
comp_set = { str(i * i) for i in range(10)}
print(comp_set)

# タプル内包表記
# ジェネレータが取得される
gen = ( i for i in range(10))
print(gen)

# forのネスト
comp_list = [i * ii for i in range(1, 10) for ii in range(1, 10)]
print(comp_list)

# ifとの併用
comp_list = [i for i in range(10) if i % 2 == 1]
print(comp_list)


