class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a= []
        b= []
        for i in s:
            a.append(i)
        for j in t:
            b.append(j) 
        new_a = sorted(a)
        new_b = sorted(b)
        if new_a == new_b:
        
            return True
        return False