# hasattr
class Test:
  def __init__(self):
    self.code = 1

test = Test()
test.name = 'name'

print(hasattr(test, "code"))
print(hasattr(test, "name"))
print(hasattr(test, "xxx"))

# getattr
print(getattr(test, "code"))
print(getattr(test, "name"))
print(getattr(test, "xxx", 'No Attr')) # default指定しない場合はError
