def kAryStringOfLengthN(k:int, n:int):
    if n==0:
        return []
    elif n==1:
        return [str(x) for x in range(k)]
    else:
        return appendToBack(k, kAryStringOfLengthN(k, n-1))


def appendToBack(k:int, l:list)->list:
    temp:list = []
    for i in range(k):
        temp += [x+str(i) for x in l]
    return temp


if __name__ == '__main__':
    k = 3
    n = 4
    result = kAryStringOfLengthN(k, n)
    print(f'The kary String with k={k} and n={n} gives:\nresult:{result}')