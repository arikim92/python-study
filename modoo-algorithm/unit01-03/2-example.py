# 숫자 n개를 리스트로 입력받아 최솟값을 구하는 프로그램

def find_min_num(n):
    # 최댓값은 0으로 설정해도 되지만 최솟값은 0이 아닐수도 있기 때문에 0번으로 설정
    min_num = n[0]
    for i in range(len(n)):
        if n[i] < min_num:
            min_num = n[i]
    print(min_num)


li = [ 17, 23, 1, 76, 94, 25, 45 ]
find_min_num(li)
