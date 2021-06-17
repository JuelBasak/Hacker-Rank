n = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range(N):
    command = input()

    if command == 'pop':
        s.pop()

    elif command.split(' ')[0] == 'discard':
        s.discard(eval(command.split(' ')[1]))

    elif command.split(' ')[0] == 'remove':
        s.remove(eval(command.split(' ')[1]))    
    

print(sum(s))