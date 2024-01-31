# 65. 例外処理

l = [1,2, 3]
i = 5

# print(l[i])とすると、インデックス5が見つからずにエラーでファイルの実行が終了する

# try/exceptがあれば処理できる
try:
    l[i]
# インデックスエラーのときDon't worry~を出力する
except IndexError as ex:
    print("Don't worry: {}".format(ex))
# NameErrorのとき…
except NameError as ex:
    print(ex)
# 他多くのエラーのとき（あまり好ましくない表記）
except Exception as ex:
    print('other: {}'.format(ex))
# いずれにも当てはまらない場合（＝exceptを全て正常に抜けた場合）
else:
    print('done')
# 必ず実行される
finally:
    print('clean up')