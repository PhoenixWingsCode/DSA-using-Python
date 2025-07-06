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

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Create a Trie
trie = Trie()

# Insert words
trie.insert("apple")
trie.insert("app")
trie.insert("bat")

# Search for words
print(trie.search("apple"))  # Output: True
print(trie.search("app"))    # Output: True
print(trie.search("bat"))    # Output: True
print(trie.search("cat"))    # Output: False

# Check prefixes
print(trie.starts_with("ap"))  # Output: True
print(trie.starts_with("ba"))  # Output: True
print(trie.starts_with("ca"))  # Output: False