# CSVファイルの書き込み
import csv
import os
csv_file1 = os.path.join(os.getcwd(), '03-application/chapter41/python1.csv')
with open(csv_file1, 'w', newline="") as f1:
  writer = csv.writer(f1)
  row = ('python', '-', 'izm', '1')
  writer.writerow(row)

  rows = []
  rows.append(('python', '-', 'izm', '2'))
  rows.append(('python', '-', 'izm', '3'))
  rows.append(('p,y,t,h,o,n', '-', 'i,z,m', '4'))
  writer.writerows(rows)

# option
csv_file2 = os.path.join(os.getcwd(), '03-application/chapter41/python2.csv')
with open(csv_file2, 'w', newline='') as f2:
  writer = csv.writer(f2,
                      quoting=csv.QUOTE_ALL, # 全クォート対象を設定
                      delimiter=':', # セパレータ文字=delimiter を設定
                      quotechar='`') # クォート文字を設定
  row = ('python', '-', 'izm', '1')
  writer.writerow(row)

  rows = []
  rows.append(('python', '-', 'izm', '2'))
  rows.append(('python', '-', 'izm', '3'))
  rows.append(('p,y,t,h,o,n', '-', 'i,z,m', '4'))
  writer.writerows(rows)

# excel_tab
csv_file3 = os.path.join(os.getcwd(), '03-application/chapter41/python3.csv')
with open(csv_file3, 'w', newline='') as f3:
  writer = csv.writer(f3,
                      dialect=csv.excel_tab)
  row = ('python', '-', 'izm', '1')
  writer.writerow(row)

  rows = []
  rows.append(('python', '-', 'izm', '2'))
  rows.append(('python', '-', 'izm', '3'))
  rows.append(('p,y,t,h,o,n', '-', 'i,z,m', '4'))
  writer.writerows(rows)

# 独自フォーマット
class CustomFormat():
  quoting = csv.QUOTE_ALL

csv_file4 = os.path.join(os.getcwd(), '03-application/chapter41/python4.csv')
with open(csv_file4, 'w', newline='') as f4:
  writer = csv.writer(f4,
                      dialect=CustomFormat())
  row = ('python', '-', 'izm', '1')
  writer.writerow(row)

  rows = []
  rows.append(('python', '-', 'izm', '2'))
  rows.append(('python', '-', 'izm', '3'))
  rows.append(('p,y,t,h,o,n', '-', 'i,z,m', '4'))
  writer.writerows(rows)

# 独自フォーマット登録
csv.register_dialect('myformat', CustomFormat)
csv_file5 = os.path.join(os.getcwd(), '03-application/chapter41/python5.csv')
with open(csv_file5, 'w', newline='') as f5:
  writer = csv.writer(f5,
                      dialect='myformat')
  row = ('python', '-', 'izm', '1')
  writer.writerow(row)

  rows = []
  rows.append(('python', '-', 'izm', '2'))
  rows.append(('python', '-', 'izm', '3'))
  rows.append(('p,y,t,h,o,n', '-', 'i,z,m', '4'))
  writer.writerows(rows)

# csvファイルの読み込み
with open(csv_file1, 'r') as read_file:
  reader = csv.reader(read_file)
  for row in reader:
    for cell in row:
      print(cell)