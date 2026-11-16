/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* runningSum(int* nums, int numsSize, int* returnSize) {
    int s=0;
    int *res=malloc(numsSize*sizeof(int));
    for(int i = 0; i<numsSize;i++){
        s+=nums[i];
        res[i]=s;
    }
    *returnSize=numsSize;
    return res;
}