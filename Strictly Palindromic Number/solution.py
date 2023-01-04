class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        x = list(x)
        for index in range(len(x)):
            elem = x[index]
            mirror = x[(len(x)-1)-index]
            if(elem != mirror):
                return False

        return True