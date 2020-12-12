target = int(input())
temp = 0
for i in range(2,11):
    # conversion
    n = target
    ans = ""
    while True:
        q,r = divmod(n,i)
        ans = str(r) + ans
        if q == 0:
            break
        n = q
    # pallindrome
    if ans == ans[::-1]:
        print(str(i), ans, sep = " ")
        temp += 1
if temp == 0:
    print("NIE")

# https://www.acmicpc.net/problem/8611