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


print('######################')

# 79. クラスの初期化とクラス変数

class Person2(object):
    def __init__(self, name):
        self.myname = name

    def say_something(self):
        print('I am {}. Hello'.format(self.myname))

person = Person2('Mike')
person.say_something()