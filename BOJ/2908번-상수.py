A, B = input().split()

def get_reverse(chr_num):
  return ''.join([list(chr_num)[-i] for i in range(1, len(list(chr_num))+1)])

A_reverse = int(get_reverse(A))
B_reverse = int(get_reverse(B))
print(max([A_reverse, B_reverse]))
