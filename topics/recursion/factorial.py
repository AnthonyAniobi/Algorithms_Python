def factorial(number:int) -> int:
    '''A recursive function to calculate factorial of a number'''
    if(number==0):
        return 1
    else:
        return number*factorial(number-1)
    


if __name__ == '__main__':
    number:int = 5
    result = factorial(number)
    print(f'The factorial of ${number} is ${result}')