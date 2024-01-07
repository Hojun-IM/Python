n = int(input())
for i in range(n):
    word = input()
    if len(word)==1:
            print(word*2)
            continue
    print('{}{}'.format(word[0], word[len(word)-1]))