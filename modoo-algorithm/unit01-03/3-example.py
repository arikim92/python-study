# n명 중 두 명을 뽑아 짝을 짓는다고 할 때 짝을 지을 수 있는 모든 조합을 출력하는 알고리즘을 만들어 보세요.

def connect_user(x):
    for i in range(len(x)-1):
        for j in range(i+1, len(x)):
            if x[ i ] == x[ j ]:
                continue

            print(x[ i ], '-', x[ j ])

name_list = [ 'Tom', 'Jerry', 'Mike', 'John' ]
connect_user(name_list)
