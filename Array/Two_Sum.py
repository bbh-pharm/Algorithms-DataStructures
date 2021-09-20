nums = [2, 7, 11, 15]
target = 9

#################
## Brute-Force ##
#################
def brute_force(nums, target):
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      if nums[i] + nums[j] == target:
        return [i, j]

brute_force(nums, target)

################
## Using "in" ##
################
def use_in(nums, target):
  for i, n in enumerate(nums):
    complement = target - n

    if complement in nums[i+1:]:
      return i, nums.index(complement)

use_in(nums, target)

##############################
## Using dictionary and key ##
##############################
def use_dict(nums, target):
  nums_dict = {}
  for i, n in enumerate(nums):
    nums_dict[n] = i
  
  for i, num in enumerate(nums):
    if (target - num) in nums_dict and i != nums_dict[target - num]:
      return i, nums_dict[target - num]

use_dict(nums, target)

###################
## Upgrade query ##
###################
def up_query(nums, target):
  nums_dict = {}
  for i, num in enumerate(nums):
    if target - num in nums_dict:
      return [nums_dict[target - num], i]
    nums_dict[num] = i

up_query(nums, target)
