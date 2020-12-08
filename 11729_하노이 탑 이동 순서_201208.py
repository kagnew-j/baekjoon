move = []
def hanoi(n,a,b,c):
    if n == 1:
        move.append([a,c])
    else:
        hanoi(n-1,a,c,b)
        move.append([a,c])
        hanoi(n-1,b,a,c)
# print answer
hanoi(int(input()),1,2,3)
print(len(move))
print("\n".join([" ".join(str(i) for i in ele) for ele in move]))

# https://www.acmicpc.net/problem/11729