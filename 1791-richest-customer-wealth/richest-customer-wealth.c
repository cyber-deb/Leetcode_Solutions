int maximumWealth(int** accounts, int accountsSize, int* accountsColSize) {
    int sum=0;
    int w=0;
    for(int i=0;i<accountsSize;i++){
        for(int j=0;j<accountsColSize[i];j++){
            sum+=accounts[i][j];
        }
        if(sum>w){
            w=sum;
        }
        sum=0;
    }
    return w;
}