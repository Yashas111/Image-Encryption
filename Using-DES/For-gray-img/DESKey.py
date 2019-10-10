# key = "0001001100110100010101110111100110011011101111001101111111110001"

#Initial permut made on the key
CP_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

#Permut applied on shifted key to get Ki+1
CP_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]

#Matrix that determine the shift for each round of keys
SHIFT = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

def generateKeys(key):
    # to store the array of keys
    keys = []
    key_list = [x for x in key]
    # Applying the initial permuatation or something like that
    key_56_bits = [key_list[x - 1] for x in CP_1]

    for shift in SHIFT:
        key_first, key_second = key_56_bits[:28], key_56_bits[28:]
        key_first = key_first[shift:] + key_first[:shift]
        key_second= key_second[shift:] + key_second[:shift]
        key_56_bits = key_first + key_second
        # to store individual key
        k = []
        k = [key_56_bits[x - 1] for x in CP_2]
        keys.append(''.join(k))
        
    return keys   
    #return [k1, k2, k3, ..., k16]

# keys = generateKeys(key)
# print(keys)
