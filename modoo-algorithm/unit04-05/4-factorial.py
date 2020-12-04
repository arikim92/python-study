# 1부터 n까지 연속한 정수의 곱을 구하는 알고리즘을 만들어 보세요.

# 기본 연산
def factorial1(n):
    # 0 곱하면 안됨 !
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


# 재귀
def factorial2(n):
    if n <= 1:  # 종료 조건
        return 1
    else:
        return n * factorial2(n - 1)


print(factorial1(4))
print(factorial2(4))
