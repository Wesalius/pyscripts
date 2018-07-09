from collections import OrderedDict

keys = open("keys.txt").readlines()
keys = [i.replace("\n", "") for i in keys]
values = open("values.txt").readlines()
values = [i.replace("\n", "") for i in values]
dictionary = OrderedDict(zip(keys, values))
