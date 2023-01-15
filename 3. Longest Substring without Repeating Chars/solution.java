class Solution {
    public int lengthOfLongestSubstring(String s) {
        int lswrc = 0;
        for(int index = 0; index < s.length(); ++index){
            Set<Character>currentSubstring = new HashSet<>();
            char currentChar = s.charAt(index);
            int currentIndex = index;
            while(!(currentSubstring.contains(currentChar))){
                currentSubstring.add(currentChar);
                ++currentIndex;
                if(currentIndex>s.length()-1){
                    break;
                }
                currentChar = s.charAt(currentIndex);
            }
            lswrc = Math.max(lswrc, currentSubstring.size());
        }
        return (lswrc);
    }
}