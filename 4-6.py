n, m = map(int, input().split())
list = [i for i in range(1, n+1)]
for a in range(m):
    i , j = map(int, input().split())
    tmp = list[i-1]
    list[i-1] = list[j-1]
    list[j-1] = tmp
for a in range(n):
    print(list[a], end=' ')