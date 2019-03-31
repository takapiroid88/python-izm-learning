# try, except, finally
def exception_test(value1, value2):
  print('計算開始')
  result = 0
  try:
    result = value1 + value2
  except:
    print('計算できませんでした')
  finally: # 正常、異常時どちらでも処理する
    print('計算終了')
  return result

print(exception_test(100, 200))
print(exception_test(100, "200"))

# raise: エラー発生
def exception_test2(value1, value2):
  print('計算開始')
  result = 0
  try:
    result = value1 + value2
  except:
    print('計算できませんでした')
    raise
  finally: # 正常、異常時どちらでも処理する
    print('計算終了')
  return result

try:
  print(exception_test2(100, 200))
  print(exception_test2(100, "200"))
except:
  print('エラーが起きました')

# エラー内容（スタックトレース）の取得
import sys
import traceback
try:
  print(exception_test2(100, "200"))
except:
  print('エラーが起きました')
  print(traceback.format_exc(sys.exc_info()[2]))