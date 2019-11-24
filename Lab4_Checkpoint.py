
BYTE_SIZE = 8

def int_to_bytes(x, size):
    result = bytearray()
    mask = 0xFF     # mask for isolating least significant byte

    for i in range(size):
        result.append(x & mask)
        x >>= BYTE_SIZE

    return result

KEY = 295556873421021697574671957841159273934
#now convert to int
my_key = int_to_bytes(KEY,16)
my_string = 'extraterrestrial'
my_block_string = bytearray(my_string, 'UTF-8')
print("myblocksring is "+str(my_block_string))
#block - use a string of 16 bytes = "extraterrestrial" convert with 'ncode' which gives you a bytes object

#this will be block
def xor_block(key, block):
    assert len(key) >= len(block)
    #take two byte array objects and put together
    #if numbers are same you get zero, if numbers are different you get 1
    #use an if-else statement
    my_byte_array = bytearray()
    print("block is "+str(block))
    print("key is "+str(key))
    for i in range(0,len(key)):
        result = key[i] ^ block[i]
        my_byte_array.append(result)
    print(my_byte_array)
    return my_byte_array




xored_block = xor_block(my_key,my_block_string)

print(xor_block(my_key,xored_block))


KEY = 295556873421021697574671957841159273934
#now convert to int
my_key = int_to_bytes(KEY,16)
my_string = 'extraterrestrial'
my_block_string = bytearray(my_string, 'UTF-8')
print("myblocksring is "+str(my_block_string))
#block - use a string of 16 bytes = "extraterrestrial" convert with 'ncode' which gives you a bytes object
def modular_exponentiation(x, d, n):
    if d == 0:
        return 1
    elif d % 2 == 0:
        y = modular_exponentiation(x, d // 2, n)
        return (y * y) % n
    else:
        return (modular_exponentiation(x, d-1, n) * x) % n

d = 2308306403379357006885875459702320825751738549680509667562253133998222902384094571531526409029206061
d = int_to_bytes(d,16)
n = 2885383004224196258607344324627901032189673187100744520880610584866823150514523262548807361988920727
n = int_to_bytes(n,16)
pad_file = 400005664837268133036139368185266511135317756598842038602332216576214181294418404302636414762355453
my_block_string = bytearray(pad_file)
def decrypt_pad(pad_file, d, n, block_size):
    #my_key = int_to_bytes(d,block_size)
    my_string = pad_file
    my_byte_array = bytearray()
    print("Your encrypted text from pad file is: " + str(my_string))
    decrypted_char = modular_exponentiation(my_string,d,n)
    print("decrypted char is: "+str(decrypted_char))
    print(hex(decrypted_char))

    return my_byte_array
    #decrypt this using your private key
    #it will be obvious that you've decrypted it
    # YOU FILL THIS IN.


print(decrypt_pad(pad_file,d,n,16))

#conceptual explanation of RSA encryption
#p,q order of 10^300
# pq=N (will be a bunch of bits which will then be translated into binary then ASCII
# e = Z_N 'co=prime', lets say N=10, = {1,3,7,9}
# therefore e = 4
# message M- how do you encrypt? want to make it C.
# "you are a student" --> binary --> ASCII --> bits (looks like b/'0x7/n   /t') and then this string is raised to N
# M^e(mod(N)) (this is M-->C)
# for C-->M do C^d(mod(N))

#follow the order of functions that Cormen gives you

#def decrypt_pad(pad_file,d,n,block size)
