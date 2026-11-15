void moveZeroes(int* nums, int numsSize) {
    int j = 0;
    int temp = 0;
    for (int i = 0; i<numsSize;i++){
        if (nums[i]!=0){
            temp=nums[i];
            nums[i]=nums[j];
            nums[j]=temp;
            j++;
        }
    }
}