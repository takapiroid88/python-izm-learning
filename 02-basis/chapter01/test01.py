import sys
sys.path.append("/Users/takapiroid/Documents/python-izm-learning")
from exp_func import expect_print

##
# 文字の基本
##
# python-izm
print("python-izm")
print('python-izm')

# python
# izm
print('''python
izm''')

print("\n")

##
# 文字列の連結
##
pre = "python"
mid = "-"
post = "izm"
exp =  "python-izm"
expect_print(exp, pre + mid + post)

combine = ""
combine += pre
combine += mid
combine += post
exp = "python-izm"
expect_print(exp, combine)

exp = "python-izmpython-izmpython-izm"
expect_print(exp, combine*3)


##
# 文字列へ変換
##
num = 100
exp =  "100円"
expect_print(exp, str(num)+"円")

##
# 文字列の置換
##
text = "python-izm"
exp = "python**izm"
expect_print(exp, text.replace('-', '**'))


##
# 文字列の分割
##
text = "python-izm"
exp = ["python", "izm"]
expect_print(exp, text.split("-"))

##
# 文字列の桁揃え
##
text = "1234"
exp1 = "0000001234"
expect_print(exp1, text.rjust(10, "0"))
exp2 = "!!!!!!1234"
expect_print(exp2, text.rjust(10, "!"))
exp3 = "0000001234"
expect_print(exp3, text.zfill(10))
exp4 = "1234"
expect_print(exp4, text.zfill(3))

##
# 文字列の検索
##
text = "python-izm"
expect_print(True, text.startswith("python"))
expect_print(False, text.startswith("izm"))
expect_print(True, "z" in text)
expect_print(False, "s" in text)

##
# 大文字小文字変換
##
text = "Python-Izm.Com"
expect_print("python-izm.com", text.lower())
expect_print("PYTHON-IZM.COM", text.upper())

##
# 先頭末尾の削除
##
text = "   python-izm.com   "
expect_print("python-izm.com   /", text.lstrip() + "/")
expect_print("-izm.com   /", text.lstrip("   python") + "/")
expect_print("   python-izm.com", text.rstrip())
expect_print("   python-izm.", text.rstrip("com   "))

