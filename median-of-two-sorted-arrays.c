
int ft_strlen(int* str) {
    int i = 0;
    while (str[i])
        i++;
    return i;
}
double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2,
                              int nums2Size) {
   int n =nums2Size + nums1Size;
    int *num = (int *)malloc(n * sizeof(int));

    int i = 0;
    int j = 0;
    int h=0;
    double k;
    while (i < nums1Size)
    {
       num[h++]= nums1[i++];
    }
    while (j < nums2Size) {
        num[h] = nums2[j];
        h++;
        j++;
    }
    i=0;
    int tmp;
    while(i < n)
    {
        j=0;
        while(j < n)
        {
            if(num[i] > num[j])
                {
                    tmp = num[i];
                    num[i]=num[j];
                    num[j]=tmp;
                }
                j++;
        }
        i++;
    }
    if (n % 2 != 0)
       return (k =num[n/2]);
    k = ((double)num[n/2 - 1] + (double)num[n/2 ]) / 2.0;
    return k;

}