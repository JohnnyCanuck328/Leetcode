class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        N=len(nums)
        numsPair = []
        numsSmaller = [0]*N
        for index in range(len(nums)):
            #array contains [element, index]
            numsPair.append([nums[index], index])
        numsPair.sort()
        prevNum = numsPair[0][0]
        numSmaller = 0
        for index in range(1,len(numsPair)):
            elemIndex = numsPair[index][1]
            elemNum = numsPair[index][0]
            if(prevNum != elemNum):
                numsSmaller[elemIndex] = index
                numSmaller = index
            else:
                numsSmaller[elemIndex] = numSmaller
            prevNum = elemNum
        return numsSmaller