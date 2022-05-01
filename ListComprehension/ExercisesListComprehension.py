# Ex1: Ex 1: Alphabet List Comprehensions

from this import s


alphabet = []

for i in range(65,91):
    alphabet.append(chr(i))

#print (alphabet)

alphabet2 = []

for i in range(65,91):
    if i not in [70,75,80,85]:
        alphabet2.append(chr(i))

#print(alphabet2)
   
alphabet3 = []

for i in range(65,91):
    if i not in range(70,80,2):
        alphabet3.append(chr(i))

#print(alphabet3)

# Ex 2: Clothes List Comprehension
colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']
newArray = [(i,c) for i in colors for c in sizes] 
print(newArray)

soled_out = [('Black', 'm'), ('White', 's')]
newArray2 = [(i,c) for i in colors for c in sizes if (i,c) not in soled_out]
print(newArray2)

# Ex 3: List & tuple exercises
# NOPE

# Ex 4: Sys module exercise
# YEPGE

# Ex 5: OS Module exercise
# YEPGE

# Ex 6: Extract .py files

# Ex 7: Simple scraber with requests