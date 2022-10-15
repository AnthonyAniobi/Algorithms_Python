def solution(test_case:int, john_list:list, other_list:list):
    matrix = []
    for i in range(len(other_list[0])):
        max_value = 0
        for l in range(len(other_list)):
            if max_value < other_list[l][i]:
                max_value = other_list[l][i]
        matrix.append(max_value)
    
    john_required:int = 0

    for o in range(len(matrix)):
        if john_list[o] < matrix[o]:
            john_required += matrix[o]-john_list[o]

    print(f'Case #{test_case}: {john_required}')


test_case = int(input())
for t in range(test_case):
    m , n, p = [int(x) for x in input().split(' ')]
    j_list = []
    other_list = []
    for m_1 in range(m):
        if m_1 == p:
            j_list = [int(j_l) for j_l in input().split(' ')]
        else:
            other_list.append([int(o_l) for o_l in input().split(' ')])
    solution(t+1, j_list, other_list)    

#     pass
# jl1 = [1000, 2000, 3000]
# ol1 = [[1500, 1500, 3000]]

# jl2 = [500, 4000]
# ol2 = [[1500, 4000],[1000, 2000]]
# solution(jl2, ol2)
