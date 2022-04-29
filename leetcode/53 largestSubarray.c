// my buggy code which dindt run



// int maxSubArray(int* nums, int numsSize){
    
//     // first lets make all the subarrays
//     int max_subarray[100000];
//     int mini_array[100000];
    
//     *max_subarray = {} ;
//     printf(max_subarray[0]);
    
//     for(int j=0; j< numsSize; ++j){
//         for (int i=1; i < numsSize-j;++i){
//             mini_array = {};
//             for(int k=j; k< j+i; ++k){
//                 mini_array[k-j] = k;
//             }
            
//             for (int l=0; l<i; ++l){
//                 printf(mini_array[l]);
//             }
//         }
//     }
// }


// int main(){
//     return 0;
// }

//something simple as

/*
Runtime: 132 ms, faster than 54.92% of C online submissions for Maximum Subarray.
Memory Usage: 12.4 MB, less than 32.57% of C online submissions for Maximum Subarray.
*/

// but why sum>0 works is a mystery.

int maxSubArray(int* nums, int size)
{
    int sum = 0;
    int max = INT_MIN;
    for(int i = 0; i < size; i++)
    {
        if(sum >= 0)
            sum += nums[i];
        else
            sum = nums[i];
        if(sum > max)
            max = sum;
    }
    return max;
}