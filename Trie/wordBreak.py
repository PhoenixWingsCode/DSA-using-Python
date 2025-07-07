# Python implementation of Trie and Word Break
class TNode:
    def __init__(self):
        self.child = [None] * 26
        self.isEndOfWord = False

# If not present, inserts key into trie
# If the key is prefix of trie node, just marks leaf node
def insert(root, key):
    pCrawl = root

    for char in key:
        index = ord(char) - ord('a')
        if not pCrawl.child[index]:
            pCrawl.child[index] = TNode()
        pCrawl = pCrawl.child[index]

    # mark last node as leaf
    pCrawl.isEndOfWord = True

# Returns true if string can be segmented into space separated words, otherwise returns false
def wordBreak(s, root):
    n = len(s)
    if n == 0:
        return True

    dp = [False] * (n + 1)
    dp[0] = True  # dp[i] is true if s[0..i-1] can be segmented

    for i in range(1, n + 1):
        curr = root
        for j in range(i - 1, -1, -1):
            index = ord(s[j]) - ord('a')
            if not curr.child[index]:
                break
            curr = curr.child[index]
            # If s[j..i-1] is a word and dp[j] is true
            if curr.isEndOfWord and dp[j]:
                dp[i] = True
                break

    return dp[n]

# Driver program to test above functions
if __name__ == '__main__':
    dictionary = [
        "mobile", "samsung", "sam", "sung", "ma",
        "mango", "icecream", "and", "go", "i",
        "like", "ice", "cream"
    ]

    root = TNode()

    # Construct trie
    for word in dictionary:
        insert(root, word)

    print("Yes" if wordBreak("ilikesamsung", root) else "No")
    print("Yes" if wordBreak("iiiiiiii", root) else "No")
    print("Yes" if wordBreak("", root) else "No")
    print("Yes" if wordBreak("ilikelikeimangoiii", root) else "No")
    print("Yes" if wordBreak("samsungandmango", root) else "No")
    print("Yes" if wordBreak("samsungandmangok", root) else "No")