class Node:
    
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        
        curr.end = True
        return 

    def search(self, word: str) -> bool:
        
        def step(curr, idx):
            # base case 
            if idx >= len(word):
                return curr.end

            # if dot explore all branches
            if word[idx] == '.':
                for c in curr.children:
                    if step(curr.children[c], idx+1):
                        return True
                return False
            
            if word[idx] not in curr.children:
                return False
            return step(curr.children[word[idx]], idx+1)
        
        return step(self.root, 0)