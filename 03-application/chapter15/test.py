# ディレクトリ、ファイルの存在チェック
import os 
filepath = os.path.join(os.getcwd() + '/03-application/chapter15/comment.txt')
if os.path.exists(filepath):
  print('指定のファイルorディレクトリが存在しています')
  if os.path.isdir(filepath):
    print('指定のパスはディレクトリです')
  elif os.path.isfile(filepath):
    print('指定のパスはファイルです')
  
else: 
  print('指定のファイルorディレクトリは存在しません')

# ディレクトリの作成と削除
import shutil
def show_dir(path):
  for dirpath, dirnames, filenames in os.walk(path):
    for dirname in dirnames:
      print(os.path.join(dirpath, dirname))

rootDir = os.path.join(os.getcwd(), '03-application/chapter15')
os.mkdir(os.path.join(rootDir, 'tmp'))
os.makedirs(os.path.join(rootDir, 'tmp2/tmp3'))
show_dir(rootDir)
os.removedirs(os.path.join(rootDir, 'tmp2/tmp3')) # ディレクトリがからでないとエラー
shutil.rmtree(os.path.join(rootDir, 'tmp')) # 再帰的に削除を行う
show_dir(rootDir)

# ファイル、ディレクトリのコピー
basePath = os.path.join(os.getcwd(), '03-application/chapter15')
src = os.path.join(basePath, 'comment.txt')
dest = os.path.join(basePath, 'copied.txt')
shutil.copy(src, dest)
print('exist copied file: ', os.path.exists(dest))
os.remove(dest)