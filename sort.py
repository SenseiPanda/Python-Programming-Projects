


def partition(the_list,p,r):

    pivot = the_list[r]
    i = p-1
    j = p
    while j<=r:
        if the_list[j]>pivot:
            j = j+1
        elif the_list[j]<=pivot:
            i = i + 1
            the_list[i], the_list[j] = the_list[j],the_list[i]
            j = j+1
        elif j==r:
            the_list[r] == the_list[i+1]
            return
    return i+1



def quicksort(the_list, p = 0, r = None):

    if r== None:
        r= len(the_list) - 1

    if len(the_list)<2:

        return
    elif p<r:
        q = (partition(0,the_list,p,r))
        quicksort(the_list, p, q - 1)
        quicksort(the_list, q + 1, r)


    return the_list
my_list = [10, 7, 8, 9, 1, 5,1,1,1,1,1,1,1]
d = ['yes','no','maybe','derp','have']
print(partition(my_list,0,10))

#quicksort(derp)








