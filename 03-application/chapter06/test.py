class TestBase:
  def test_method(self, msg):
    print('TestBase: ', msg)

class Test(TestBase):
  def test_method(self, msg):
    super().test_method(msg)

test = Test()
test.test_method('method call')