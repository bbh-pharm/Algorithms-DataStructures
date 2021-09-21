nums = [1, 2, 3, 4]

def product(nums):
  out = []
  p = 1
  # Left side
  for i in range(0, len(nums)):
    out.append(p)
    p = p * nums[i]
  p = 1
  # Right side
  for i in range(len(nums) - 1, 0 - 1, -1):
    out[i] = out[i] * p
    p = p*nums[i]
  return out

product(nums)
