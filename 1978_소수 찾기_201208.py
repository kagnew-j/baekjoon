import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int,input().split()))
cnt = 0
for ele in nums:
    if ele == 1:
        pass
    else:
        temp = 0
        for i in range(1,ele//2+1):
            if ele%i == 0:
                temp +=1
        if temp == 1:
            cnt += 1   
print(cnt)
# https://www.acmicpc.net/problem/1978