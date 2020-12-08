quad = [0,0,0,0,0] #quadrant 0:axis
for _ in range(int(input())):
    a, b = map(int,input().split())
    if a == 0 or b == 0:
        quad[0] += 1
    elif a > 0:
        if b>0:
            quad[1] += 1
        else:
            quad[4] += 1
    else:
        if b>0:
            quad[2] += 1
        else:
            quad[3] += 1
# print answer
print("Q1:",str(quad[1]), sep = " ")
print("Q2:",str(quad[2]), sep = " ")
print("Q3:",str(quad[3]), sep = " ")
print("Q4:",str(quad[4]), sep = " ")
print("AXIS:",str(quad[0]), sep = " ")

# https://www.acmicpc.net/problem/9610