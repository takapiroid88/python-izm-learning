# min
print(min(1, 2, 3, 4, 5))
print(min([1, 2, 3, 4, 5]))
print(min('A', 'B', 'C'))

# max
print(max(1, 2, 3, 4, 5))
print(max([1, 2, 3, 4, 5]))
print(max('A', 'B', 'C'))

# key引数
# 順序づけに用いる関数を指定できる


def key_func1(n):
    return int(n)


l = [2, 3, "111"]
print(min(l, key=key_func1))
print(max(l, key=key_func1))
# 以下も同様に動作
# print(min(l, key=int))
# print(max(l, key=int))


def key_func2(n):
    return str(n)


l = [2, 3, "111"]
print(min(l, key=key_func2))
print(max(l, key=key_func2))

# よくあるkey関数


def key_func3(n):
    return n[2]


l = [(1, 'python', 100), (2, 'Ruby', 80), (3, 'Perl', 40)]
print(min(l, key=key_func3))
print(max(l, key=key_func3))


def key_func4(n):
    return n.score


class Test:
    def __init__(self, code, name, score):
        self.code = code
        self.name = name
        self.score = score

    def __str__(self):
        return '({}, {}, {})'.format(self.code, self.name, self.score)


l = [
    Test(1, 'python', 100),
    Test(2, 'Ruby', 80),  Test(3, 'Perl', 40)
]
print(min(l, key=lambda n: n.score))  # lambda式も良し
print(max(l, key=key_func4))
