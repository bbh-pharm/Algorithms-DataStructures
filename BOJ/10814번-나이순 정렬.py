N = int(input())
group = []

for n in range(N):
  age, name = input().split()
  group.append((int(age), name))
group.sort(key=lambda age_name: age_name[0])
for age, name in group:
  print(age, name)
