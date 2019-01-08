#Most Water
# Given n non-negative integers (a1, a2, ... , an), n vertinal lines are drawn
# in the plane such that the two endpoints are (i, ai) and (i, 0). Find the container
# with boundaries given by any pair of lines and the x-axis such that the container
# has the larget volume.

#Solution sketch:
#	The goal is to find the pair of integers that maximize the distance between their
#	indices and the magnitude of the smallest in the pair. I want the most separated
#	pair with the largest smaller element. The pair must satisfy the constraint that
#	no element with a smaller index than the smallest index of elements in the pair
#	is at least as large as the smallest value in the pair. The pair must satisfy the
#	constraint that no element with a larger index than the largest index of elements
#	in the pair is at least as large as the smallest value in the pair. In either case
#	if the closest index to the candidate element is the smallest value in the pair, the
#	candidate element can replace the closest index. If the furthest index to the candidate
#	element is the smallest value in the pair, the candidate element can replace the closest
#	index. An arbitrarily bad solution (depending on the instance) can be found in O(n) by a
#	random start and "gradient ascent" with a constant number of restarts. We can reverse
#	the above thinking so that we move from the ends inward rather than a valid solution
#	outwards.

def maxArea(heights):
	left = 0
	right = len(heights)-1
	
	maxArea = 0
	
	while left < right:
		maxArea = max(maxArea, min(heights[left], heights[right]) * (right-left))
		if(heights[left] < heights[right]):
			left += 1
		else:
			right -= 1
			
	return maxArea
	
print maxArea([0, 21, 3, 5, 8, 19, 15, 1, 0, 0, 6])