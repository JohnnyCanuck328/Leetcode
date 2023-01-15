class Solution(object):
    def lengthOfLongestSubstring(self, s):
        lswrc = 0
        for index,element in enumerate(s):
            currentSubstring = {}
            currentChar = element
            currentIndex = index
            while(not(currentChar in currentSubstring)):
                currentSubstring[currentChar] = None
                currentIndex+=1
                if(currentIndex==len(s)):
                    break
                currentChar = s[currentIndex]
            lswrc = max(lswrc, len(currentSubstring))
        return lswrc