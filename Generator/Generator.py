from re import X
from time import sleep

def compute():
    li = []
    for i in range(10):
        li.append(i)
        sleep(.5)
    return li



#print(compute())

class Compute:
    def __call__(self):
        li = []
        for i in range(10):
            li.append(i)
            sleep(.5)
        return li





class Computer:
    def __iter__(self):
        self.last = 0
        return self
    
    def __next__(self):
        if self.last > 5:
            raise StopIteration
        else:
            self.last += 1
            return self.last

compute = Computer()
it = iter(compute)

#print(next(it))


#for i in compute:
#    print(i)


def gen_compute(x):
    for i in range(x):
        yield i

it = gen_compute(100000)


li_comprehension = [i for i in range(10)]

#print(li_comprehension)

