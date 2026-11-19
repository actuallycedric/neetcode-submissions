class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        seen_rows = defaultdict(set)
        seen_cols = defaultdict(set)
        seen_sq = defaultdict(set)

        for row in range(9):

            for col in range(9):

                curr = board[row][col]

                if curr in seen_rows[row] or curr in seen_cols[col] or curr in seen_sq[(row//3, col//3)]:
                    return False

                if curr != '.':
                    seen_rows[row].add(curr)
                    seen_cols[col].add(curr)
                    seen_sq[(row//3, col//3)].add(curr)

        
        return True
                    
        