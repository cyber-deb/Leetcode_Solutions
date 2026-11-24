/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countBits(int n, int* returnSize) {
    int num = 0;
    int *res=calloc((n+1),sizeof(int));
    for(int i = 0; i<=n ; i++){
        num=i;
        while(num){
            num&=(num-1);
            res[i]++;
        }
    }
    *returnSize = n+1;
    return res;
}