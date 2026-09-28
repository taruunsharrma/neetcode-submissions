class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        cols = defaultdict(set)
        row = defaultdict(set)
        square = defaultdict(set)

        for r in range(9):
            for c in range(9):
                # now we have access to each cell
                # we can now keep track
                if board[r][c] == '.':
                    continue
                
                if (
                    board[r][c] in row[r]
                    or
                    board[r][c] in cols[c]
                    or 
                    board[r][c] in square[(r//3, c//3)]
                    ):
                    return False

                cols[c].add(board[r][c])
                row[r].add(board[r][c])
                square[(r//3, c//3)].add(board[r][c])
        
        return True
