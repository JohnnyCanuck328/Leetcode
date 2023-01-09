class Solution {
    public int mostWordsFound(String[] sentences) {
        int mostWords = 0;
        int temp = 0;
        for(String elem : sentences){
            temp = elem.split(" ").length;
            if(temp > mostWords){
                mostWords = temp;
            }
        }
        return mostWords;
    }
}