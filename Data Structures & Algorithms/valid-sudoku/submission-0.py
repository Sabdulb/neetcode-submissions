class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        cubs = defaultdict(set)
        nums = {"1","2","3","4","5","6","7","8","9"}

        for i in range(len(board)):
            for j in range(len(board[i])):

                if board[i][j] in nums:
                    if board[i][j] in rows[i]:
                        return False
                    else:
                        rows[i].add(board[i][j])
                    print(rows)
                    
                    if board[i][j] in cols[j]:
                        return False
                    else:
                        cols[j].add(board[i][j])
                    print(cols)

                    if board[i][j] in cubs[(i // 3, j // 3)]:
                        return False
                    else:
                        cubs[(i // 3, j // 3)].add(board[i][j])
                    print(cubs)

        return True