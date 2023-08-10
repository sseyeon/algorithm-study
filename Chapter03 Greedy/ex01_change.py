# - 문제
# 거스름돈으로 사용할 수 있는 동전은 500원, 100원, 50원 10원
# 손님에게 거슬러 줘야 할 돈이 N원일 때, 거슬러줘야 할 동전의 최소 갯수는 ?

# - 핵심
# 가장 큰 화폐 단위부터 거슬러 주기

n = 1260 
count = 0

# 큰 단위의 화폐부터 차례대로 확인 
coin_types = [500, 100, 50, 10]
for coin in coin_types:
	count += n // coin
	n %= coin 

print(count)