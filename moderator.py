def combine(a, b, c) :
    for i in a :
        yield i
    for i in b :
        yield i
    for i in c :
        yield i
 
L = [1,2,3,4,5]
for i in combine(L, range(10,15), "ABCDEF"):
    print(i, end = ' ')


#square

def generate_squares(start, stop):
    while start <= stop:
        yield start * start
        start += 1
g = generate_squares(2,9)
 
for i in g:
    print(i)


#reverse
def reverse(sequence):
    for i in range(len(sequence)-1, -1, -1):
        yield sequence[i]
 
for value in reverse([1,2,3,4]):
     print(value)
