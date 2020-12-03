# 동명이인을 찾는 알고리즘
# n명의 사람 이름 중에서 같은 이름을 찾아 집합으로 만들어 돌려주는 알고리즘을 만들어 보세요.

# # Set (집합)(자료의 순서는 무관함)
# len(s): 길이
# add(x): 맨 뒤에 추가
# discard(x): x가 집합에 있으면 삭제
# clear(): 비우기
# x in s: x가 집합 s안에 있는지 확인한다 (x not in s 는 반대)

# 1. 첫번째 Tom 을 뒤의 3사람과 비교한다.
# 2. 마지막 Tom 과 첫번째 Tom 은 동명이인이다.
# 3. 두번째 Jerry 를 뒤의 2사람과 비교한다.
# 4. 세번째 Mike 를 뒤의 Tom 과 비교한다.
# 5. Tom 은 이미 비교했다.


def find_same_name(x):
	result = set()  # set 으로하면 중복을 제거할 수 있다
	for i in range(len(x)-1):  # len(x)-1 은 마지막 Tom을 비교하지 않는 5번에 해당됨
		for j in range(i+1, len(x)):  # i+1 은 뒤로 갈 수록 서로 비교한 값들(중복) 제하기 위한 작업
			if x[ i ] == x[ j ]:
				result.add(x[ i ])

			# print(x[ i ], x[ j ])
	print("result", result)

name_list = [ 'Tom', 'Jerry', 'Mike', 'Tom' ]
find_same_name(name_list)  # Tom
