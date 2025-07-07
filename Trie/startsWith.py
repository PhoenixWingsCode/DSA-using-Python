class TrieNode:
    def __init__(self):
        self.children = {}  # keys are characters, values are TrieNode
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
trie = Trie()

# Insert words
trie.insert("apple")
trie.insert("app")
trie.insert("bat")

# Search for words
print(trie.search("app"))    # True
print(trie.search("apple"))  # True
print(trie.search("bat"))    # True
print(trie.search("bath"))   # False

# Check prefix
print(trie.startsWith("ap"))  # True
print(trie.startsWith("ba"))  # True
print(trie.startsWith("ca"))  # False