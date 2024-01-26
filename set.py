# 28.集合

# 重複するデータは省かれる
a = {1, 2, 3, 3, 4, 4, 4, 5, 6}
type(a)
print(a)

b = {2, 3, 6, 6, 7}
print(b)

# ユニーク化したデータ同士の除算が可能
x = a - b
print(x)

y = b - a
print(y)

# aかつbに含まれるデータ
z = a & b
print(z)

# aまたはbに含まれるデータ
s = a | b
print(s)

# aまたはbに含まれるが重複しないデータ
t = a ^ b
print(t)

print('##############################')


# 29.集合のメソッド

# 集合にはインデックスが無いので"[]"でデータを呼ぶ出すことはできない
# 追加は可能
s.add(8)
print(s)

# 削除も可能
s.remove(6)
print(s)

# 空にもできる
s.clear()
print(s)

print('##############################')


# 30.集合の使いどころ

# 共通の友人は？
my_friands = {'A', 'B', 'C'}
A_friends = {'C', 'D', 'E'}
print(my_friands & A_friends)

# 買った果物の種類は？
# アプリケーションでユーザーが購入したものを保存するにはリストを使う
bought = ['apple', 'banana', 'apple', 'banana']
# これだと買ったものが全部でちゃう。
print(bought)

# 買った種類を表示するためリストを集合に変換＝重複しなくなる
kind = set(bought)
print(kind)