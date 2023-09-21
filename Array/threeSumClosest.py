"""
排序复杂度 O(nlogn)
整个遍历过程，固定值为 n 次，双指针为 n 次，时间复杂度为 O(n^2)
"""

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 升序排序
        nums.sort()
        # 双指针
        # 第一次提交报错的原因：指针在移动的时候，要比较前后和target的距离
        res = 10**7 # 10的7次方
         
        def update(cur):
            # 用于嵌套函数中，不能用于全局作用域
            nonlocal res
            if abs(cur-target) < abs(res-target) :
                res = cur

        for index,num in enumerate(nums):
            if index>0 and nums[index]==nums[index-1]:
                continue
            l,r = index+1,len(nums)-1
            while l < r :
                sum = num + nums[l] + nums[r]
                if sum == target :
                    return target
                update(sum)
                if sum < target :
                    l0 = l+1
                    # 优化： 移动到下一次不相等的指针
                    while l0<r and nums[l0]==nums[l] :
                        l0 += 1
                    l = l0
                else :
                    r0 = r-1
                    while l<r0 and nums[r0]==nums[r] :
                        r0 -= 1
                    r = r0
        print(res)
        return res
    


case1 = [-1,2,1,-4]
case2 = [1,1,1,0]

if __name__ == "__main__":
	obj = Solution()
	obj.threeSumClosest(case1,1)
	obj.threeSumClosest(case2,1)