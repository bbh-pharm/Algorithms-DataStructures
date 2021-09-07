num = int(input())
N_list = [int(n) for n in input().split()]

assert len(N_list) == num

print(min(N_list), max(N_list))
