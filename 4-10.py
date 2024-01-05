n = int(input())
grade = list(map(int, input().split()))
max=0
avg=0
for i in range(n):
    if grade[i]>max:
        max = grade[i]
for i in range(n):
    grade[i] = grade[i]/max*100
    avg+=grade[i]
avg/=n
print(avg)