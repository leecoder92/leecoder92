#그리디: 거스름돈 문제
n = 1260 #받은 돈
count = 0 #동전 갯수
coins = [500,100,50,10] #동전 종류

for coin in coins:
    count += n//coin
    n %= coin

print(count)
