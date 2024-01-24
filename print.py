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