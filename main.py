def main():
    leap_year_check()

def leap_year_check():
    T = int(input())
    N = int(input())

    if N % 400 == 0:
        print(N, "is a leap year")

    elif N % 4 == 0 and N % 100 != 0:
        print(N, "is a leap year")

    else:
        print(N, "is not leap year")

if __name__ == "__main__":
    main()

# 西暦が4で割り切れる年は閏年。
# ただし、100で割り切れる年は閏年ではない。
# ただし、400で割り切れる年は閏年。

# input_line = int(input())
# for i in range(input_line):
#     s = input().rstrip().split(' ')
#     print("hello = "+s[0]+" , world = "+s[1])