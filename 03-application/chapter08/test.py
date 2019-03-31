# インスタンスメソッドの基本
class Test:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def instance_method(self, display_x=True, display_y=True):
    if display_x:
      print('x is {}'.format(self.x))
    if display_y:
      print('yis {}'.format(self.y))

test = Test(100, 50)
test.instance_method(display_y=False)