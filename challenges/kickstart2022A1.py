def solve(case_index, required:str, entry:str):
    modifiable_count = 0
    entry_index = 0
    for index in range(len(required)):
        if(entry[entry_index]==required[index]):
            entry_index+=1
        else:
            modifiable_count += 1
    if entry_index <= len(required)-1:
        return f'Case #{case_index}: {modifiable_count}'
    else:
        return f'Case #{case_index}: IMPOSSIBLE'

# input_value = input().split('\n')
input_value = '''
2
aaaa
aaaaa
bbbbb
bbbbb
'''

input_value = input_value.strip()
input_value = input_value.split('\n')
test_cases =  int(input_value[0])
typing_test_cases = (len(input_value)-1)//2

for val in range(typing_test_cases):
    required = input_value[val*2]
    entry = input_value[(val*2)+1]
    
    print(solve(val+1, required, entry))
    