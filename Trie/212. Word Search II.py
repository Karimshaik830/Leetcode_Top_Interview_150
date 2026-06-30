class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Insert every word into trie
        # start dfs from every cell
        # In DFS, walk through trie
        # if tree node contains complete word we found candidate
        # continue search
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        rows = len(board)
        cols = len(board[0])

        result = []

        def dfs(r, c, parent):
            letter = board[r][c]
            if letter not in parent.children:
                return

            node = parent.children[letter]
            # check if current pos make up the word
            if node.word:
                result.append(node.word)
                # To avoid duplicates
                node.word = None
            board[r][c] = '#'  # so that we do not count it again
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < rows and
                        0 <= nc < cols and
                        board[nr][nc] != '#'):
                    dfs(nr, nc, node)

            # reset back
            board[r][c] = letter
            if not node.children and node.word is None:
                del parent.children[letter]

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root)

        return result