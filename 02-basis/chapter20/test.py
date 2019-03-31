# rangeの基礎
value = range(10) # 0~9
print('value', value)
for i in value:
  print(i)

value = range(2, 10) # 2~9
print('value', value)
for i in value:
  print(i)

value = range(-2, 10) # -2~9
print('value', value)
for i in value:
  print(i)

# xrange
# python2系にあったもの
# 機能がほぼ同等でメモリ効率が悪かったためrangeに集約されているとのこと