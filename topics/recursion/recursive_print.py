def recursivePrint(number:int) ->None:
    if number == 0:
        return 0
    else:
        print(number)
        return recursivePrint(number -1)


if __name__ == '__main__':
    number:int = 10
    recursivePrint(number)