#include<string.h>
#include<stdbool.h>
bool isAnagram(char* s, char* t) {
    int freq[26]={0};
    if(strlen(s)!=strlen(t)){
        return false;
    }
    for (int i = 0 ; i<strlen(s) ; i++){
        freq[s[i]-'a']++;
        freq[t[i]-'a']--;
    }
    for(int j = 0; j<26; j++){
        if (freq[j]!=0){
            return false;
        }
    }
    return true;
}