a = list(map(int,input().split()))
b = list(map(int,input().split()))
answer = []
ascore = 0
bscore = 0
for i in range(len(a)):
    if a[i] < b[i]:
        bscore += 3
        answer.append('B')
    elif a[i] > b[i]:
        ascore += 3
        answer.append('A')
    else:
        ascore += 1 
        bscore += 1
        #answer.append('d')
print(ascore, bscore, sep = " ")
if ascore < bscore:
    print("B")
elif ascore > bscore:
    #print(ascore, bscore, sep = " ")
    print("A")
else:
    #print(bscore, ascore, sep = " ")
    if len(answer) == 0:
        print('D')
    else:
        print(answer[-1])

# https://www.acmicpc.net/problem/2511