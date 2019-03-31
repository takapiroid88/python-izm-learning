# ジェネレータ関数-yield
def func_sample(): # 関数内にyieldがあるとジェネレータになる
  yield('おはよう')
  yield('こんにちは')


# ジェネレータは反復可能となるためforループが可能
for i in func_sample():
  print(i)

f = func_sample()
print(next(f))
print(next(f))

# ジェネレータ式
gen_sample = (i for i in 'おはよう こんにちは こんばんは'.split())
print(gen_sample)
for i in gen_sample:
  print(i)