# Two Sum
#	Given an array of integers, return the indices of the two numbers such that they
#	add up to a specific target.

# Solution sketch:
#	Invert the array in a hash map so the value maps to the index, then verify a value
#	exists such that nums[i] + nums[j] = target

def twoSum(nums, target):
	invert = {}
	i = 0
	
	for n in nums:
		invert[n] = i
		i+=1
	
	for n in nums:
		if target-n in invert:
			return {invert[target-n], invert[n]}
			
			
# Optimized solution, one pass through the input
def twoSumOpt(nums, target):
	invert = {}
	i = 0
	
	while i < len(nums):
		if(target-nums[i] in invert):
			return {i, invert[target-nums[i]]}
		else:
			invert[nums[i]] = i
		i+=1
			
print twoSumOpt([2,7,11,15], 9)