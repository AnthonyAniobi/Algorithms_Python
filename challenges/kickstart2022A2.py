def solve(test_case:int, number:str):

    number_sum = 0
    for x in range(len(number)):
        number_sum += int(number[x])
    remainder = 0
    if number_sum<9:
        remainder = 9-number_sum
    else:
        remainder = 9%number_sum
    if remainder < int(number[0]):
        return f'Case #{test_case}: {remainder}{number}'
    else:
        return f'Case #{test_case}: {number}{remainder}'


test_cases = int(input())

for i in range(test_cases):
    number = input()
    print(f'number is: {number}')
    print(solve(i+1,number))