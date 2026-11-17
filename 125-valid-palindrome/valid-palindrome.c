#include<ctype.h>
#include<string.h>
bool isPalindrome(char* s) {
    int  left = 0;
    int right = strlen(s)-1;
    while(left<=right){
        if isalnum(s[left]){
            if isalnum(s[right]){
                if (tolower(s[left])==tolower(s[right])){
                    left++;
                    right--;
                }
                else{
                    return false;
                }
            }
            else{
                right--;
            } 
        }
        else{
            left++;
        }
    }
    return true;
}