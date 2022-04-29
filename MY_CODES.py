# PRACTICE FROM BASICS

# PRINTING A STRING USING PRINT FUNC..



from calendar import IllegalMonthError
from numpy import average, negative
import numpy


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
    print(bhuvan)

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
def all_inp():
    def valid_inp(): 
        
        print('1.SAMSUNG')
        print('2.REDMI')
        print('3.ONEPLUS')
        def loop():
            while True:
                try:
                    question = int(input('Out of these--[1,2,3] , which is your favourite MOBILE brand?: '))
                    print()
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
                loop()  # recursive func

        loop()
    valid_inp()

    print()

    list1 = []
    for lis in range(1, 11): # 1, 10
        list1.append(lis)
    print(list1)


    # List COMPREHENSIONS
    lis1 = [i for i in range(1,11)]
    print(lis1)

    print()



print('  ---   _TASKS_  ---    '    )
                    # ---- TASKS ---- #
print()

# TASK 1 --- Python Program to Calculate the Average of Three Numbers

def task1():
    print('TASK-1')
    while True:
        try:
            num1,num2,num3 = int(input('Enter a numeric value: ')), int(input('Enter a numeric value: ')), int(input('Enter a numeric value: '))
            average = num1 + num2 + num3 / 3                                                    
            print()
            print(f'Hey, here is your average: {average}')
            break
        except:
            print("That's invalid, enter a numeric value!")


# task1()



# TASK 2 --- Python Program to Exchange the Values of Two Numbers
def task2():

    print('TASK-2')
    k,n = 10,9
    print(k,n)
    k,n = n,k
    print(k,n)
# task2()

# TASK 3 --- Python Program to evaluate two expressions
def task3():
    print('TASK-3')

    exp1 = 4+6*9-3/2  # BODMAS
    print(exp1)

    exp2 = "-5**2+34>66+8/2*3"
    print(eval(exp2))

# task3()

# TASK 4 --- Python Program to print the below strings:
    # i) Ram's Hand
	# ii) Hi,
	#     My name is Ram

def task4():
    print('TASK-4')
    # printing -- Ram's Hand

    v = "Ram's Hand"
    b = 'Ram\'s Hand'
    print(b)
    print(v)

    #  printing -- Hi, -- next line--  My name is Ram

    kn= "Hi,\nMy name is Ram"
    print(kn)
    # another way
    name,intro = "Hi," , "My name is Ram"
    print(name,'\n',intro)
    print()
# task4()

# TASK 5 --- Python Program to perform below operations for the string "Besant Technologies"
def task5():
    print('TASK-5')
    inst = "Besant Technologies"
    # Printing first & second elements
    print(inst[:2])
    # Printing elements from 2nd to 5th index
    print(inst[2:5])
    # Printing all elements from 1st index
    print(inst[1:])
    # Printing the first word from the string (Besant) five times
    print(inst[:6] * 5)
# task5()

# TASK 6 --- Python Program to extract a word 'sita' from the string 'ram@gmail.com sita@gmail.com'
def task6():
    print('TASK-6')

    emails = 'ram@gmail.com sita@gmail.com'

    ind1= emails.find(' ') # 13
    print(ind1)

    ind2 = emails.find('@',ind1) # 18
    print(ind2)

    name = emails[ind1 + 1 : ind2]
    print(name)
#task6()


# TASK-- 7
def task7():
    print('TASK-7')

    a = 5
    # ways of printing a var with a str without using a comma

    print(f"Number: {a}") 
    print("Number: " + str(a))
    print("Number: %g" %(a))
    print("Number: {}".format(a))
# task7() 

# The new one...

# TASK 1 --- Python Program to Find the Second Largest Number and Third Smallest Number in a List [5, 6, 7, 7, 8, 1, 9, 9]

def task_1():

    list1 = [5, 6, 7, 7, 8, 1, 9, 9]
    elm_dupl = set(list1)
    print(elm_dupl)
    con_2_lis = list(elm_dupl)
    con_2_lis.sort()
    print('The second largest number is: ',con_2_lis[-2])
    con_2_lis.reverse()
    print('The third smallest number is: ', con_2_lis[-3])
# task_1() 
# TASK 2 ---  Python Program to to Remove Element 85 from a Tuple (14, 32, 16, 85, 47, 65)

def task_2():

    tup1 = (14, 32, 16, 85, 47, 65)
    con_lis = list(tup1)
    con_lis.remove(85)
    print(con_lis)
    con_tup = tuple(con_lis)
    print(con_tup)


# TASK 3 --- Python Program to create a Dictionary with each item as a pair. The items are a=(1,'k'), b=(2,'l')

def task_3():

    a=(1,'k')
    b=(2,'l')

    con_dict = dict(zip(a,b))
    print(con_dict)


# TASK 6 --- Using a while loop, print the sum of the first 100 numbers.

def task_6():
    num_ = 1
    sum1 = 0
    while num_<=100:
        sum1 = sum1 + num_
        # print(num_, ' : ', sum1)
        num_ +=1

    print(sum1)


def youtube():
    
    vv = 0
    data = int(input("Hey user, enter the number of minutes you have watched till now.. (enter 0 to end) : "))
    while data != 0:
        if vv == 0:
            min = data
        else:
            if data < min:
                min = data
        vv = vv + 1
        data = int(input("Hey user, enter the number of minutes you have watched till now..(enter 0 to end) "))
    print("Minimun value:",min)

# Python program that asks a user for what town Kean University is located in. If the user enters “Union”, print correct.
def task_4():
    ques_inp = input('where is kean university located: ')

    if ques_inp.upper() == 'UNION':
        print('HEY, You are CORRECT !')
    # elif ques_inp == 'Union'.lower():
    #     print('HEY, You are CORRECT !')
    # elif ques_inp == 'Union'.capitalize():
    #     print('HEY, You are CORRECT !')
    else:
        print('Your Wrong')
        print('The correct answer is : Union')

# task_4()

# Use a while loop to ask the user for 6 numbers.  Print the minimum number.
def task_7():
    while True:
        try:
            lis_1 = []
            summ = 0
            while summ < 6:
                a = int(input('enter value: '))
                summ+= 1

                lis_1.append(a)
            print('The minimum value is: ', min(lis_1))
            break
        except:
            print('Please Enter Numeric Expression: ')
# task_7()

# Write Python code that asks: x1, x2, y1 and y2. Calculate the slope of the line, slope = (y2-y1)/(x2-x1). If the slope is positive, print positive slope. If the slope is negative, print negative slope. If the slope is zero, print horizontal line. If the the denominator is 0, print vertical line.
def slope():
    while True:
        try:
            x1 = float(input('Enter a value for x1: '))
            y1 = float(input('Enter a value for y1: '))
            x2 = float(input('Enter a value for x2: '))
            y2 = float(input('Enter a value for y2: '))

            if (x2 - x1) == 0:
                print('vertical line') 
                break
            slp= (y2-y1)/(x2-x1)
            
            print('slope : ', slp)

            if slp > 0:
                print('positive slope')
            elif slp < 0:
                print('negative slope')
            elif slp == 0:
                print('horizontal line')  
            break
        except:
            print('Enter numeric val')
# slope()

# 12, -1, 24, 0
# 4, 2, 2, 5
# 12, -1, 1.3, 0

def dictionary():
    a1=(1,'k')
    b2=(2,'l')

    con_dic = dict((a1,b2))
    print(con_dic)

# dictionary()

                                    # PYTHON_TASK_3 #
# TASK 1 --  Using a for loop, ask the user for 5 numbers. Print the minimum of these numbers.
def loop_5():
    ap_lis = []
    while True:
        try:
            for i in range(5):
                as_inp = int(input('Enter a value: '))
                ap_lis.append(as_inp)
            print('The minimum value is: ', min(ap_lis))
            break
        except:
            print('Please enter a numeric value..')
# loop_5()


# TASK 2 -- Using a for loop, print odd numbers from 1 to 20.
def evod():
    # LIST COMPREHENSION
    evodnum1 =  [i for i in range(1,20)  if i%2 == 0 ]
    print('Odd Numbers:', evodnum1)


# evod()

# TASK 3 -- Use a for loop - Running on a treadmill, you burn 4.5 calories per minute. Write Python code that displays the number of calories burned after 10, 15, 20, 25 and 30 minutes.
def calories():
    calor_per_min = 4.5
    for i in range(10,31,5):
        calories = i * calor_per_min
        print('You burned',calories,'calories in', i,'Minutes')
# calories()


# TASK 4 -- Create a list of 5 numbers that contains positive and negative numbers.
# Print the list.  Delete all of the negative numbers. Print the list again.

def elm_neg():
    ps_ng = [23, -44, 56, -34, 22]
    print(ps_ng)

    for neg in ps_ng:
        if neg < 0:
           ps_ng.remove(neg)
    print(ps_ng)
# elm_neg()

# def elm_neg():
#     ps_ng = [23, -44, 56, -34, 22]
#     print(ps_ng)

#     ps_list = [i for i in ps_ng if i > 0]
#     print(ps_list)

#     ps_ng = ps_list
#     print(ps_ng)
# # elm_neg()

# TASK 5 --  Create a list of 5 numbers. Print the list.  Print the position of the largest element.
def f_lrg():
    f_lrg = [12,234,230,876,43]
    print(f_lrg.index(max(f_lrg)))
# f_lrg()

# TASK 6 -- Create a list of 10 positive and negative numbers. Print the average of the positive numbers and average of the negative numbers.
def f_aver():
    pos_neg = [1,-1,2,-2,3,-3,4,-4,5,-5,6,-6,7,-7,8,-8,9,-9,10,-10]
    elm = [i for i in pos_neg if i > 0]
    elm_p = [x for x in pos_neg if x < 0]
    print(f'Positive Numbers: {elm}')
    print(f'Negative Numbers: {elm_p}')
    print(numpy.average(elm))
    print(numpy.average(elm_p))
# f_aver()

# TASK 7 -- Create a list of 10 numbers that contains positive and negative numbers.  Print the list.  Print the number of odd numbers, even numbers and zeros.def ext_evod():
    
    f_evod = [0,-9, 16, 25, -36, 49, -64, 81, -2, 0]

    positive_l = []
    negative_l = []
    zeros_l    = []

    for i in f_evod:
        if i > 0:
            positive_l.append(i)
        elif i < 0:
            negative_l.append(i)
        elif i == 0:
            zeros_l.append(i)

    
    print('Positive_num_count: ', len(positive_l))
    print('Negative_num_count: ', len(negative_l))
    print('Zeros_count: ', len(zeros_l))


# ext_evod()            

    # num_eve = [y for y in f_evod if y > 0]
    # print('Number of Even Nums in the List:', len(num_eve))

    # num_odd = [l for l in f_evod if l < 0]
    # print('Number of Odd Nums in the List:', len(num_odd))

    # num_zrs = [o for o in f_evod if o == 0]
    # print('Number of Zeros in the List:', len(num_zrs))
# ext_evod()

# TASK 8 -- Create a Dictionary, write a program to rename a key in that dictionary.
def re_key():
    dict_x = {'nithya': 14, 'koushil': 15, 'likith': 21}
    print(dict_x)

    # # RE-ASSIGNING VALUE
    # dict_x['likith'] = 12
    # print(dict_x)

    # RE-NAMING KEY
    dict_x['Madan'] = dict_x.pop('likith')
    print(dict_x)

# re_key()

# TASK 11 --  Create a string made of the middle three characters.
def mid_():
    str2 = 'brand'
    midd = int(len(str2) / 2)
    extr = str2[midd - 1  :midd + 2]
    print("Middle three chars are:", extr)
# mid_()

print()
# TASK 10 -- Create a string and make another new string with first, middle and last character of the old string.
def cr_str():
    str1 = 'BAND'
    str_ext = str1[0] + str1[int(len(str1) / 2) - 1] + str1[-1] 
    print(str_ext)

# variable = 'NITHYANISHA is Fourteen'
# print(variable.count('Nisha'))

# var_1 = 'NithyaNisha is fourteen'
# ff = var_1.upper() or var_1.lower() 
# print(ff.count('NISHA'))

"""d1 = dict()
for c in ff:
    if c in d1:
        d1[c]+=1
    else:
        d1[c] = 1
print(d1)
"""

# CONTINUE STATEMENT

def prt_evn_num():

    for i in range(1,11):
        if i%2 == 1:
            continue    
        else:
            print(i, end = ' ')

def tables():
    for i in range(1,11):
        print()
        for x in range(1,11):
            print(i ,'x',x ,'=',i*x)

def k_ar():
    # Keyword arg
    def mult(y):
        return y*y-2
    print(mult(3))

def lam():
    # Lambda Function
    lambda_r = lambda r: r*r-2
    print(lambda_r(3))

# Length arg
def l_ar():
    def game(*games):
        for i in games:
            print(i, end=' <--> ' )
    game('fortnite','pubg','COD')

print()
print()

def k_ln():
# Keworded Length arg
    def dic_func(**details):
        for key,value in details.items():
            print("{}: {}".format(key,value))
    dic_func(Name = "Nithya", Age = 14, Number = 9456378920)


