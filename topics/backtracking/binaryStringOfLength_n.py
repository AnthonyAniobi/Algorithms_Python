def binaryStringOfLength(n:int):
    if n == 0:
        return []
    elif n == 1:
        return ['0', '1']
    else:
        return appendBehind(binaryStringOfLength(n-1))

def appendBehind(array:list) -> list:
    return [x+'0' for x in array] + [x+'1' for x in array]


if __name__ == '__main__':
    n = 3
    result:list = binaryStringOfLength(n)
    print(f'the binary string of length {n} is {result}')