def solve(case_index, required:str, entry:str):
    required_index = 0
    for index in range(len(entry)):
        if required_index>=len(required):
            break
        if(required[required_index]==entry[index]):
            required_index+=1
    if required_index == len(required):
        return f'Case #{case_index}: {len(entry)-len(required)}'
    else:
        return f'Case #{case_index}: IMPOSSIBLE'
        

test_cases = int(input())
input_value = list()

for i in range(test_cases*2):
    input_value.append(input())
    
for val in range(test_cases):
    required = input_value[val*2]
    entry = input_value[(val*2)+1]
    
    print(solve(val+1, required, entry))
    