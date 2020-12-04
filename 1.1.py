let = ['a','b','c','d','e','a','a','b','c']
r = {}
for i in range(len(let)):
    r[let[i]] = r.get(let[i], []) + [i]
print(r)
