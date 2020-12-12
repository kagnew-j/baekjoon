s1,s2,s3 = map(int,input().split())
di = {}
for i in range(1,s1+1):
    for j in range(1,s2+1):
        for k in range(1,s3+1):
            di[i+j+k] = di.get(i+j+k, 0) + 1
ans = sorted(di.items(), key = lambda x : x[1], reverse = True)
print(ans[0][0])

# https://www.acmicpc.net/problem/1233