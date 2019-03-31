class Test:
  # 通常のメソッド
  def instance_method(self):
    pass

  # インスタンス化なしで呼び出すことが可能
  @classmethod
  def class_method(self):
    pass

  # インスタンス化なしで呼び出すことが可能
  # self,classを表す変数を必要しない
  @staticmethod
  def static_method():
    pass