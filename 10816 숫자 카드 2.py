n = int(input())
li = map(int,input().split())
k = int(input())
li2 = map(int,input().split())
di = {}
for i in li:
    di[i] = di.get(i,0) + 1
print(" ".join([str(di[ele]) if ele in di else '0' for ele in li2]))