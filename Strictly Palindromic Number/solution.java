class Solution {
    public boolean isPalindrome(int x) {
        String tempX = Integer.toString(x);
        for(int index = 0; index < tempX.length(); ++index){
            if(tempX.charAt(index)!=tempX.charAt((tempX.length()-1)-index)){
                return false;
            }
        }
        return true;
    }
}