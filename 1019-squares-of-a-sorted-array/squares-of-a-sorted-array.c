
#include<stdlib.h>
int compare(const void *a, const void *b){
    int x = *(int*)a;
    int y = *(int*)b;
    return ((x>y)-(x<y));
}
int* sortedSquares(int* nums, int numsSize, int* returnSize) {
    int *result = malloc(numsSize*sizeof(int));
    for(int i=0;i<numsSize;i++){
        result[i]=nums[i]*nums[i];
    }
    qsort(result,numsSize,sizeof(int), compare);
    *returnSize=numsSize;
    return result;
}