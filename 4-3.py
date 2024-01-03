n = int(input())
list = list(map(int, input().split()))
max=-1000001
min=1000000
for i in range(n):
    if list[i]>max:
        max=list[i]
    if list[i]<min:
        min=list[i]
print(min, max)