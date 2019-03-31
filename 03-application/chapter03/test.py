# クラスの基礎
class Test1:
  def __init__(self, code, name): # クラスの初期化　selfはインスタンス変数
    self.code = code
    self.name = name
test = Test1(100, 'python')
print(test)
print(test.code)
print(test.name)

