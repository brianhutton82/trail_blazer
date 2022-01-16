import random, time
from os import system as sys

"""
make game so that if user does not eat all fruit within the minimum number of moves then player loses
"""

class Board:
    def __init__(self, size, num_fruits):
        self.arr = []
        for i in range(size):
            self.arr.append([])
        for i in range(len(self.arr)):
            for j in range(size):
                self.arr[i].append(' ')
        self.fruits = num_fruits
        for i in range(num_fruits):
            x = random.randrange(0,size)
            y = random.randrange(0,size)
            self.arr[y][x] = '@'
    def prnt(self):
        print("\t+{0}+".format('-'*len(self.arr)))
        current = ''
        for i in range(len(self.arr)):
            for j in range(len(self.arr[i])):
                current += self.arr[i][j]
            print("\t|{0}|".format(current))
            current = ''
        print("\t+{0}+".format('-'*len(self.arr)))
    def eat_fruit(self):
        self.fruits -= 1

class Player:
    def __init__(self,pos,board):
        self.x = pos[0]
        self.y = pos[1]
        board.arr[self.y][self.x] = 'o'
    def move(self,direction,board):
        board.arr[self.y][self.x] = 'x'
        if(direction == 'w'):
            self.y -= 1
        elif(direction == 's'):
            self.y += 1
        elif(direction == 'a'):
            self.x -= 1
        elif(direction == 'd'):
            self.x += 1
        if(board.arr[self.y][self.x] == '@'):
            board.eat_fruit()
        board.arr[self.y][self.x] = 'o'

def print_title(title):
    print("\t{0}".format('-'*len(title)))
    print("\t{0}".format(title))
    print("\t{0}".format('-'*len(title)))

def update(p1, board):
    print_title("TRAIL-BLAZE")
    board.prnt()
    direction = input("\tDirection: ")
    p1.move(direction,board)
    while(direction != 'q' and board.fruits > 0):
        sys('clear')
        print_title("TRAIL-BLAZE")
        board.prnt()
        direction = input("\tDirection: ")
        p1.move(direction, board)
    if(board.fruits == 0):
        print("\n\tWINNER!")
    else:
        print("\n\tGOODBYE!")

size = int(input("Enter size of board: "))
fruits = random.randrange(1,10)
board = Board(size, fruits)
origin = (size//2,size//2)
p1 = Player(origin,board)
update(p1,board)


