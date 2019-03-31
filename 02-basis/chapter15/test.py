# If文の基礎
value = 2
if value == 1:
  print('valueの値は1です')
elif value == 2:
  print('valueの値は2です')
elif value == 3:
  print('valueの値は3です')
else:
  print('該当する値はありません')
  
# 条件の組み合わせ
value1 = 'python'
value2 = 'izm'
if value1 == 'PYTHON':
  pass
elif value1 == 'python' and value2 == 'izm':
  print('2番目の条件式がTrue')
elif value1 == 'IZM' or value2 == 'Python':
  print('3番目の条件式がTrue')
  
# pass → 何もしない
value = True
if value:
  pass
else:
  print(False)