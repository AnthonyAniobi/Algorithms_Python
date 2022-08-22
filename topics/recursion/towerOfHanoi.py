def towerOfHanoi(num:int)->None:
    '''tower of hanoi solution for num tiles'''
    moves(num, source='source', auxilliary='auxilliary', destination='destination')
    print('solved')

def moves(num:int, source:str, auxilliary:str, destination:str):
    '''moves for the tower of hanoi problem'''
    if num:
        moves(num-1, source, destination, auxilliary)
        print(f'move tile {num} from {source} to {destination}')
        moves(num-1, auxilliary, source, destination)

if __name__ == '__main__':
    number:int = 3
    towerOfHanoi(number)