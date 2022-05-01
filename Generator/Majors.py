import random

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

def students_list(num_students):
    #li = []
    #for i in range(num_students):
    #    j = names[random.randint(0,5)]
    #    k = majors[random.randint(0,4)]
    #    t = (i,j,k)

    #    li.append(t)
    li = [(i,names[random.randint(0,5)],majors[random.randint(0,4)]) for i in range(num_students)]
    return li


def students_generator(num_students):
    li = ((i,names[random.randint(0,5)],majors[random.randint(0,4)]) for i in range(num_students))
    return li

#people = students_list(1000000)
people = students_generator(1000000)

print(next(people))
print(next(people))
print(next(people))
print(next(people))
print(next(people))