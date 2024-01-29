num = 1
name = '1'

new_num = int(name)

print(new_num, type(new_num))

print('########################')

# return文演習
# https://aiacademy.jp/texts/show/?id=572

def gen_text(text, num):
    return text * num

text = gen_text("繰り返したい文字", 3)
print(text)