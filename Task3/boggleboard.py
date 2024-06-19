class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

def find_words(board, words):
    def dfs(board, node, i, j, path, result):
        if node.is_end_of_word:
            result.add(path)
            node.is_end_of_word = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        char = board[i][j]
        if char not in node.children:
            return
        board[i][j] = '#'  # Mark the cell as visited
        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            dfs(board, node.children[char], i + x, j + y, path + char, result)
        board[i][j] = char  # Unmark the cell

    trie = Trie()
    for word in words:
        trie.insert(word)
    result = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(board, trie.root, i, j, "", result)
    return list(result)

# Function to take input from user
def input_board():
    rows = int(input("Enter the number of rows in the board: "))
    board = []
    print("Enter the board row by row, with characters separated by spaces:")
    for _ in range(rows):
        row = input().split()
        board.append(row)
    return board

def input_words():
    words = input("Enter the words to search in the board, separated by spaces: ").split()
    return words

# Take input from user and test the function
board = input_board()
words = input_words()
print("Words found in the board:", find_words(board, words))
