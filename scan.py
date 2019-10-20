# scan.py
# Performs inclusive and exclusive scan operations on a list.

def plus(a, b):
    return a + b

def times(a, b):
    return a * b

# Perform an inclusive scan operation on my_list, given an operation op.
# When done, my_list[i] should contain the result of the operation
# performed on my_list[0] through my_list[i], and my_list[0] should
# remain unchanged.
def inclusive_scan(my_list,op):
    #state a starting position

    for i in range(1,len(my_list)):
        my_list[i]= op(my_list[i], my_list[i-1])

#test new code

# dans_list = [3, 6, 2, 1, 4, 7]
# print(inclusive_scan(dans_list,plus))
# print(inclusive_scan(dans_list,times))
# #print(inclusive_scan(dans_list))

    # range and len functions in the for-loop headers.
# (You’ll probably find the two-argument form of range useful.)

# Perform an exclusive scan operation on my_list, given an operation op
# and the identity id for the operation.  When done, my_list[i] should
# contain the result of the operation performed on my_list[0] through
# my_list[i-1], and my_list[0] should contain the identity.
# id to whatever is in the index
#
def exclusive_scan(my_list, op, id):
    t1=id


#what info do I currently have vs what I want?
    for i in range(1,len(my_list)):
         t2 = my_list[i]
         my_list[i]=op(t1,my_list[i-1])
         t1=t2
    my_list[0] = id




numbers = [3, 6, 2, 1, 4, 7]
print(len(numbers))
print("The list: ", numbers)
exclusive_scan(numbers, plus, 0)
print("After an exclusive plus-scan:", numbers)

numbers = [3, 6, 2, 1, 4, 7]
print("The list: ", numbers)
inclusive_scan(numbers, plus)
print("After an inclusive plus-scan:", numbers)

numbers = [2, 4, 2, 6, 2]
print("The list: ", numbers)
exclusive_scan(numbers, times, 1)
print("After an exclusive times-scan:", numbers)

numbers = [2, 4, 2, 6, 2]
print("The list: ", numbers)
inclusive_scan(numbers, times)
print("After an inclusive times-scan:", numbers)