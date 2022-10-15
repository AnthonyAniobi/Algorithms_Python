def solution(test_case:int, radius, r_list:list, y_list:list):
    if len(y_list)==0 and len(r_list)>0:
        result = check_count_empty(radius,  r_list)
        return f'Case #{test_case}: {result} 0'
    if len(r_list)==0 and len(y_list)>0:
        result = check_count_empty(radius,  y_list)
        return f'Case #{test_case}: 0 {result}'
    r_list.sort()
    y_list.sort()    
    if r_list[0]< y_list[0]:
        result = check_count(radius, y_list[0], r_list)
        return f'Case #{test_case}: {result} 0'
    else:
        result = check_count(radius, r_list[0], y_list)
        return f'Case #{test_case}: 0 {result}'

def check_count(radius, check, check_list):
    checker = 0
    check_index = 0
    while check_list[check_index] < check:
        if check_list[check_index]<= radius:
            checker +=1
        check_index+=1
    return checker

def check_count_empty(radius, check_list):
    checker = 0
    for val in check_list:
        if val<= radius:
            checker +=1
    return checker


def calc_abs(s_str):
    s_list = [int(x) for x in s_str.split(' ')]
    y_i = s_list[0]**2
    x_i = s_list[1]**2
    return (x_i + y_i)**(0.5)

test_case = int(input())
for t in range(test_case):
    r_h, r_s = [int(r) for r in input().split(' ')]
    n = int(input())
    n_red_list = []
    for n_i in range(n):
        n_red_list.append(calc_abs(input()))
    m = int(input())
    m_red_list = []
    for m_i in range(m):
        m_red_list.append(calc_abs(input()))
    print(solution(t+1, r_h+r_s, n_red_list, m_red_list))
