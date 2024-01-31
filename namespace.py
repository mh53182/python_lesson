# 64. 名前空間とスコープ

animal = 'cat'

def f():
    # グローバル変数を関数内でローカル変数として上書きはできる
    # 関数内で再宣言しているものを先に呼び出すと、グローバル変数が使われるのではなくエラーになる
    # print(animal)　←これはエラー
    animal = 'dog'
    print('local', animal)

f()
print('global', animal)

print('#######################')

drink = 'coffee'

def f():
    # グローバル変数をグローバル変数として上書きすることも可能
    global drink
    drink = 'water'
    print('local', drink)

# 以下の呼び出しはどちらも水になる
f()
print('global', drink)