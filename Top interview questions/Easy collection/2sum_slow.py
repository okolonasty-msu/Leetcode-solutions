#O(n^2)
# too slow solution
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                if nums[i] + nums[j] == target:
                    return list((i, j))
                    break
