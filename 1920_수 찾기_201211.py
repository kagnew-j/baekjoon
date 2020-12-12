di = {}
n = int(input())
li = list(map(int,input().split()))
for ele in li:
    di[ele] = 1
n = int(input())
li = list(map(int,input().split()))
for ele in li:
    try :
        print(di[ele])
    except :
        print(0)
        
# https://www.acmicpc.net/problem/1920