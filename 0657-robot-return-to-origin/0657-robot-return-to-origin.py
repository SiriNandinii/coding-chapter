class Solution:
    def judgeCircle(self, moves: str) -> bool:
        moves = [char for char in moves]
        U = moves.count('U')
        D = moves.count('D')
        L = moves.count('L')
        R = moves.count('R')

        if U==D and L==R:
            return True
        return False