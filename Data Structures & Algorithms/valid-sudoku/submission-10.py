class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(0,9):
            row_seen = set()
            for digit in range(0,9):
                val = board[row][digit]
                if val != ".":
                    if val in row_seen:
                        print("row")
                        return False
                    row_seen.add(val)
                
        
        for column in range(0,9):
            seen_col = set()
            for digit in range(0,9):
                val = board[digit][column]
                if val != ".":
                    if val in seen_col:
                        print("col")
                        return False
                    seen_col.add(val)


        for row in range(0,3):      
            for square in range(0,3):
                seen_sq = set()
                for sq_row in range(0,3):
                    for digit in range(0,3):
                        val = board[row * 3 + sq_row][square * 3 + digit]
                        if val != ".":
                            if val in seen_sq:
                                print(f"sq {row} {square} {sq_row} {digit}")
                                return False
                            seen_sq.add(val)

        
        return True



            
        

        


        