let = ['a','b','c','d','e','a','a','b','c']
print({k: [i for i, j in enumerate(let) if j == k] for k in let})
