from collections import defaultdict
#for a list
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
d['b'].append(4)
print(d)

#for a set - no repitition of values
e = defaultdict(set)
e['a'].add(1)
e['a'].add(2)
e['b'].add(4)
e['b'].add(4)
print(e)
