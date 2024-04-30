def containsDuplicate(nums):
    nums.sort()
    for num in range(len(nums) - 1):
        if nums[num] == nums[num + 1]:
            return True
    return False

arr = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate(arr))
