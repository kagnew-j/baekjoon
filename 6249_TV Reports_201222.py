n, l, u = map(int,input().split())
temp = 0
for i in range(n):
    update = int(input())
    if update > u:
        print("BBTV: Dollar reached {} Oshloobs, A record!".format(update))
        u = update
    elif temp != 0: 
        if temp > update:
            print("NTV: Dollar dropped by {} Oshloobs".format(temp-update))        
    else:
        if l > update:
            print("NTV: Dollar dropped by {} Oshloobs".format(l-update))
    temp = update

# https://www.acmicpc.net/problem/6249