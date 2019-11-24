


def gray(n):
    recursive_result = []
    gray_result = []
    #stop recursion at zero
    if n==0:
        return ['']  #return empty string so it's able to add to future recursions of n
    if n==1:
        return ['0','1']   #base case result

    gray_result = gray(n-1)
    for result in gray_result:
        recursive_result = [result] + recursive_result
    for i in range(len(gray_result)):
         gray_result[i] = '0' + gray_result[i]
    for i in range(len(recursive_result)):
        recursive_result[i] = '0'+ recursive_result[i]
    reverse_result = recursive_result[::-1]
    for i in range(n-1):
        reverse_result[i] = '1'+ reverse_result[i]

    return recursive_result + reverse_result



print(gray(3))


#Recursively call gray to form a Gray code for the numbers 0 to 2n − 1 − 1 with n − 1 bits per number
#     if len(recursive_result[i]) < n:
#         recursive_result[i] = '0' + recursive_result[i]
# recursive_result[3] = '0' + recursive_result[3]
# #reverse the string
# print(recursive_result[::-1])
#
