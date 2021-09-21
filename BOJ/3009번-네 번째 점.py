# Function to remove duplicated elements
def remainder(num_list):
  result = num_list.copy()
  for n in num_list:
    if result.count(n) == 2:
      result = list(filter(lambda x: x!= n, result))
  return result[0]

# Input 3 point of box
point_dict = {'x': [], 'y': []}
for n in range(3):
  x, y = map(int, input().split())
  point_dict["x"].append(x)
  point_dict["y"].append(y)

# Print answer
print(remainder(point_dict["x"]), remainder(point_dict["y"]))
