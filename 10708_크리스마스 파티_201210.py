n = int(input())
k = int(input())
target_list = list(map(int,input().split()))
score = [0]*n
for i in range(k):
    pred_list = list(map(int,input().split()))
    target = target_list[i]
    for j in range(n):
        if pred_list[j] == target:
            score[j] += 1
        else:
            score[target-1] += 1    
for ele in score:
    print(ele)

# https://www.acmicpc.net/problem/10708