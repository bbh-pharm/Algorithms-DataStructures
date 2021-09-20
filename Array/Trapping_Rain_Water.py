heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

#######################
## Using two pointer ##
#######################
def trapping_rain(heights):
  volume = 0
  # Left, right is index for going toward highest
  left, right = 0, len(heights)-1
  # Left max, right max is for computing water volume
  left_max, right_max = heights[left], heights[right]

  while left < right:
    left_max, right_max = max(heights[left], left_max), max(heights[right], right_max)

    if left_max <= right_max:
      volume += left_max - heights[left]
      left += 1
    else:
      volume += right_max - heights[right]
      right -= 1
  return volume

trapping_rain(heights)

#################
## Using stack ##
#################
# To be honest, it's not understanded exactly...
# so I'll review it next time 
def trapping_rain(heights):
  stack = []
  volume = 0

  for i in range(len(heights)):
    while stack and heights[i] > heights[stack[-1]]:
      top = stack.pop()

      if not len(stack):
        break
      
      distance = i - stack[-1] - 1
      waters = min(heights[i], heights[stack[-1]]) - heights[top]

      volume += distance * waters

    stack.append(i)
  return volume

trapping_rain(heights)
