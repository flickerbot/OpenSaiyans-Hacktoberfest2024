def three_sum(nums):
    # Edge case: If there are fewer than 3 numbers, we can't have a triplet
    if len(nums) < 3:
        return []
    
    # Sort the array to simplify two-pointer logic
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):  # No need to go beyond len(nums) - 2
        # Skip duplicates for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Two pointers approach
        left, right = i + 1, len(nums) - 1
        
        # If the current number is greater than 0, break early (no triplet can sum to 0)
        if nums[i] > 0:
            break
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                # Found a valid triplet
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for the second and third elements
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                # Move both pointers inward after finding a valid triplet
                left += 1
                right -= 1
            
            elif total < 0:
                # Move the left pointer to increase the sum
                left += 1
            else:
                # Move the right pointer to decrease the sum
                right -= 1
    
    return result
