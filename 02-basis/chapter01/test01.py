##
#  文字の基本
##
# python-izm
print("python-izm")
print('python-izm')

# python
# izm
print('''python
izm''')

print("")

##
# 文字列の連結
##
pre = "python"
mid = "-"
post = "izm"
# python-izm
print(pre + mid + post)

combine = ""
combine += pre
combine += mid
combine += post
# python-izm
print(combine)

# python-izmpython-izmpython-izm
print(combine*3)

print("")

##
# 文字列へ変換
##
num = 100
# 100円
print(str(num)+"円")

##
# 文字列の置換
##
text = "python-izm"
# python**izm
print(text.replace('-', '**'))
