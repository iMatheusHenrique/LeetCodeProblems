class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        size_of_nums = len(nums)

        for iterator in range(0,size_of_nums,1):
            for iterator2 in range(iterator+1,size_of_nums,1):
                sum_of_positions = nums[iterator] + nums[iterator2]
                if sum_of_positions == target:
                    return [iterator, iterator2]


# nums = [3,2,4]
# target = 6

# nums = [2,7,11,15]
# target = 9

nums = [3,3]
target = 6

# nums = [2,5,5,11]
# target = 10

object_solution = Solution()
result = object_solution.twoSum(nums, target)
print(result)
print(type(result))
