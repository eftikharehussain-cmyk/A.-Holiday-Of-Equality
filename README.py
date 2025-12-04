# A.-Holiday-Of-Equality
n = int(input())
lst = list(map(int, input().split()))
lst.sort()
lst1 = []
_max = max(lst)
for i in range(n - 1):
	if lst[i] != _max:
		s = _max - lst[i]
		lst1.append(s)
print(sum(lst1))
