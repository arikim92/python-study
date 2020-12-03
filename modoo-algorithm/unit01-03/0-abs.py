# 절대값 구하는 알고리즘

# 1. 값이 0보다 큰지, 작은지 구별
# 0보다 크다면 return
# 0보다 작으면 - 를 붙여서 return

print('절대값을 구해주는 프로그램입니다.')
x = int(input('숫자만 입력해주세요!'))

# x.isalpha(), x.isdigit() : 문자, 숫자 구분하는 함수..

if x >= 0:
    print(x)
elif x < 0:
    print(-x)
else:
    print('숫자가 아니여서 종료됩니다.')
