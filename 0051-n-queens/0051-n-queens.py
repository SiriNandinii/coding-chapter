class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(row, col):
            for r in range(row):
                # Check same column or diagonal conflicts
                if board[r] == col or abs(board[r] - col) == abs(r - row):
                    return False
            return True

        def backtrack(row=0):
            if row == n:
                # Convert numeric board to string board
                solution = []
                for i in range(n):
                    row_str = '.' * board[i] + 'Q' + '.' * (n - board[i] - 1)
                    solution.append(row_str)
                result.append(solution)
                return
            
            for col in range(n):
                if is_safe(row, col):
                    board[row] = col
                    backtrack(row + 1)
                    board[row] = -1  # Backtrack

        result = []
        board = [-1] * n
        backtrack()
        return result
