# dungeon treasure map
import random

grid_width = int(input("Enter dungeon width: "))
grid_height = int(input("Enter dungeon height: "))

board = []
numberOfUndiscoveredTreasures = 0

def create_grid(width, height):
    global board, numberOfUndiscoveredTreasures
    for i in range(height):
        i = []
        for j in range(width):
            j = random.random()
            if j >= 0.7:
                j = "T"
                numberOfUndiscoveredTreasures += 1
            else:
                j = "O"
            i.append(j)
        board.append(i)
    print(board)
    return board, numberOfUndiscoveredTreasures

def main():
    global board, numberOfUndiscoveredTreasures, grid_width, grid_height
    rows = grid_width - 1
    height = grid_height - 1
    create_grid(grid_width, grid_height)
    print(f"Treasures are hidden in {numberOfUndiscoveredTreasures} locations.")
    while numberOfUndiscoveredTreasures > 0:
        checkRow = int(input(f"Enter row to check (0-{height}) "))
        checkColumn = int(input(f"Enter column to check (0-{rows}) "))
        if board[checkRow][checkColumn] == "T":
            print(f"You found a treasure at ({checkRow}, {checkColumn}!)")
            board[checkRow][checkColumn] = "X"
            numberOfUndiscoveredTreasures -= 1
        else:
            print(f"No treasure found at ({checkRow}, {checkColumn})")
    return board

def print_board():
    global board
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=" ")
        print()



main()
print_board()