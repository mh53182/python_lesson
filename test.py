# インデックス範囲をスライス指定すると、後のインデックスの手前のデータまでが対象になる
Zen = 'SimpleIsBetterThanComplex'
print('{}{}{}'.format(Zen[0:3], Zen[-3], Zen[-1:]))
print('{}{}{}'.format(Zen[0:2], Zen[-2], Zen[-1]))

print('###########################')

fruits = ['apple', 'kiwi', 'plum']
for f in fruits[:]:
    if len(f) < 5:
        fruits.insert(0, f)
        print(fruits)
        fruits.pop()
        print(fruits)

print(fruits, end = ' ')

print('#####################')

pairs = [(3, 'b'),(1, 'c'),(2, 'a')]
pairs.sort(key = lambda arg : arg[1])
print(pairs)

print('#####################')

combs = []
for x in [3,2,1]:
    for y in [6,5]:
        if x != y:
            combs.append((x, y))
print(combs)

combs2 = [(a,b) for a in [3, 2, 1] for b in [6,5] if a != b]
print(combs2)

print('###################')

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
power = [tuple(row[i] for row in matrix) for i in range(3)]
print(power)

power2 = list(zip(*matrix))
print(power2)

print('#################')

class kusanagi(Exception):
    pass

def raise_character(a):
    print("【A】")
    raise kusanagi
    print("【B】")

def func(name: int):
    try:
        print(name, "【C】")
        raise_character(name)
    except kusanagi:
        print("【D】")
        raise Exception

name = "Magatama"
try:
    func(name)
except Exception:
    print("【E】")

print('############################')

loc = "1"
def scope():
    loc = "2"
    def do_local():
        loc = "3"
    def do_nonlocal():
        nonlocal loc
        loc = "4"
    def do_global():
        global loc
        loc = "5"

    do_local()
    print("【A】", loc)
    do_nonlocal()
    print("【B】", loc)
    do_global()
    print("【C】", loc)

print("【D】", loc)
scope()
print("【E】", loc)

print('#####################')

# [ 実行結果 ]
# Need Speed?
# I'm Saya.
# Need Speed?
# I'm David.

class kusanagi():
    def s(self):
        print("Need Speed?")
        self.m()
    def m(self): 
        print("I'm Saya.")

class wexal(kusanagi):
        def m(self):
            print("I'm David.")

k = kusanagi()
w = wexal()
k.s()
w.s()