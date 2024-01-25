# 16.リスト型

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ひとつ飛ばしでデータを抽出する
print(l[::2])

# マイナスをつけたら逆から
print(l[::-2])


# 配列をネストする
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)

# ex)xからbを取り出すには…
print(x[0][1])
# インデックス0のリストのインデックス1のデータが抽出できる

print('########################')

# 17. リストの操作

s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

s[0] = 'X'
print(s)

s[2:5] = ['C', 'D', 'E']
print(s)

s[3:6] = []
print(s)

s[:] = []
print(s)


s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

s.append(100)
print(s)

s.insert(0, 200)
print(s)

s.pop(2)
print(s[0:4])

del s[2]
print(s)

s.remove(9)
print(s)

t = [1, 2, 3, 4, 5]
u = [6, 7, 8, 9, 10]
v = t + u
print(v)
print(t)
print(u)

t += u
print(t)
print(u)

u.extend(t)
print(t)
print(u)

print('########################')



# 18.リストのメソッド

r = [1, 2, 3, 4, 5, 1, 2, 3]

# "3"がインデックス何番にあるか調べる
print(r.index(3))

# もう一個の"3"を探すため、インデックス[3]から後ろの"3"を探す
print(r.index(3, 3))

# "3"の個数を数える
print(r.count(3))

# ソート
# 昇順に
r.sort()
print(r)

# 降順に
r.sort(reverse=True)
print(r)

# 逆向きに並び変え
r.reverse()
print(r)


# スプリット
s = 'My name is Mike.'

# sの文字列を''の中身(この場合は半角スペース)で区切ってリストに入れる
to_split = s.split(' ')
print(to_split)

# リストの中身を''の中身(この場合は半角スペース)で繋げて合体する
x = ' '.join(to_split)
print(x)


print('########################')



# 19.リストのコピー

# 後から定義したリストの中身を書き換えても、先に定義したリストも書き換わる。
# イコールで繋いでも、jはiをコピーして作られたわけではない
i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print('i =', i)
print('j =', j)

# コピーするには…
# この書き方だとyの中身だけ書き換わる
x = [1, 2, 3, 4, 5]
y = x.copy()
# ↑はy = x[:] こう書いても同じだけどcopyの方が明示的で分かりやすい
y[0] = 100
print('x =', x)
print('y =', y)