def fibonacci(number:int)->int:
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number-2)


if __name__ == '__main__':
    number:int = 20
    result = fibonacci(number)
    print(f'the fibonacci of {number} is {result}')