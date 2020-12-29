def mean(nums):
    return round(sum(nums)/len(nums))

def median(nums):
    nums.sort()
    mid = nums[len(nums)//2]
    return mid

def mode(nums):
    from collections import Counter
    mode_dict = Counter(nums)
    modes = mode_dict.most_common()
    if len(nums)>1:
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else:
            mod = modes[0][0]
    else:
        mod = modes[0][0]
    return mod
    
def scope(nums):
    return max(nums)-min(nums)

import sys
input = sys.stdin.readline
li = []
for _ in range(int(input())):
    li.append(int(input()))
print(mean(li))
print(median(li))
print(mode(li))
print(scope(li))

# https://www.acmicpc.net/problem/2108