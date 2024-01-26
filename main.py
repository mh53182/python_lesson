# 関数まわりメモ

# 52. 位置引数のタプル化

# 引数の前にアスタリスク"*"をつけると、渡されてくる引数の数が分からなくても全部タプルに入れてくれる
def say_something(word, *args):
    print('word =', word)
    for arg in args:
        print(arg)

say_something('Hi!', 'Mike', 'Nancy')


print('##################################')

# 53. キーワード引数の辞書化

# 引数の前にアスタリスク2つ"**"をつけると、渡されてくるキーワード引数を全部辞書に入れてくれる
def menu(**kwargs): # keyword arguments
    # print(kwargs)
    for k, v in kwargs.items():
        print(k, v)

# menu('entree': 'beef', 'drink': 'coffee',)

d = {
    'entree': 'beef',
    'drink': 'coffee',
    'dessert': 'ice'
}

menu(**d)

print('##################################')

# 55. 関数内関数

# ある関数の中でのみ繰り返し使う関数は関数内関数に出来る。
def outer(a, b):

    def inner(c, d):
        return c + d
    
    r1 = inner(a, b)
    r2 = inner(b,a)
    print(r1, r2)
    print(r1 + r2)

outer(1, 2)




print('##################################')

# 以下、閏年判定

# def main():
#     leap_year_check()

# def leap_year_check():
#     T = int(input())
#     N = int(input())

#     if N % 400 == 0:
#         print(N, "is a leap year")

#     elif N % 4 == 0 and N % 100 != 0:
#         print(N, "is a leap year")

#     else:
#         print(N, "is not leap year")

# if __name__ == "__main__":
#     main()

# 西暦が4で割り切れる年は閏年。
# ただし、100で割り切れる年は閏年ではない。
# ただし、400で割り切れる年は閏年。

# input_line = int(input())
# for i in range(input_line):
#     s = input().rstrip().split(' ')
#     print("hello = "+s[0]+" , world = "+s[1])