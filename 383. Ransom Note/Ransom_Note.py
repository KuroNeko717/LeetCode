class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict1 = {}
        dict2 = {}
        Flag=True
        for keys in ransomNote:
            dict1[keys] = dict1.get(keys, 0) + 1
        
        for keys in magazine:
            dict2[keys] = dict2.get(keys,0) + 1
            
        list_of_keys = list(dict1.keys())
        for key in list_of_keys:
            if key in dict2.keys():
                if dict2[key] >= dict1[key]:
                    continue
                else:
                    Flag = False
            else:
                Flag = False
                break
        return Flag


# A much better optimum solution would be
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in set(ransomNote):
            if magazine.count(i) < ransomNote.count(i):
                return False
        return True