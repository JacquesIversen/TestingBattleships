#legend
# X for placing a ship and hit battleship.
#. " " for available space
#. "-" for missed shot.

from random import int

HIDDEN_BOARD = [(" ") * 8 for x in range(8)]
GUESS_BOARD = [(" ") * 8 for x in range(8)]

letter_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "e": 4, "F": 5, "G": 6, "H": 7}


def print_board():  #Create playing board.
    print(" A B C D E F G H")
    print(" - - - - - - - - - ")
    row_number = 1 
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))  #Pipe betweeen space in Arrays.
        row_number += 1


def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7) #. Imported Random int in line 1. 
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = randint(0,7), randint(0,7)
        board[ship_row][ship_column] = "X"



def get_ship_location(): #Ask user for their placement.
    row = input("Please enter a ship row 1-8")
    while row not in "12345678":  # Loops if not provided correct integer. 
        print("plaese enter a valid row.")
        row = input("Please try again to enter a ship row between 1 & 8") 
    column = input("Please enter a ship column A-H").upper() # # Loops if not provided correct str data
    while column not in "ABCDEFGH":
        print("Please enter a letter between A & H")
        column = input("Please enter a ship column A-H").upper()




def count_hit_ships():
    pass


create_ships()
turns = 10
while turns > 0:


print_board()