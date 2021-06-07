S = input()
S += ' '

mylist = []
count = 1

for i in range(len(S) - 1):
    if S[i] == S[i + 1]:
        count += 1
    else:
        mylist.append((count, int(S[i])))
        count = 1

for i in mylist:
    print(i, end = ' ')

