import sys
input = sys.stdin.readline
nums = list(map(int,input().split()))
# create sieve
if nums[1] < 2:
    sieve = [False]*(nums[1]+1)
else:
    sieve = [False,False] + [True]*(nums[1]-1)
primes = []
# start sieve
for i in range(2,nums[1]+1):
    if sieve[i]:
        primes.append(i)
        for j in range(2*i, nums[1]+1, i):
            sieve[j] = False
# print answer
for i in range(nums[0],nums[1]+1):
    if sieve[i]:
        print(i)
# https://www.acmicpc.net/problem/1929