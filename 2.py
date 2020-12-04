a = {1, 2, 3, 4, 5}
b = {2, 4, 5, 9, 0, 10}
in = 0
un = 0
for i in a:
    if i in b:
        in += 1
un = len(a) + len(b) - in
print(in/un)
