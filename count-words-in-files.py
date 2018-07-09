"""
Output word counts in text files in
current working directory
"""

from collections import Counter
from glob import iglob
import re
import os

topwords = 100
folderpath = os.getcwd()
counter = Counter()
for filepath in iglob(os.path.join(folderpath, '*.txt')):
    with open(filepath) as file:
        counter.update(file.read().split())

for word, count in counter.most_common(topwords):
    print('{}: {}'.format(count, word))

