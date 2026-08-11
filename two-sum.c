#include<stdlib.h>
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int i = 0;
    int j;
    int h=0;
    int *res= (int *)malloc(sizeof(int) *2);
    *returnSize =2;
    while( i <numsSize)
    {
        j=i+1;
        while(j < numsSize)
        {
            if((nums[i]+nums[j]) == target)
            {
              
                res[0]= i;
                res[1] = j;
                return res;
            }
            j++;
        }
        i++;
    }
    return 0;
}