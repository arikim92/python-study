# [ RESULT ]
#    1부터 n까지 연속한 숫자의 합 구하는 프로그램입니다.
#    더하려는 숫자를 1보다 크게 알려주세요!
#    --> 100
#    for/ 결과는 [ 5050 ] 입니다!
#    while/ 결과는 [ 5050 ] 입니다!
#    calculation/ 결과는 [ 5050 ] 입니다!

# 문제: 1부터 n까지 연속한 숫자의 합 구하기

# 알고리즘: 입력을 출력으로 만드는 과정
# 입력: n
# 출력: 숫자의 합
# 계산방법: 1+2+3+4+5 ...
# (((1+2)+3)+4) ...
# 1+2=3, 3+3=6, 6+4=10, ...

# for문으로 결과 구하기
def calculation_for(n):
    result = 0
    # 0 때문에 1 추가
    for i in range(n+1):  # (1, n+1) 도 가능한데 js 에서 1부터 더한적이 없어서 어색하다 ;;
        result += i
    print('for/ 결과는 [', result, '] 입니다!')


# while문으로 결과 구하기
def calculation_while(n):
    i = 0
    result = 0
    while i < n:
        i = i + 1  # 1부터 더할꺼라서 1을 우선 추가한다
        result += i
    print('while/ 결과는 [', result, '] 입니다!')


# 공식으로 결과 구하기
def calculation(n):
    result = n * (n + 1) // 2
    print('calculation/ 결과는 [', result, '] 입니다!')


print('1부터 n까지 연속한 숫자의 합 구하는 프로그램입니다.')
x = int(input('더하려는 숫자를 1보다 크게 알려주세요!\n --> '))

if x < 2:
    print('숫자를 잘못 입력하셔서 종료합니다.')

else:
    calculation_for(x)
    calculation_while(x)
    calculation(x)
