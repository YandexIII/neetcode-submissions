class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(0,9):
            digits_row = []
            for digit in range(0,9):
                if board[row][digit] in digits_row and board[row][digit].isdigit():
                    print("row")
                    return False
                digits_row.append(board[row][digit])
                
        
        for column in range(0,9):
            digits_col = []
            for digit in range(0,9):
                if board[digit][column] in digits_col and board[digit][column].isdigit():
                    print("col")
                    return False
                digits_col.append(board[digit][column])


        for row in range(0,3):      
            for square in range(0,3):
                digits_sq = []
                for sq_row in range(0,3):
                    for digit in range(0,3):
                        if board[row * 3 + sq_row][square * 3 + digit] in digits_sq and board[row * 3 + sq_row][square * 3 + digit].isdigit():
                            print(f"sq {row} {square} {sq_row} {digit}")
                            return False
                        digits_sq.append(board[row * 3 + sq_row][square * 3 + digit])

        
        return True



            
        

        


        