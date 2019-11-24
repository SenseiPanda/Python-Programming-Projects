

def gray(n):
    recursive_result = []
    reverse_result = []
    #stop recursion at zero
    if n==0:
        return ['']  #return empty string so it's able to add to future recursions of n
    if n==1:
        return ['0','1']   #base case result
    j = 2^n-1
    while j>1:
        recursive_result =gray(n-1)
        j = j-1
    reverse_result = recursive_result[::-1]

    # for result in recursive_result:
    #     recursive_result = [result] + recursive_result
    for i in range(len(recursive_result)):
         recursive_result[i] = '0' + recursive_result[i]
    # for i in range(len(recursive_result)):
    #     recursive_result[i] = '0'+ recursive_result[i]
    #
    for i in range(len(reverse_result)):
        reverse_result[i] = '1'+ reverse_result[i]
    return recursive_result + reverse_result



print(gray(5))