"""32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 ->
6 -> 4 -> 21 ->
65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 ->
No common element in the Linked lists
3 ->
No common element in the Linked lists
"""
a="65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 -> "
a=a.split(' -> ')
print(a)
b=[int(i) for i in a[:len(a)-1]]
print(b)