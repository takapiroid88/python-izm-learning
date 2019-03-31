# with文の基礎
import os
with open(os.path.join(os.getcwd(), '03-application/chapter16/comment.txt')) as f:
  print(f.closed)
print(f.closed)
