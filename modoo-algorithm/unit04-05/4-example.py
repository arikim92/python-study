# 4-1. 1부터 n까지의 합 구하기를 재귀 호출로 만드시오
# 4-2. 숫자 n개 중에서 최댓값 찾기를 재귀 호출로 만드시오
# 4-3. 0과 1부터 시작해서 바로 앞의 두 수를 더한 값을 다음 값으로 추가하는 방식으로 만든 수열을 피보나치 수열이라고 합니다.
#      즉 0+1=1, 1+1=2, 1+2=3 이므로 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ...
#      0부터 시작한다고 가정할 때 n번째 피보나치 수를 구하는 알고리즘을 재귀 호출을 이용해서 구현해 보세요.

# [ RESULT ]
#    [unit1] 1부터 4까지 더하기: 10
#    [unit2] 최댓값 찾기: 94
#    [unit4] 피보나치 수열: [0, 1, 1, 2, 3, 5, 8]

# 재귀 - 1부터 더하기
def unit1(n):
    if n <= 1:
        return 1
    else:
        return n + unit1(n - 1)


# 재귀 - 최댓값 찾기
def unit2(n):
    if len(n) <= 1:
        return n[0]
    else:
        if n[0] > n[1]:
            n.pop(1)
        else:
            n.pop(0)

        return unit2(n)


# 재귀 - 피보나치 수열
def unit4(fibonacci, n):
    if n < 1:
        return fibonacci
    else:
        fibonacci.append(fibonacci[-2] + fibonacci[-1])
        n = n - 1
        return unit4(fibonacci, n)


# 재귀 - 피보나치 수열 마지막 값
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 2) + fibo(n - 1)


print('[unit1] 1부터 4까지 더하기:', unit1(4))

li = [17, 23, 1, 76, 94, 25, 45]
print('[unit2] 최댓값 찾기:', unit2(li))

# 0 + 1 = 1
# 1 + 1 = 2
# 1 + 2 = 3
# 2 + 3 = 5
# 3 + 5 = 8
# 5 + 8 = 13
# .
# .
fibonacci = [0, 1]
print('[unit4] 피보나치 수열:', unit4(fibonacci, 5))
print('[fibo] 피보나치 수열:', fibo(5))
