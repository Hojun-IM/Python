h, m = map(int, input().split())
take = int(input())

h+=take//60
m+=take%60

if m>59:
    h+=1
    m-=60
if h>23:
    h-=24
print(h, m)