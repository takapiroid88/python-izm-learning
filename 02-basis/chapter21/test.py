# printの基礎
print('python')
print('-')
print('izm')
print('com')

# 改行しない
print('python', end = '  ') # デフォルトではend='\n'になっている
print('-', end = '  ')
print('izm', end = '  ')
print('com')

# 出力先の変更
import os
import sys
dir = os.path.join(os.getcwd(), '02-basis/chapter21', 'output.txt')
print(dir)
f_obj = open(dir, "w")
print('python-izm.com', file=f_obj)

# format出力
# %s: 文字列
# %d: 数値
print('pythonの学習サイト：%s' % 'python-izm.com')
print('pythonの学習サイト：%s-%s.%s' % ('python', 'izm', 'com'))
test_int = 100 + 100
test_str = 'python-izm.com'
print('サイト開設 %d 日め！ %s' % (test_int, test_str))

print('pythonの学習サイト：{}'.format('python-izm.com'))
print('pythonの学習サイト：{0}-{1}.{2}'.format('python', 'izm', 'com'))
test_int = 100 + 100
test_str = 'python-izm.com'
print('サイト開設 {1} 日め！ {0}'.format(test_str, test_int))

