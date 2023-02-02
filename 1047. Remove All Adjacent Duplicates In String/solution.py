class Solution(object):
    def removeDuplicates(self, s):
        index = 0
        for element in s:
                    if(index == 0):
                        index+=1
                        continue
                    elif(s[index-1] == element):
                        s = s[:index-1] + s[index+1:]
                        index-=1
                    else:
                        index+=1
        return s