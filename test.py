# インデックス範囲をスライス指定すると、後のインデックスの手前のデータまでが対象になる
Zen = 'SimpleIsBetterThanComplex'
print('{}{}{}'.format(Zen[0:3], Zen[-3], Zen[-1:]))
print('{}{}{}'.format(Zen[0:2], Zen[-2], Zen[-1]))

print('###########################')

fruits = ['apple', 'kiwi', 'plum']
for f in fruits[:]:
    if len(f) < 5:
        fruits.insert(0, f)
        fruits.pop()
        print(fruits)

print(fruits, end = ' ')