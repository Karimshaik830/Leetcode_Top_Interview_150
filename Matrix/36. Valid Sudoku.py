class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[] for _ in range(9)]
        column = [[] for _ in range(9)]
        block = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    idx = (i // 3) * 3 + j // 3
                    if board[i][j] in block[idx]:
                        return False
                    else:
                        block[idx].append(board[i][j])
                    if board[i][j] in row[i]:
                        return False
                    else:
                        row[i].append(board[i][j])
                    if board[i][j] in column[j]:
                        return False
                    else:
                        column[j].append(board[i][j])

        # # check board valid
        # for i in range(9):
        #     if len(row[i]) != len(set(row[i])):
        #         # print("row")
        #         # print(board[i])
        #         return False
        #     if len(column[i]) != len(set(column[i])):
        #         # print("row")
        #         # print(board[i])
        #         return False
        #     if len(block[i]) != len(set(block[i])):
        #         # print("block")
        #         # print(block[i])
        #         return False

        return True