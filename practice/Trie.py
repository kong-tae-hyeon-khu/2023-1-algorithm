# 동적 문자열을 저장하는 트리 형태의 데이터 구조
# 문자열을 효율적으로 검색할 수 있다. -> O(L)
# 각 노드는 단일 문자를 나타내며 각 에지는 각 문자와 문자의 관계표

# Insert / Search

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.children:
                node.children[word[i]] = TrieNode()
            node = node.children[word[i]]
        node.is_end_of_word = True


    def search(self,word):
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.children:
                return False
            node = node.children[word[i]]
        return node.is_end_of_word

    def delete(self,word):
        nodes_to_del = []
        node = self.root

        for i in range(len(word)):
            if word[i] not in node.children:
                return False # 삭제할 문자열 존재 X
            nodes_to_del.append((node, word[i]))
            node = node.children[word[i]]

        if node.is_end_of_word == False: # 문자열에 존재 X
            
            return False
        
        node.is_end_of_word = False

        for parent,char in reversed(nodes_to_del):
            if node.is_end_of_word or len(node.children) > 0:
                break
            del parent.children[char]
            node = parent
     



## Test
node = Trie()
node.insert("hello")
node.insert("abc")

print(node.search("abc"))
print(node.search("hello"))

# hello 삭제.
node.delete("hello")
print(node.search("hello"))
