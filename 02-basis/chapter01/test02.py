import sys
sys.path.append("/Users/takapiroid/Documents/python-izm-learning")
from exp_func import expect_print

test = 100
expect_print(110, test+10)
expect_print(90, test-10)
expect_print(1000, test*10)
expect_print(10, test/10)

##
# 数値への変換
##
test = "100"
expect_print(100, int(test))

##
# 浮動小数点
##
test = "100.5"
expect_print(100.5, float(test))
test = .5
expect_print(0.5, test)


##
# 複素数
#  数値にj/Jをつけると虚数になる
##
test = 100 + 5j
expect_print((100+5j), test)
expect_print(100, test.real)
expect_print(5, test.imag)
