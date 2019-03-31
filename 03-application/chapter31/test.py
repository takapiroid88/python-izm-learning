# callable
import sys # moduleなので呼び出し不可
def func_test(): # 関数呼び出し可能
  print('function')

class Test: # class呼び出し可能
  pass

str_test = 'str' # 呼び出し不可な値

print(callable(sys))
print(callable(func_test))
print(callable(Test))
print(callable(str_test))
