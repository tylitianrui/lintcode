package   main

import "fmt"


/**
 * @param nums: A list of integers
 * @return: A integer indicate the sum of max subarray
 */
func maxSubArray (nums []int) int {
	// write your code here
	res,max := nums[0],nums[0]
	for i:=1;i<len(nums);i++{
		if  res>0{
			res += nums[i]
		}else {
			res = nums[i]
		}
		if  res >max{
			max = res
		}

	}
	return max
}



func main()  {
	l:=[]int{0,-1,4,6,-1,-2,4,-8}
	fmt.Println(maxSubArray(l))

}