# リスト自体を逆順にする
list = [100, 200, 10, 800, 60]
print('raw:', list)
list.reverse()
print('reversed:', list)

# リストの逆順を取得する
# リスト自体は操作されない
list = [100, 200, 10, 800, 60]
print('raw:', list)
print('reversed:')
for value in reversed(list):
  print(value)
print('after:', list)

# スライスで逆順を取得
list = [100, 200, 10, 800, 60]
print('raw:', list)
print('reversed:')
for value in list[::-1]:
  print(value)
print('after:', list)