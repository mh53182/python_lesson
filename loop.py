# 39．while文とcontinue文とbreak文

count = 0
while count < 5:
    print(count)
    count += 1

count = 0
while True:
    if count >= 5:
        break
    print(count)
    count += 1

# continueは続きの処理に行かずにloopの先頭に戻る
count = 0
while True:
    if count >= 5:
        break

    # countが2の時この処理に入る
    if count == 2:
        count += 1
        # continueで戻るので"2"は出力されない
        continue

    print(count)
    count += 1

print('########################')

# 40. while else文

count = 0
while count < 5:
    print(count)
    count += 1
else:
    print('done')

print('########################')

# 41. input関数

while True:
    word = input('入力してください')
    if word == 'OK':
        break
    print('次へ')

print('########################')

# 42. for文とbreak文とcontinue文

some_list = [1, 2, 3, 4, 5]

i = 0
while i < len(some_list):
    print(some_list[i])
    i += 1

for i in some_list:
    print(i)