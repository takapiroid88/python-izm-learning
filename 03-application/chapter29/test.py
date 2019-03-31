# isinstance
class Test:
  def __init__(self):
    pass

print(isinstance(Test(), Test))
print(isinstance(('python', 'izm'), tuple))
print(isinstance(['python', 'izm'], list))
print(isinstance({'python': 'izm'}, dict))
