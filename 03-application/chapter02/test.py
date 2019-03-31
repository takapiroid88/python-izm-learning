# *args: tapluとして取得できる
def test_func1(*args):
  print(args)
test_func1(1,2,3,4)

def test_func2(code, name, *args):
  print(code, name)
  print(args)
test_func2(100, 'python-izm', 'JP', 'US')

# **kwargs: dictionaryとして取得できる
def test_func3(**kwargs):
  print(kwargs)
test_func3(code=100, name='python-izm')

def test_func4(code, name, *args, **kwargs):
  print(code, name)
  print(args)
  print(kwargs)
test_func4(100, 'python-izm', u'パイソンイズム', 'JP', 'US', email="xxx", city="Tokyo")