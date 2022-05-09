# We will be going thru different applications of list comprehensions in Python.

# Squaring each element in a list.

from re import I

from pkg_resources import yield_lines


def makeAlist(num):
    A = [];
    for i in range(1,num+1):
        A.append(i);
    return A;

sample = makeAlist(10);

myList = []
for i in sample:
    myList.append(i*i);

# with comprehension: 
myList = [i*i for i in sample]
print(myList,'\n') 

# What is there is a conditional? 

print('with for-loop')
myList = [];
for i in sample:
    if i%2 == 0:
        myList.append(i*i);

print(myList,'\n') 

# Adding the conditional to the comprehension: 

myList = []
myList = [i*i for i in sample if i%2==0]
print(myList)

# Great, now what is we want something that is more difficult? Like nested for loops?


myList = []
for i in 'abcd':
    for j in range(4):
        myList.append((i,j))

print('Nested Loop Output', myList)

# Making this into a comprehension. 
myList = []
myList = [(letter,num) for letter in 'abcd' for num in range(4)]
print('Comprehension Loop', myList,'\n')


# Dictionary Comprehensions: 

heroes = ['batman','superman','spiderman','wolverine','deadpool']
names = ['bruce','clark','peter','logan','wade']

myHero = {}
for name,hero in zip(names,heroes):
    myHero[hero] = name;
print("for loop dictionary construction",myHero)

# Using the comprehension; 
myHero = {}; 
myHero = {hero:name for name,hero in zip(names,heroes)}

print('\nUsing the comprehension: ',myHero)

# Sets allow us to have a list that does not contain duplicates; 
sample_2 = [1,1,2,2,3,4,4,4,4,5,6,7,8,9,9,9,9,10];
mySet = set();
for i in sample_2:
    mySet.add(i)
print(mySet)

# Notice that is is basically a dictionary.

mySet = {}
mySet = {i for i in sample_2}


print(mySet,sample_2)


# WHAT If we decide to do a generator: 

def gen_fun(nums):
    for i in nums:
        yield i*i
a = gen_fun(sample)

for i in gen_fun(sample):
    print(i)

myGen = (i*i for i in sample)
print(i for i in myGen)