"""AoC 2024 Day 18 Task 1"""

from collections import deque

# pylint: disable=E0606,E0601,C0103

# File Handeling
def read_file(file_name: str) -> list[str]:
    with open(file_name, "r", encoding="utf-8") as file_in:
        return [line.strip() for line in file_in]

def clean_data(filename):
    raw_input = read_file(filename)
    towels = raw_input[0].split(', ')

    patterns = []
    for index in range(2, len(raw_input)):
        patterns.append(raw_input[index])

    return towels, patterns

# Trie based prefix tree
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

def build_prefix_tree(towels):
    trie = Trie()
    for towel in towels:
        trie.insert(towel)
    return trie


if __name__ == "__main__":

    towels, patterns = clean_data('data/test/19.txt')
    trie = build_prefix_tree(towels)

    # Example of trying to match 'brwrr'
    print(trie.starts_with("b")) 
    print(trie.starts_with("br"))
    print(trie.starts_with("brw"))
    print(trie.starts_with("w"))
    print(trie.starts_with("wr"))
    print(trie.starts_with("wrr"))
    print(trie.starts_with("r"))