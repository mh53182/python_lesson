# 78. クラスの定義

# Python3から'(object)'は無くても問題ないが書いてあることが多い　無くてもびっくりしないこと
# classは設計図
class Person(object):
    def say_something(self):
        print('Hello')

# 'person'という変数に'Person'というclassを呼び出す
# ここで呼び出されたものがオブジェクト(実際にメモリを消費する)
person = Person()
person.say_something()