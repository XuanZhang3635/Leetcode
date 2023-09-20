"""
盛水最多的容器 ： 双指针
1.首先这个问题的答案可以用数学的方式表示：res = min(height[i],height[j])*(j-i), 求最大值
2.当移动较短的板时，res的值可能会增大；移动较长的板时，res的值肯定不会增加。所以每一次移动较短的那块板。

正确性证明：

复杂度分析：
时间复杂度 O(N)​ ： 双指针遍历一次底边宽度 N​ 。
空间复杂度 O(1)​ ： 变量 left, right , resresres 使用常数额外空间。
"""
from typing import List

case1 = [1,8,6,2,5,4,8,3,7]
case2 = [1,1]
# 当你定义一个类，并在类中定义方法时，通常需要将 self 作为第一个参数传递给方法。
# 这样，在类的实例被创建后，方法可以通过 self 来访问实例的属性和其他方法。
class Solution:
	def maxArea(self, height: List[int]) -> int:
		left,right,res = 0,len(height)-1,0
		while left < right:
			if  height[left] < height[right]:
				res = max(res,height[left]*(right-left))
				left += 1
			else:
				res = max(res,height[right]*(right-left))
				right -= 1
		print(res)
		return res

if __name__ == "__main__":
	obj = Solution()
	obj.maxArea(case1)
	obj.maxArea(case2)
