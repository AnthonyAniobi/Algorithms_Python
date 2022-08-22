def isSorted(array:list) -> bool:
    '''check if an array is sorted'''
    if len(array)==1:
        return True
    else:
        return array[0]<array[1] and isSorted(array[1:])

if __name__ == '__main__':
    array:list = [1, 2, 3, 4, 5, 3]
    result:bool = isSorted(array)
    print(f'the array: {array} => sorted:{result}')