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

    def has_all_prefixes(self, word):
        node = self.root
        for char in word:
            if char not in node.children or not node.children[char].is_end_of_word:
                return False
            node = node.children[char]
        return True

def longest_word_with_prefixes(words):
    trie = Trie()
    for word in words:
        trie.insert(word)

    longest_word = ""
    for word in words:
        if trie.has_all_prefixes(word):
            # Update longest word based on length and lexicographical order
            if len(word) > len(longest_word) or (len(word) == len(longest_word) and word < longest_word):
                longest_word = word

    return longest_word

# Example usage
words = ["a", "ap", "app", "appl", "apple", "apply"]
result = longest_word_with_prefixes(words)
print("Longest word with all prefixes:", result)
