# 9.まずはprintで出力

# カンマ区切りの文字列は、半角スペース' '区切りで出力される
print('Hi' , 'Mike')

# セパレーション'sep= 'で区切り文字を指定可能
# 'Hi,Mike'と出力
print('Hi', 'Mike', sep=',') 

# 'end='で行末の表示を指定可能
# '\n'で改行　※デフォルトのため、これだけで終わる場合は指定不要
print('Hi', 'Mike', sep=',', end='\n')

# 下記は行末にピリオドも表示
print('Hi', 'Mike', sep=',', end='.\n')


# 11.文字列

# シングルクォートでも
print('Hallo')
# ダブルクォートでもOK
print("Hallo")

# 中身にシングルクォートがあればダブルクォートで囲む
print("I don't know")

# どうしてもシングルクォートで囲むならデータ内のシングルクォート前にバックスラッシュ
print('I don\'t know')

# ダブルクォート入りデータはシングルクォートで囲む
print('say "I don\'t know"')

# ダブルクォートでダブルクォートを囲むならバックスラッシュ
print("say \"I don't know\"")

# \nで改行
print('Hello.\nHow are you?')

# データ内に"/n"があるときは生(raw)データとして先頭に"r"をつける
print(r'C:\name\name')

# \nを使わず見た通りに改行するにはダブルクォート3つで囲む
# ※ダブルクォート前後の改行も丁寧に改行されるので、1行目と最終行はダブルクォートに繋げるorバックスラッシュを入れる
print("""\
1111
2222
3333
4444\
""")


# 12.文字列のインデックスとスライス

# 変数に代入した文字列にはrubyの配列のようなインデックスが振られている　※最初から、や、最後まで、は省略可
word = 'python'
print(word[0])
print(word[1])
print(word[-1])
print(word[0:2])
print(word[:2])
print(word[2:])

# 1文字目を'j'に変更して代入する場合
word = 'j' + word[1:]
print(word[:])

# 長さ(文字数)を数える
n = len(word)
print(n)


# 13.文字のメソッド

s = 'My name in Mike. Hi Mike.'
print(s)

# 文字列は'My'で始まっているか？　を判定するメソッド
is_start = s.startswith('My')
print(is_start)

print(s.find('Mike'))


# 14.文字の代入