# 特殊メソッドを実装
class Test:
  def __enter__(self):
    print('__enter__')
    return 'as obj' # asで取得できる値を返却
  
  def __exit__(self, type, value, traceback):
    print('__exit__')
    print('type:', type)
    print('value:', value)
    print('traceback:', traceback)

with Test():
  print('with')

with Test() as obj:
  print('with')
  print('obj:', obj)

try:
  with Test():
   print('with')
   int('test')
except:
 pass

# デコーダを使用する
from contextlib import contextmanager
@contextmanager
def context_func():
  print('enter')
  yield 'as obj' # asで受け取るオブジェクトを指定する
  print('exit')

with context_func() as obj:
  print('with')
  print('obj:', obj)