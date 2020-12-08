for i in range(int(input())):
    num = 0
    gpa = 0
    for j in range(int(input())):
        a,b=map(float,input().split())
        num += int(a)
        gpa += a*b
    print(num, round(gpa/num,1), sep = " ")

# https://www.acmicpc.net/problem/10984