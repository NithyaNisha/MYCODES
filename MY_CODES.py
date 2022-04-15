# PRACTICE FROM BASICS

# PRINTING A STRING USING PRINT FUNC..

def my_codes():

    print('Hello USER..!')

    # Variables... 
    # PRINTING AGE 
    ram = 22
    nisha = 14
    bhuvan = 19

    print(ram)
    print() # prints a new empty line

    # INSTEAD
    # ASSIGNING MULTIPLE VAR IN A SINGLE LINE

    ram, nisha, bhuvan = 22,14,19

    print(ram)
    print(nisha)


    # Anything inside single qoutes or double quotes are STRINGS...

    #--STRINGS--is a sequence of characters
    nithya = ' i am 14'
    add = nithya + ' ' + 'years old ' #in str-- '+' means concatenating two str
    print(add)
    print()

    print(add[3]) #indexing
    print(len(add)) #counts the total elements in the str inc spaces
    print(add.count('old')) #counts the number of times repeated
    print(add.upper())
    print(add.capitalize())
    print(add.lower())
    print(add.casefold())
    print(add.find('14'))
    print(add.startswith('i'))
    print(add.startswith(' '))
    print(add.endswith('j'))
    print(add.endswith(' '))
    print(add.isnumeric())
    print(add.strip())
    print(add.index('y'))
    print(add.join(['hey!','elder than you',]))
    print(add.split())
    rplace = add.replace('am','Am')
    print(rplace)
    # DATA STRUCTURES -- organisiing a data in a systamatic way,accessing in a efficient way based on a situation

    # PRIMITIVE DS(data_structure) -- BASIC TYPES IN PYTHON, EX : INT,FLOAT, BOOL, COMPLEX

    i1 = 1
    print(type(i1)) # USED TO FIND THE TYPE of i1
    print(type(2.34821)) # a float is represted with a dot(decimel)
    print(type(True)) # A boolean consists of either True or False..
    print(type(1+44j)) # Returns the type AS complex

    # NON-PRIMITIVE DS -- USER DEFINED, STORINNG MULTIPLE VALUES IN A SINGLE IDENTITY
    # CONSISTS two types
    # -- LINEAR DS-- SEQUENCIAL ...EX: LIST,TUPLE,STACK,QUEUE
    # -- Non linear DS -- non sequen... ex: set,dict,tree, graph
    # -- Conditional DS
                        # --- LINEAR DS --- #
            #---LIST--Mutable,allows duplicate elements

    list1 = ['nisha','dhanush','pranav']
    print(list1)
    list2 = [] #creates empty list
    list2.append('apples')
    list2.extend(['bananas','watermelon'])
    print(list2.count('watermelon'))
    list2.insert(2,'strawberry')
    print(len(list2))
    print(list2)
    print(list2.index('bananas'))
    print(list2.pop(3))
    print(list2)
    print(list2.sort())
    list2.remove('apples')
    print(list2)
    list2.reverse()
    print(list2)
    list2.clear()
    print(list2)
    print()


        #--TUPLES--Immutable,allows duplicate elements
    tup = ('23',2,34,2,2,45,767)
    print(tup)
    print(tup.count(2))
    print(tup.index('23'))

                        # --- NON_LINEAR DS --- #


        #--Sets--unordered,unindexed,no duplicate elements allowed
    set1 = {'hello','world','hello',234,454,234,'nisha'}
    print(set1)
    print(len(set1))
    set1.add('karl')
    print(set1)
    set1.remove(234)
    print(set1)

        #--Dictionary--unordered,mutable,no duplicate elements allowed

    dict1 = {} #empty dict
    dict1['nithya'] = '14'
    print(dict1)
    dict2 = ['onion','tomato','ginger']
    dict3 = [34,32,12]
    joinn = dict(sorted(zip(dict2,dict3)))
    print(joinn)
    print(joinn.get('tomato'))
    print(joinn.items()) #List of tuples
    print(joinn.keys())
    print(joinn.values())
    print(joinn.pop('onion'))
    print(joinn)



                     # --- CONDITIONAL DS --- #

def valid_inp(): 
    
    print('1.BLACK')
    print('2.BLUE')
    print('3.BROWN')
    def loop():
        while True:
            try:
                question = int(input('Out of these--[1,2,3] , which is your favourite colour?: '))
                break
            except:
                print("That's not a valid option!")

        if question == 1:
            print('Nice!')
        elif question == 2:
            print('Cool')
        elif question == 3:
            print('Awesome!')
        else:
            print("That's not an option!")
            loop()

    loop()
valid_inp()


list1 = []
for lis in range(1, 11): # 1, 10
    list1.append(lis)
print(list1)

# List COMPREHENSIONS
lis1 = [i for i in range(1,11)]
print(lis1)

print()
def evod():
    evodnum = []

    for x in range(1,11):
        if x%2 == 0:
            evodnum.append(str(x)+ " : Even")
        else:
            evodnum.append(str(x) + " : Odd")
    print(evodnum)

    # LIST COMPREHENSION

    evodnum1 = [str(i) + " : Even" if i%2 == 0 else str(i) +" : Odd" for i in range(1,11)]
    print(evodnum1)


                    # ---- TASKS ---- #
# TASK 4 --- Python Program to print the below strings:
	# ii) Hi,
	 #    My name is Ram
print('TASK-4')
# printing -- Ram's Hand
v = "Ram's Hand"
print(v)
#  printing -- Hi, -- next line--  My name is Ram
kn= "Hi,\nMy name is Ram"
print(kn)

print()

# TASK 2 --- Python Program to Exchange the Values of Two Numbers
print('TASK-2')
k,n = 10,9
print(k,n)
k,n = n,k
print(k,n)

print()

# TASK 5 --- Python Program to perform below operations for the string "Besant Technologies"
print('TASK-5')
inst = "Besant Technologies"
# Printing first & second elements
print(inst[:2])
# Printing elements from 2nd to 5th index
print(inst[2:5])
# Printing all elements from 1st index
print(inst[1:])
# Printing the first word from the string (Besant) five times
for i in range(5):
    print(inst[:6], end='')
    


















