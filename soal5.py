import random
import string

def cetak(n=0):
    if n > 1:
        data = set()
        while len(data) < n:
            x = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(32))
            data.add(x)
        for i in data:
            print(i)
    else:
        print('input salah')
        
cetak(3)