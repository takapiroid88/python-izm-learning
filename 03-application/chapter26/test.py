# collections.OrderedDict
test_dic = {}
test_dic['word'] = 'doc'
test_dic['excel'] = 'xls'
test_dic['access'] = 'mdb'
test_dic['powerpoint'] = 'ppt'

# 通常(順序は安定しない。。)
for key in test_dic:
  print(key)

import collections
test_dic = collections.OrderedDict()
test_dic['word'] = 'doc'
test_dic['excel'] = 'xls'
test_dic['access'] = 'mdb'
test_dic['powerpoint'] = 'ppt'

# 順序が保証される
for key in test_dic:
  print(key)