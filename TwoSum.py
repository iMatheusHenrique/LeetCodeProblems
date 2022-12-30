
import time

start = time.perf_counter()
nums = [2,5,5,11]
target = 10

# My Solution
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         size_of_nums = len(nums)

#         for iterator in range(0,size_of_nums,1):
#             for iterator2 in range(iterator+1,size_of_nums,1):
#                 sum_of_positions = nums[iterator] + nums[iterator2]
#                 if sum_of_positions == target:
#                     return [iterator, iterator2]
# 1.590000101714395e-05

# leet code solution
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
# 1.4600000213249587e-05

object_solution = Solution()
result = object_solution.twoSum(nums, target)

end = time.perf_counter()
runtime = end-start
print(f"Runtime {runtime}")
