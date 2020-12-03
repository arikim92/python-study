# 주어진 숫자 n개 중 가장 큰 숫자를 찾는 알고리즘
# 입력: n
# 출력: 가장 큰 숫자

# # list 기능
# append(x): 맨 뒤에 추가
# insert(i, x): i번째 위치에 x를 추가
# pop(i): i번째 위치를 반환하고 리스트에서 지운다
# clear(): 리스트를 비운다
# x in a: x가 리스트 a안에 있는지 확인한다 (x not in a 는 반대)

def find_max_num(n):
	max_num = 0
	for i in range(len(n)):
		# 현재 저장된 제일 큰 수보다 현재 값이 크다면?
		if n[i] > max_num:
			max_num = n[i]
	print(max_num)


li = [ 17, 23, 1, 76, 94, 25, 45 ]
find_max_num(li)  # 94

# 응용
# 리스트에 숫자가 n개 있을 때 가장 큰 값이 있는 위치 번호를 돌려주는 알고리즘

def find_max_index(n):
	max_index = 0
	for i in range(len(n)):
		# 현재 저장된 제일 큰 수보다 현재 값이 크다면?
		if n[i] > n[max_index]:
			max_index = i
	print(max_index)

find_max_index(li)  # 4
