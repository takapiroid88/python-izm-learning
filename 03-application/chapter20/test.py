# リスト自体をソートする
list = [100, 200, 10, 800, 60]
print('raw:', list)
list.sort()
print('sorted:', list)

# リストのソート結果のみ取得
# リスト自体は操作されない
list = [100, 200, 10, 800, 60]
print('raw:', list)
print('sorted:', sorted(list))
print('after:', list)