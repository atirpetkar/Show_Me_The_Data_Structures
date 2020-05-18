I have implemented huffman encoding technique here with following steps:

<br>i) Calculate the occurences of each characters in a string. 
<br>ii) Character with highest occurence is encoded with minimum code length ie 1 then next Character as 01 and 
then 001 and the process continues.

Time complexity: O(n) Space complexity: O(distinct_characters)
