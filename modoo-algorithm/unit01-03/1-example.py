# 1부터 n까지 연속한 숫자의 제곱의 합을 구하는 프로그램을 for 반복문으로 만들어 보세요.

# 제곱 구하기: x ** 2

# 1-1 for문 사용하기
def calculation_for(n):
    result = 0
    for i in range(1, n+1):
        result += i ** 2
    print('for/ 결과는 [', result, '] 입니다!')


# 1-3 공식 사용하기
def calculation(n):
    result = (n * (n + 1) * (2*n + 1)) // 6
    print('공식/ 결과는 [', result, '] 입니다!')


calculation_for(10)  # 결과 385
calculation(10)  # 결과 385
