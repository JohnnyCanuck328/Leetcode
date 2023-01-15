class Solution(object):
    def reverse(self, x):
        isNeg = False
        if(x<0):
            x = -x
            isNeg = True
        x=list(str(x))
        returnValue = [0]*len(x)
        print(x)
        for index in range(len(x)):
            reverseIndex = (len(x)-1)-index
            returnValue[reverseIndex]=x[index]
        print(returnValue)
        returnValue = ''.join(returnValue)
        returnValue = int(returnValue)
        if(isNeg):
            returnValue = -returnValue
        if(returnValue > (2**31-1) or returnValue < -(2**31)):
            return 0
        return returnValue