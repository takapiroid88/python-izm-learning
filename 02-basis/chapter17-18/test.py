# while文の基礎
counter = 0
while counter < 10:
  counter += 1
  print(counter)

# 無限ループ＆break
counter = 0
while True:
  counter += 1
  print(counter)
  if counter == 10:
    break