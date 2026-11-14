#include<stdlib.h>
#include<string.h>
int compare(const void *a, const void *b){
    int x = *(int*)a;
    int y = *(int*)b;
    return ((x>y)-(x<y));
}
int heightChecker(int* heights, int heightsSize) {
    int current[heightsSize];
    memcpy(current,heights,heightsSize*sizeof(int));
    qsort(heights,heightsSize,sizeof(int),compare);
    int c =0;
    for(int i=0;i<heightsSize;i++){
        if(current[i]!=heights[i]){
            c++;
        }
    }
    return c;
}