class Solution {
    public String removeDuplicates(String s) {
        StringBuilder builder = new StringBuilder();
        for(int i=0;i<s.length();++i){
            if(builder.length() !=0 && builder.charAt(builder.length()-1)==s.charAt(i)){
                builder.deleteCharAt(builder.length()-1);
                continue;
            }
            builder.append(s.charAt(i));
        }
        return builder.toString();
    }
}