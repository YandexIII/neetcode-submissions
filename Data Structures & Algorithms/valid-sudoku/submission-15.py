class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(0,9):
            seen_row = set()
            seen_col = set()
            for j in range(0,9):
                row_val = board[i][j]
                col_val = board[j][i]
                if row_val != ".":
                    if row_val in seen_row:
                        return False
                    seen_row.add(row_val)
                
                if col_val != ".":
                    if col_val in seen_col:
                        return False
                    seen_col.add(col_val)
                    


        for row in range(0,3):      
            for square in range(0,3):
                seen_sq = set()
                for sq_row in range(0,3):
                    for digit in range(0,3):
                        val = board[row * 3 + sq_row][square * 3 + digit]
                        if val != ".":
                            if val in seen_sq:
                                return False
                            seen_sq.add(val)

        
        return True

