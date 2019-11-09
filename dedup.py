# Solution 1
nums = [1,2,2,3,6,6,7]
nums1 = [1,2,2,3]

def remove_duplicates(numbers):
	i = 0

	while i < len(numbers)-1:

		if numbers[i] == numbers[i+1]: 
			numbers.pop(i)

		else:
			i += 1
	return len(numbers)

unq_nums_len = remove_duplicates(nums1)

print(unq_nums_len,nums)

# Solution 2

def no_duplicates(nums):

	if len(nums) == 0:
		return 0

	i = 0
	for j in range(len(nums)):
		if nums[j] != nums[i]:
		# if unequal, collect unique values at the front of the list, increment both
			i += 1
			nums[i] = nums[j]
		# else i stays the same, increment j

	return i + 1

unq_nums_2 = no_duplicates(nums1)
print(unq_nums_2)
