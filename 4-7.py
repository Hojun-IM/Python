list = [0 for i in range(31)]
for i in range(1, 29):
    a = int(input())
    list[a]=1
for i in range(1, 31):
    if list[i]==0:
        print(i)