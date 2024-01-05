n, m = map(int, input().split())
basket = [i for i in range(1,n+1)]
for a in range(m):
    i, j = map(int, input().split())
    tmp_basket = basket[i-1:j]
    tmp_basket.reverse()
    basket[i-1:j] = tmp_basket
for a in range(n):
    print(basket[a], end=' ')