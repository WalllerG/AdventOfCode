import ast
from copy import deepcopy
with open('input.txt')as f:
    data = f.read().splitlines()
    
class Pair():
    def __init__(self, left, right, parent=None):
        self.left = left
        self.right = right
        self.parent = parent
        if isinstance(self.left, Pair): self.left.parent = self
        if isinstance(self.right, Pair): self.right.parent = self
        
    @classmethod
    def create(cls, s):
        if not isinstance(s, list):
            return s
        return cls(left=cls.create(s[0]), right=cls.create(s[1]))  
        
    def __repr__(self):
        return f"[{self.left}, {self.right}]"
    
    def explode(self, depth=0):
        if depth >= 4 and isinstance(self.left, int) and isinstance(self.right, int):
            #check left
            cur = self.parent
            child = self
            found = False
            while cur != None:
                if isinstance(cur.left, int):
                    cur.left += self.left
                    break
                elif cur.left != child:
                    target = cur.left
                    while isinstance(target, Pair):
                        if isinstance(target.right, int):
                            target.right += self.left
                            found = True
                            break
                        target = target.right
                    if found: break
                child = cur
                cur = cur.parent

            #check right
            cur = self.parent
            child = self
            found = False
            while cur != None:
                if isinstance(cur.right, int):
                    cur.right += self.right
                    break
                elif cur.right != child:
                    target = cur.right
                    while isinstance(target, Pair):
                        if isinstance(target.left, int):
                            target.left += self.right
                            found = True
                            break
                        target = target.left
                    if found: break
                child = cur
                cur = cur.parent
            
            if self == self.parent.left:
                self.parent.left = 0
            else:
                self.parent.right = 0    
                
            return True
        
        if isinstance(self.left, Pair):
            if self.left.explode(depth + 1): return True
            
        if isinstance(self.right, Pair):
            if self.right.explode(depth + 1): return True
            
        return False
    
    def split(self):
        #check left
        if isinstance(self.left, int):
            if self.left >= 10:
                num = self.left
                self.left = Pair(num // 2, num - (num // 2), self)
                return True
        elif self.left.split(): return True
        #check right
        if isinstance(self.right, int):
            if  self.right >= 10:
                num = self.right
                self.right = Pair(num // 2, num - (num // 2), self)
                return True
        elif self.right.split(): return True
        
        return False
           
    def get_sum(self):
        total = 0
        if isinstance(self.left, int) and isinstance(self.right, int):
            return 3 * self.left + 2 * self.right
        if isinstance(self.left, int) and not isinstance(self.right, int):
            return 3 * self.left + 2 * self.right.get_sum()
        if not isinstance(self.left, int) and isinstance(self.right, int):
            return 3 * self.left.get_sum() + 2 * self.right
        total += 3 * self.left.get_sum() + 2 * self.right.get_sum()

        return total
            
def add(left, right):
    return Pair(left, right)
    
def reduce(p):
    while True:
        if p.explode():
            continue
        if p.split():
            continue
        break
    return p

ans = float('-inf')
for s1 in data:
    for s2 in data:
        if s1 != s2:
            process = add(Pair.create(ast.literal_eval(s1)), Pair.create(ast.literal_eval(s2)))
            process = reduce(process)
            ans = max(ans, process.get_sum())
            
print(ans)