class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.node_count = 0

    def insert(self, s):
        node = self.root
        for char in s:
            if char not in node.children:
                node.children[char] = TrieNode()
                self.node_count += 1  # New node = new unique substring
            node = node.children[char]

def count_unique_substrings(string):
    trie = Trie()
    for i in range(len(string)):
        # Insert each suffix into the Trie
        trie.insert(string[i:])
    return trie.node_count  # Node count equals number of distinct substrings

# Example usage:
input_str = "ababa"
print(count_unique_substrings(input_str))  # Output: 10