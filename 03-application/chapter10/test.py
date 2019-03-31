# スタティックメソッドの基本
class Test:
  @staticmethod
  def static_method(x, y):
    return x + y

# インスタンス化なし
print(Test.static_method(1,2))

# インスタンス化あり
print(Test().static_method(1,2))