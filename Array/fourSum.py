### 和threeSumClosest很像，都是排序加双指针
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        # 判空
        quadruplets = list()
        if not nums or len(nums)<4:
            return quadruplets

        n = len(nums)
        nums.sort()

        """
        去重：
        1.每一种循环枚举到的下标必须大于上一重循环枚举到的下标
        2.同一重循环中，如果当前元素与上一个元素相同，则跳过当前元素
        剪枝：
        尽可能减少判断
        """

        for i in range(n-3):
            # 去重
            if i>0 and nums[i] == nums[i-1]:
                continue
            # 剪枝
            if nums[i]+nums[i+1]+nums[i+2]+nums[i+3] > target :
                break
            if nums[i]+nums[n-3]+nums[n-2]+nums[n-1] < target:
                continue

            for j in range(i+1,n-2):
                # 去重
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                # 剪枝
                if nums[i]+nums[j]+nums[j+1]+nums[j+2] > target :
                    break
                if nums[i]+nums[j]+nums[n-2]+nums[n-1] < target:
                    continue
                
                l,r = j+1,n-1
                while l<r:
                    sum = nums[i]+nums[j]+nums[l]+nums[r]
                    if sum == target:
                        quadruplets.append([nums[i],nums[j],nums[l],nums[r]])
                        # ！去重
                        while l<r and nums[l] == nums[l+1]:
                            l += 1
                        l += 1
                        while l<r and nums[r] == nums[r-1]:
                            r -= 1
                        r -= 1
                    elif sum > target:
                        r -= 1
                    else:
                        l += 1

        print(quadruplets)
        return quadruplets

case1 =  [1,0,-1,0,-2,2]
case2 = [2,2,2,2,2]
if __name__=="__main__":
	obj = Solution()
	obj.fourSum(case1,0)
	obj.fourSum(case2,8)

