class Solution(object):
    def mostWordsFound(self, sentences):
        maxNumWords = 0
        for elem in sentences:
            temp = elem.split()
            if(len(temp) > maxNumWords):
                maxNumWords = len(temp)
        return maxNumWords
