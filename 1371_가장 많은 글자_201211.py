di = {}
while True:
    try:
        text = input()
        for ele in text:
            if ele == " ":
                pass
            else:
                di[ele] = di.get(ele,0)+1
    except:
        break
answer = sorted(di.items(), key = lambda x:x[0])
answer = sorted(answer, key = lambda x:x[1], reverse = True)
ans = ""
target = 0
for i in range(len(answer)):
    if i == 0 :
        target = answer[i][1]
        ans += answer[i][0]
    elif target == answer[i][1]: 
        ans += answer[i][0]
    else:
        break
print(ans)

# https://www.acmicpc.net/problem/1371