nums = [1,2,2,3,6,6,7]

def remove_duplicates(numbers):
	i = 0
	while i < len(numbers)-1:

		if numbers[i] == numbers[i+1]: 
			numbers.pop(i)

		else:
			i += 1
	return len(numbers)

unq_nums_len = remove_duplicates(nums)



print(unq_nums_len,nums)