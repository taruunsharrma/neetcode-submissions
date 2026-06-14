class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]


        for i in range(9):
            for j in range(9):
                cell = board[i][j]

                if cell == '.':
                    continue

                # Calculate the box index
                box_index = (i // 3) * 3 + j // 3

                # Check if the number is already present in the row, column, or box
                if cell in rows[i] or cell in cols[j] or cell in boxes[box_index]:
                    return False

                # Add the number to the row, column, and box sets
                rows[i].add(cell)
                cols[j].add(cell)
                boxes[box_index].add(cell)
        
        return True