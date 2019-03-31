# クラス継承の基本
class Country:
  def __init__(self, name):
    self.name = name
  
class City(Country):
  def __init__(self, name, city):
    super().__init__(name)
    self.city = city

city = City('Japan', 'Tokyo')
print(city)
print(city.name)
print(city.city)