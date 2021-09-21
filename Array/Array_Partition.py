nums = [1, 4, 3, 2]

###############
## Ascending ##
###############
def array_partition(nums):
  sum = 0
  nums.sort()
  pair = []

  for n in nums:
    pair.append(n)
    if len(pair) == 2:
      sum += min(pair)
      pair = []
  return sum

array_partition(nums)

######################
## Using even order ##
######################
def array_partition(nums):
  sum = 0
  nums.sort()

  for i, n in enumerate(nums):
    if i % 2 == 0:
      sum += n
  return sum

array_partition(nums)

####################
## Other method 1 ##
####################
def array_partition(nums):
  nums.sort()
  sum = nums[0] + nums[-2]
  return sum

array_partition(nums)

####################
## Other method 2 ##
####################
def array_partition(nums):
  return sum(sorted(nums)[::2])

array_partition(nums)
