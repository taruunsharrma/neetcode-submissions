class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # We will be looping for rows, cols and boxes
        # [
        # ["1","2",".",".","3",".",".",".","."], (0,0) (0,1)
        # ["4",".",".","5",".",".",".",".","."],
        # [".","9","8",".",".",".",".",".","3"],
        # ["5",".",".",".","6",".",".",".","4"],
        # [".",".",".","8",".","3",".",".","5"],
        # ["7",".",".",".","2",".",".",".","6"],
        # [".",".",".",".",".",".","2",".","."],
        # [".",".",".","4","1","9",".",".","8"],
        # [".",".",".",".","8",".",".","7","9"]]

        cols = defaultdict(set)
        rows = defaultdict(set)
        boxes = defaultdict(set) #key = r//3, c//3

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (
                    board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in boxes[(r//3, c//3)]
                ):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                boxes[(r//3, c//3)].add(board[r][c])

        return True





