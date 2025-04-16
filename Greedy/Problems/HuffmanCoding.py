import heapq
from collections import defaultdict, Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def calculate_frequency(data):
    return Counter(data)

def build_huffman_tree(freq):
    heap = [Node(char, frequency) for char, frequency in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def generate_codes(node, current_code='', codes={}):
    if node is None:
        return
    if node.char is not None:
        codes[node.char] = current_code
    generate_codes(node.left, current_code + '0', codes)
    generate_codes(node.right, current_code + '1', codes)

def huffman_encoding(data):
    freq = calculate_frequency(data)
    root = build_huffman_tree(freq)
    codes = {}
    generate_codes(root, '', codes)
    return ''.join(codes[char] for char in data), root

def huffman_decoding(encoded_data, root):
    decoded_data = ''
    current_node = root
    for bit in encoded_data:
        current_node = current_node.left if bit == '0' else current_node.right
        if current_node.char is not None:
            decoded_data += current_node.char
            current_node = root  # Reset to root for next character
    return decoded_data

# Example Usage
if __name__ == "__main__":
    input_data = "hello world"
    encoded_data, tree_root = huffman_encoding(input_data)
    print(f"Encoded Data: {encoded_data}")

    decoded_data = huffman_decoding(encoded_data, tree_root)
    print(f"Decoded Data: {decoded_data}")