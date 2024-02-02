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


print('##########################')

# 66. 独自例外の作成

# Exception を継承して自作のエラー(ここでは'UppercaseError')を作る
class UppercaseError(Exception):
    pass

# raise文で明示的にエラーを起こす
def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)
        
# 直接checkファンクションを実行すると"UppercaseError: APPLE"が出力される
# check()

# try exceptを使って、自作エラーに引っかかった際の処理を行う
try:
    check()
except UppercaseError as exc:
    print('This is my fault. Go next')
# ※独自エラーにPython本来のエラー名を使わない方がベター
# Pythonのエラーが出ているように見えると、その対応が必要だと思われるため