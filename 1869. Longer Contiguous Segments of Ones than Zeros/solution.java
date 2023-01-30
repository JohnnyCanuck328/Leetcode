class Solution {
    public boolean checkZeroOnes(String s) {
        int oneSum = 0;
        int zeroSum = 0;
        int tempSumOne = 0;
        int tempSumZero = 0;
        for(char character : s.toCharArray()){
            if(character=='1'){
                oneSum = Math.max(oneSum, ++tempSumOne);
                tempSumZero = 0;
            }
            else{
                zeroSum = Math.max(zeroSum, ++tempSumZero);
                tempSumOne = 0;
            }
        }
        return(oneSum > zeroSum);
    }
}