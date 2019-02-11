import sys
sys.path.append("/Users/takapiroid/Documents/python-izm-learning")
from exp_func import expect_print
import datetime

##
# 日付の取得
##
test_date = datetime.date.today()
test_date_detail = datetime.datetime.today()
print(test_date)
print(test_date_detail)
print(test_date.isoformat())
print(test_date_detail.isoformat())

##
# 日付の計算
##
test = datetime.datetime.today()
# 明日の日付
print(test + datetime.timedelta(dats=1))
