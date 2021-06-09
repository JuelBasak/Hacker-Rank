from itertools import combinations

S, k = input().split(' ')

S = sorted(S)
k = int(k)


temp = []
for i in range(1, k + 1):

    for j in combinations(S, i):
        temp.append(''.join(j))


for i in temp:
    print(i)

