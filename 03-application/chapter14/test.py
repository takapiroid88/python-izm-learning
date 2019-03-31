import os

# ファイルの読み
f = open(os.path.join(os.getcwd() + "/03-application/chapter14/read_file.txt"), 'r')
for row in f:
  print(row)
f.close()

# ファイルに書き込み
f = open(os.path.join(os.getcwd() + "/03-application/chapter14/write_file.txt"), 'w')
f.write('ファイルに書き込みました')
f.close()

# 文字コードの指定
f = open(os.path.join(os.getcwd() + "/03-application/chapter14/read_file.txt"), 'r', encoding='shift_jis')
f.close()