class Board:
    
    def __init__(self):
        self.__grid = [[0,0,0] for _ in range(3)]
    
    def display(self):
        print("\n   0   1   2")
        for i, row in enumerate(self.__grid):
            row_display = []
            for j, cell in enumerate(row):
                if cell == 0:
                    row_display.append(" ")   # empty cell
                else:
                    row_display.append(str(cell))  # X or O
            print(f"{i}  " + " | ".join(row_display))
            if i < 2:
                print("  ---+---+---")
    
    def update(self,position,symbol):
        #STATUS
        #0 Occubied
        #1 Success
        #-1 Invailid position

        if (position[0] > 2 or position[0] < 0) or (position[1] > 2 or position[1] < 0):
            return -1
        
        if self.__grid[position[0]][position[1]] != 0:
            return 0
        
        self.__grid[position[0]][position[1]] = symbol
        return 1
    def check_winner(self):
        def check_rows():
            for i in range(3):
                if self.__grid[i][0] != 0 and self.__grid[i][0] == self.__grid[i][1] == self.__grid[i][2]:
                    return True
            return False

        def check_cols():
            for i in range(3):
                if self.__grid[0][i] != 0 and self.__grid[0][i] == self.__grid[1][i] == self.__grid[2][i]:
                    return True
            return False

        def check_diagonal():
            # main diagonal
            if self.__grid[0][0] != 0 and self.__grid[0][0] == self.__grid[1][1] == self.__grid[2][2]:
                return True
            # anti diagonal
            if self.__grid[0][2] != 0 and self.__grid[0][2] == self.__grid[1][1] == self.__grid[2][0]:
                return True
            return False

        return check_rows() or check_cols() or check_diagonal()
    
    def is_full(self):
        for i in range(3):
            for j in range(3):
                if self.__grid[i][j] == 0:
                    return False
        return True
    