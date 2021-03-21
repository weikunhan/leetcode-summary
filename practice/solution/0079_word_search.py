class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        self.res = False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(i, j, board, word)

        return self.res
 
    def dfs(self, row, col, board, word):
        if not word: 
            self.res = True
            
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or self.res or board[row][col] != word[0]:
            
            return 
        
        temp_value = board[row][col]
        board[row][col] = '#'
        self.dfs(row + 1, col, board, word[1:])
        self.dfs(row, col + 1, board, word[1:])
        self.dfs(row - 1, col, board, word[1:])
        self.dfs(row, col - 1, board, word[1:])
        board[row][col] = temp_value