class Strategy:
    
    def get_move(self,board,symbol):
        for i in range(3):
            for j in range(3):
                status = board._Board__grid[i][j]
                if status == 0:
                    return i, j
                    