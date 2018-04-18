from collections import OrderedDict
d = OrderedDict()
d['foo'] = 2
d['bar'] = 1
d['spam'] = 3
d['grok'] = 4
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
    print(key, d[key])

#remove duplicates or just make a set
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
    
a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))
print(a)