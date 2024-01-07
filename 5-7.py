n = int(input())
for i in range(n):
    r, word = input().split()
    for j in word:
        print(j*int(r), end='')
    print()