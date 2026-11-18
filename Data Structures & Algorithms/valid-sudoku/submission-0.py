class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)



        for i in range(9):

            for j in range(9):

                curr = board[i][j]

                if curr in rows[j] or curr in cols[i] or curr in squares[(i//3, j//3)]:
                    return False

                if board[i][j] != ".":
                    rows[j].add(curr)

                    cols[i].add(curr)

                    squares[(i//3, j//3)].add(curr)

        return True







            
        