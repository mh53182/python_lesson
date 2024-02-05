# 58. ラムダ

# 大文字で始まらない誤ったデータがリストに混じっている…
l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']

# def change_words(words, func):
#     for word in words:
#         print(func(word))

# # 全て大文字化するファンクション
# def sample_func(word):
#     return word.capitalize()

# change_words(l, sample_func)


# # ラムダを使うとsample_funcを1行で書ける
# sample_func1 = lambda word: word.capitalize()
# # 小文字化する処理を書いても2行で済む
# # def～で書くと4行になる
# sample_func2 = lambda word: word.lower()

# change_words(l, sample_func1)
# change_words(l, sample_func2)

# # 呼び出しごと1行でラムダにすることも可能
# change_words(l, lambda word: word.capitalize())


# 全部一行で処理するとこうなる
capital_list = list(map(lambda word: word.capitalize(), l))
print(capital_list)