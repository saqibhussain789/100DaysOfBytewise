def max_subarray(nums):
    if not nums:
        return 0
    max_current = max_global = nums[0]
    for num in nums[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
    return max_global

# Function to take input from user
def input_array(prompt):
    return list(map(int, input(prompt).split()))

# Take input from user and test the function
nums = input_array("Enter the elements of the array separated by spaces: ")
print("Maximum subarray sum:", max_subarray(nums))
