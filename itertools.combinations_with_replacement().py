<<<<<<< HEAD
from itertools import combinations
=======
from itertools import combinations_with_replacement
>>>>>>> 8866fc696a60a8059b49f2c85b40a603f37634e2

S, k = input().split(' ')

S = sorted(S)
k = int(k)

<<<<<<< HEAD

temp = []
for i in range(1, k + 1):

    for j in combinations(S, i):
        temp.append(''.join(j))


for i in temp:
    print(i)

=======
for i in combinations_with_replacement(S, k):
    print(''.join(i))
>>>>>>> 8866fc696a60a8059b49f2c85b40a603f37634e2
