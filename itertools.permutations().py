from itertools import permutations

S, k = input().split(' ')

k = int(k)

temp = []
for i in permutations(S, k):
    temp.append(''.join(i))

for i in sorted(temp):
    print(i)
