# 複数のスレッドによる処理
import threading
import time

class TestThread(threading.Thread):
  def run(self):
    print('== start sub thread ==')
    for i in range(5):
      time.sleep(5)
      print('== sub thread ==')
    print('== end sub thread ==')

# th = TestThread()
# th.start()
# time.sleep(1)

# print('== start main thread ==')
# for i in range(5):
#   time.sleep(10)
#   print('== main thread ==')
# print('== end main thread ==')

# デーモンスレッド
# Trueにするとメインスレッドが終了するとサブスレッドも終了する
th = TestThread()
th.daemon = True
th.start()
time.sleep(1)

print('== start main thread ==')
print('== end main thread ==')