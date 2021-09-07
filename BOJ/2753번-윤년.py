# 윤년이면 1, 아니면 0을 출력하는 프로그램
# 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때
# 연도는 1보다 크거나 같고, 4000보다 작거나 같은 자연수
year = int(input())
assert 1 <= year <= 4000

ans = 1 if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0) else 0
print(ans)
