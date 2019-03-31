# zipfile
import zipfile
import os
basePath = os.path.join(os.getcwd(), '03-application/chapter40')
# 複数ファイルをまとめるのみで圧縮しない
zipFile = zipfile.ZipFile(os.path.join(basePath, 'compress_1.zip'), 'w', zipfile.ZIP_STORED)
zipFile.write(os.path.join(basePath, 'python.py'))
zipFile.write(os.path.join(basePath, 'python.txt'))
zipFile.write(os.path.join(basePath, 'python.csv'))
zipFile.close()

basePath = os.path.join(os.getcwd(), '03-application/chapter40')
# ファイルサイズ圧縮
zipFile = zipfile.ZipFile(os.path.join(basePath, 'compress_2.zip'), 'w', zipfile.ZIP_DEFLATED)
zipFile.write(os.path.join(basePath, 'python.py'))
zipFile.write(os.path.join(basePath, 'python.txt'))
zipFile.write(os.path.join(basePath, 'python.csv'))
zipFile.close()
