#Program Name 4.3 Print all index number of the same item
L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

R = {n: rep[n] for rep in [{}] for i, n in enumerate(L)
     if rep.setdefault(n, []).append(i) or len(rep[n]) == 2}
print(R)
