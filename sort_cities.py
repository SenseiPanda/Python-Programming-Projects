

my_list= ['London','New York','Sydney','Tokyo','Paris']
#my_list= [3,7,1,9,5,6,7,8]

def partition(the_list,p,r):

#initially place the pivot at the end of the list
    pivot = the_list[r]
#start j at the beginning and i at the super beginning
    i = p-1

#kick higher values to the right side of the list, lower to the left, and return pivot
    for j in range (p,r):
        if the_list[j]<=pivot:
            i = i + 1
            the_list[i], the_list[j] = the_list[j],the_list[i]
    the_list[i + 1], the_list[r] = the_list[r], the_list[i + 1]
    return i+1



def quicksort(the_list, p = 0, r = None):
    if r== None:
        r= len(the_list)-1
    if len(the_list)<2:
        return
    elif p<=r:
#get that pivot point

        q = (partition(the_list,p,r))
#quicksort the first half of the list
        quicksort(the_list, p, q - 1)
#now quicksort the latter half
        quicksort(the_list, q + 1, r)
#give the user back the sorted list
    return the_list

print(quicksort(my_list))