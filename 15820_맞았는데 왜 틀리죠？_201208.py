s1, s2 = map(int,input().split())
temp = 0
for i in range(s1):
    a,b = map(int,input().split())
    if a != b :
        temp += 1
idx = 0
if temp == 0:
    for j in range(s2):
        a,b = map(int,input().split())
        if a != b :
            idx += 1
else:
    pass
if temp != 0:
    print("Wrong Answer")
else:
    if idx != 0:
        print("Why Wrong!!!")
    else:
        print("Accepted")
        
# https://www.acmicpc.net/problem/15820