
#month of the yesr
def months_of_year():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
               'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    i = 0
    while True:
        yield months[i]
        i = (i+1) % 12
g = months_of_year()    
 
for i in range(20):
   print(next(g), end=' ')


#multilples of a number

def generate_multiples(number, n):
    for i in range(n):
        yield number * (i+1)
 
for i in generate_multiples(6, 10):
    print(i, end = ' ')

print('--------------')
#factors
def gen_factors(n):
    for i in range(1, n+1):
        if n%i == 0:
            yield i
 
for i in gen_factors(500):
    print(i, end = ' ')


print('------------------------------------')
def enumerate1(sequence, start=0):
    n = start
    for element in sequence:
        yield n, element
        n += 1
 
L = [10,20,30]
t = (8,9,10,11,12)
 
for i, value in enumerate1(L):
    print(i, value)
for i, value in enumerate1(t,4):
    print(i, value)

