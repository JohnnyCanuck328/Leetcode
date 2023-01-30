class Solution(object):
    def checkZeroOnes(self, s):
        oneSum = 0
        zeroSum = 0
        tempSum = 0
        for index, character in enumerate(s):
            if(int(character) != int(s[index-1])):
                if(s[index-1] == "1"):
                    oneSum = max(oneSum, tempSum)
                else:
                    zeroSum = max(zeroSum, tempSum)
                tempSum = 0
            tempSum += 1

        if(s[index] == "1"):
            oneSum = max(oneSum, tempSum)
        else:
            zeroSum = max(zeroSum, tempSum)
        return(oneSum > zeroSum)