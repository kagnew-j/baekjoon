while True:
    try:
        n,p = map(int,input().split())
        ans = []
        if p%2 == 0:
            ans.append(p-1)
            ans.append(p)
        else:
            ans.append(p)
            ans.append(p+1)
        idx = (p+1)//2
        half = n//2
        if p < half+1:
            ans.append(2*(half+1-idx)-1)
            ans.append(2*(half+1-idx))
        else:
            ans1 = []
            ans1.append(2*(half+1-idx)-1)
            ans1.append(2*(half+1-idx))
            ans =  ans1 + ans
        for ele in ans:
            if ele != p:
                print(ele, end = " ")
    except:
        break

# https://www.acmicpc.net/problem/9437