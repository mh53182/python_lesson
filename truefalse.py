# 37.値がはいっているか判定

# 以下のどの場合もOKが出力される
is_ok = True
is_ok = 1
is_ok = 'a'
is_ok =[1, 2, 3]
is_ok = ('a', 'b', 'c')
is_ok = {1:'a', 2:'b', 3:'c'}
is_ok = {'x', 'y', 'z'}

# is_ok == True と書かなくてもTrueなら、という意味になる。
if is_ok:
    print('OK')
else:
    print('NO')

# 以下はNOが出力される
is_ok = False
is_ok = 0
is_ok = ''
is_ok =[]
is_ok = ()
is_ok = {}
is_ok = set()
