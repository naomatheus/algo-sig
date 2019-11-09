## mock interview 

# 
## 
list_1 = [1,3,4,5,6]
list_2 = [2,3,4,7,8,9,9]

def merge_lists(nums1, nums2):

	for j in range(len(nums2)):
		nums1.append(nums2[j])
	# combine the two lists, merge

	return sorted(nums1)

print(merge_lists(list_1,list_2))

# 0(m*log(n)) complexity where m is the number of items in the first list, and n is the number of items in the second merged list 

## More efficient pseudo code 

# while i < list1.len && j < list2.len
# if (list1[i] <= list2[j])
# sortedList.append(list1[i])
#   i++
# else
# sortedList.append(list2[j])
# j++

# while j < list2.len
# sortedList.append(list2[j])

# while i < list1.len
# sortedList.append(list1[i])