

HIDDEN_BOARD = [(" ") * 8 for x in range(8)]
GUESS_BOARD = [(" ") * 8 for x in range(8)]

letter_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "e": 4, "F": 5, "G": 6, "H": 7}


def print_board(): #Create playing board.
    print(" A B C D E F G H")
    print(" - - - - - - - - - ")


def create_ships():
    pass


def get_ship_location(): #Ask user for their placement.
    pass


def count_hit_ships():
    pass


create_ships()
turns = 10
while turns > 0:


print_board()