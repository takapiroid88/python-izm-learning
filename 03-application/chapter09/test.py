# クラスメソッドの基本
import datetime
class Test:
  def __init__(self, year, month, day):
    self.year = year
    self.month = month
    self.day = day
  
  @classmethod
  def class_method(cls, date_diff=0): # cls: class自身
    today = datetime.datetime.today()
    d = today + datetime.timedelta(days=date_diff)
    return cls(d.year, d.month, d.day)

# インスタンス化なし
test1 = Test.class_method()
print(test1.year, test1.month, test1.day)

# インスタンス化
test2 = Test(2019, 1, 1)
print(test2.year, test2.month, test2.day)