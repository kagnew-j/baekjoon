import sys
input = sys.stdin.readline
nums = []
for _ in range(2):
    nums.append(int(input()))
ans = []
for ele in range(nums[0],nums[1]+1):
    if ele == 1:
        pass
    else:
        temp = 0
        for i in range(1,ele//2+1):
            if ele%i == 0:
                temp +=1
        if temp == 1:
            ans.append(ele)
if len(ans) == 0:
    print(-1)
else:
    print(sum(ans))
    print(ans[0])
# https://www.acmicpc.net/problem/2581