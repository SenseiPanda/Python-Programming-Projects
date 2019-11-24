

#read in the first line of a ciphertext file


cipher_file_1 = 'ciphertext1.txt'

cipher_file_2 = 'ciphertext2.txt'


def read_file(file_name):
    in_file = open(file_name, "r")

    text = ""
    for line in in_file:

        text += line.strip() + " "
        print(line)

    in_file.close()
    return text


read_file(cipher_file_1)