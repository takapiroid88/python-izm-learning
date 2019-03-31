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
today = datetime.datetime.today()
# 明日の日付
print(today + datetime.timedelta(days=1))
# 2010年1月1日の1週間後
newyear = datetime.datetime(2010, 1, 1)
print(newyear + datetime.timedelta(days=7))
# 2010年1月1日から今日までの日数
calc = today - newyear
print(calc.days)

##
# うるう年の判定
##
import calendar
print(calendar.isleap(2015))
print(calendar.isleap(2016))
print(calendar.isleap(2017))
# 期間内のうるう年の回数
print(calendar.leapdays(2010, 2020))