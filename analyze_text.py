# analyze_text.py
# Codebase for CS 1 Short Assignment 10.
# Uses the suffix array and lcp list to analyze texts.
from substrinfo import SubstrInfo
from suffix_array import *

# Read a file whose name is given as a parameter into a text string
# and return the text string.

# For example, you could set text to bippityboppityboo and verify that the list
# returned by find_longest_repeated_substrings has just one string, and it’s ppitybo.
# Then try it with text that has no repeated substrings, i.e., all characters are unique.
# And then with text that has multiple, but different, longest repeated substrings.

# full_text = str(text1)+str(divider)+str(text2)
# s_a = make_suffix_array(full_text)
# lcp = make_lcp(full_text)

#max lcp- says how many characters long the item is

#sa is a list of indices indicating where a substring exists
def read_file(file_name):
    in_file = open(file_name, "r")

    text = ""
    for line in in_file:
        text += line.strip() + " "

    in_file.close()
    return text

# Return a list of all longest repeated substrings in a text.

def return_substring(string, n):
    return str(string)[n - 1]
def find_longest_repeated_substrings(text):
    global n1, n2
    sf_array = make_suffix_array(text)
    lcp =make_lcp(text,sf_array)
    print_suffix_array(text, sf_array, lcp)
    i =(lcp.index(max(lcp))) #the index in LCP array where max LCP lives
    position =(sf_array[i]) #the position in the text where max LCP starts
    return(text[position:position+lcp[i]])



# Return a list of all longest common substrings between text1 and text2.
# divider_char may not appear in either text.
def find_longest_common_substrings(text1, text2, divider_char):
    text = text1+divider_char+text2
    sf_array = make_suffix_array(text)
    lcp =make_lcp(text,sf_array)
    max_lcp = 0
    common_substrings = []
    for i in range(1, len(lcp)):
        if (sf_array[i - 1] < n1 and sf_array[i] > n1) or (sf_array[i - 1] > n1 and sf_array[i] < n1):
            if lcp[i] > max_lcp:
                max_lcp = lcp[i] #this is the length of the max lcp
    for i in range(1, len(lcp)):
        if lcp[i] == max_lcp:
            position = (sf_array[i])
            thing =(text[position:position+lcp[i]])
            common_substrings.append(thing)

    return common_substrings


# Print all longest substrings.
def report_longest_substrings(longest_substrings, type):
    if len(longest_substrings) == 0:
        print("No " + type + " substrings")
    elif len(longest_substrings) == 1:
        print("Longest " + type + " substring, of length " + str(len(longest_substrings[0])) + ":")
    else:
        print("Longest " + type + " substrings, of length " + str(len(longest_substrings[0])) + ":")
    for substring in longest_substrings:
        print(substring)

text = "bippityboppityboo"
print(find_longest_repeated_substrings(text))

# longest_repeated_substrings = find_longest_repeated_substrings(text)
# print("For jellyfish GFP gene")
# report_longest_substrings(longest_repeated_substrings, "repeated")
#
# # text = read_file("moby-dick.txt")
# # longest_repeated_substrings = find_longest_repeated_substrings(text)
# # print("\nFor Moby Dick")
# # report_longest_substrings(longest_repeated_substrings, "repeated")
# #
# # text1 = read_file("moby-chap1.txt")
# # text2 = read_file("moby-chap2.txt")
# # n1 = len(text1)
# # n2 = len(text2)
# # longest_common_substrings = find_longest_common_substrings(text1, text2, "@")
# # print("\nFor Moby Dick chapters 1 and 2")
# # report_longest_substrings(longest_common_substrings, "common")
#
# text1 = read_file("Michelle.txt")
# text2 = read_file("Melania.txt")
# n1 = len(text1)
# n2 = len(text2)
# longest_common_substrings = find_longest_common_substrings(text1, text2, "@")
# print("\nFor Michelle Obama's and Melania Trump's speeches")
# report_longest_substrings(longest_common_substrings, "common")
#
# # text = read_file("mouse-chromosome-1.txt")
# # longest_repeated_substrings = find_longest_repeated_substrings(text)
# # print('\nFor mouse chromosome 1')
# # report_longest_substrings(longest_repeated_substrings, "repeated")