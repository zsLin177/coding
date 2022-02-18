'''
构建前缀树
key:
首先要理解前缀树的定义，然后就好做了
'''
class TrieNode:
    def __init__(self, if_end=False):
        self.if_end = if_end
        self.next_lst = [None] * 26

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if node.next_lst[ord(c)-97] is None:
                node.next_lst[ord(c)-97] = TrieNode()
            node = node.next_lst[ord(c)-97]
        node.if_end = True


    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if node.next_lst[ord(c)-97] is None:
                return False
            node = node.next_lst[ord(c)-97]
        return node.if_end


    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if node.next_lst[ord(c)-97] is None:
                return False
            node = node.next_lst[ord(c)-97]
        return True

