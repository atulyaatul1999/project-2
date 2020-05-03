"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
b = set()
c=set()
for i, j in zip(texts, calls):
    b.add(j[0])
    c.add(j[1])
    c.add(i[0])
    c.add(i[1])
b=b.difference(c)
b=list(b)
print("These numbers could be telemarketers: ")
for word in sorted(b):
    print(word)
"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

