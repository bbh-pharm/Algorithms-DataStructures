nums = [-1, 0, 1, 2, -1, 4]

#################
## Brute-Force ##
#################
# It's not recommended due to time complexity
def sum_of_three(nums):
  results = []
  nums.sort()

  for i in range(len(nums) - 2):
    if i > 0 and nums[i] == nums[i - 1]:
      continue
    for j in range(i + 1, len(nums) - 1):
      if j > i + 1 and nums[j] == nums[j - 1]:
        continue
      for k in range(j + 1, len(nums)):
        if k > j + 1 and nums[k] == nums[k - 1]:
          continue
        if nums[i] + nums[j] + nums[k] == 0:
          results.append((nums[i], nums[j], nums[k]))
  return results

sum_of_three(nums)

#######################
## Using two pointer ##
#######################
def sum_of_three(nums):
  result = []
  nums.sort()

  for i in range(len(nums) - 2):
    if i > 0 and nums[i] == nums[i - 1]:
      continue
  
    left, right = i + 1, len(nums) - 1
    while left < right:
      sum = nums[i] + nums[left] + nums[right]
      if sum < 0:
        left += 1
      elif sum > 0:
        right -= 1
      else:
        result.append((nums[i], nums[left], nums[right]))
        while left < right and nums[left] == nums[left + 1]:
          left += 1
        while left < right and nums[right] == nums[right - 1]:
          right -= 1
        left += 1
        right -= 1
  return result

sum_of_three(nums)
