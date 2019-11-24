def print_sort_dictionary(dictionary):
    sorted_dictionary = sorted(dictionary.items(), key = lambda x:x[1], reverse = True)
    for key in sorted_dictionary:
        print(key)
def strip_word(w):
    w = w.replace(".", "")
    w = w.replace(",", "")
    w = w.replace(";", "")
    w = w.replace(":", "")
    w = w.replace("'", "")
    w = w.replace("&", "")
    w = w.replace("\n", "")
    w = w.lower()
    return w

DOI_dictionary = {}
def read_file(file_name):
    in_file = open(file_name, "r")
    for line in in_file:
        words =line.split(' ')
        for w in words:
            w = strip_word(w)
            if len(w)>0:
                if w in DOI_dictionary:
                    DOI_dictionary[w] +=1
                else:
                    DOI_dictionary[w] = 1

    in_file.close()
    return print_sort_dictionary(DOI_dictionary)


print(read_file('DOI.txt'))



#if key exists, increment value
#otherwise increment the value






