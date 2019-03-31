# 関数の基礎
def test_func1():
  print('call test_func1')
test_func1()

# 引数の基礎
def test_func2(num1, num2):
  print('calc:', num1 + num2)
test_func2(1,2)

# 引数の初期値
def test_func3(num1, num2=3):
  print('calc:', num1 + num2)
test_func3(1)

# 関数とメソッド
class Test:
  def test_method(self):
    print('call test_method')
Test().test_method()
print('func', test_func1)
print('func type:', type(test_func1))
print('method', Test().test_method)
print('method type:', type(Test().test_method))

