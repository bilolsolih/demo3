d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
d3 = {}
keys_set = {*d1.keys(), *d2.keys()}

for key in keys_set:
    d3[key] = 0

for dictionary in [d1, d2]:
    for key, value in dictionary.items():
        d3[key] += value
print(d3)
