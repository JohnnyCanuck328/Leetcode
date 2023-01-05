class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        //elem, index
        int[][] newNums = new int[nums.length][];
        int[] returnArr = new int[nums.length];
        for(int index = 0; index < nums.length; ++index){
            newNums[index] = new int[]{nums[index], index};
        }
        Arrays.sort(newNums, (a, b) -> a[0] - b[0]);
        System.out.println(Arrays.deepToString(newNums) + "\n");
        int prevNum = newNums[0][0];
        int numSmaller = 0;
        for(int index = 1; index < newNums.length; ++index){
            if(prevNum != newNums[index][0]){
                returnArr[newNums[index][1]] = index;
                prevNum = newNums[index][0];
                numSmaller = index;
            }
            else{
                returnArr[newNums[index][1]] = numSmaller;
            }
        }
        return returnArr;
    }
}