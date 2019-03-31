# property関数
class Test1:
  def __init__(self, url):
    self._url = url
  
  def get_url(self):
    print('-- get url --')
    return self._url

  def set_url(self, url):
    print('-- set url --')
    self._url = url

  def del_url(self):
    print('-- del url --')
    del self._url
  
  # url1のproperty指定
  # 引数は順に、getter/setter/deleter/string
  url = property(get_url, set_url, del_url, 'url property') # gettrerの指定

test = Test1('python-izm.com')
test.url = 'python-izm.net'
print(test.url)
del test.url

class Test2:
  def __init__(self, url):
    self._url = url
  
  @property # getterの定義
  def url(self):
    print('-- get url --')
    return self._url

  @url.setter
  def url(self, url):
    print('-- set url --')
    self._url = url
  
  @url.deleter
  def url(self):
    print('-- del url --')
    del self._url
  
test = Test2('python-izm.com')
test.url = 'python-izm.net'
print(test.url)
del test.url