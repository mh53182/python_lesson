# ターミナルで"python"と入力すると対話型の操作が可能
# 割り算はスラッシュで可能
# 割り切れない数値をitegerで求めるにはスラッシュを2つ重ねる
# べき乗はアスタリスクを2つ重ねて何回掛けるか指定　※"5 ** 2"は5の二乗

# round関数
pie = 3.1415926
print(round(pie, 2))
# shellでこのように入力すると小数点以下2桁に丸めて表示される

# 対話型shellは"exit()"またはCtrl-Zで抜けられる


# 数学のライブラリ"math"をインポート
import math

# sqrtは平方根を求める
result = math.sqrt(25)
print(result)

# help関数　※下記の場合はmathのドキュメントを表示
print(help(math))