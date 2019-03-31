# random
import random
print(random.random()) # 0~1 float 
print(random.uniform(1,100)) # 0~100 float
print(random.randint(1,100)) # 0~100 int
print(random.choice('1234567890abcdefghij')) # どれか一つの要素
sample_list = ['python', 'izm', 'com', 'random', 'sample'] 
random.shuffle(sample_list) # array内をシャッフル
print(sample_list)