M = input()
a = set(map(int, input().split(' ')))
N = input()
b = set(map(int, input().split(' ')))



s = a.union(b) - a.intersection(b)
for i in sorted(s):
    print(i)