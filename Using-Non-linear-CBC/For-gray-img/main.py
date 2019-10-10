from utils import convertNumToBinary, convertBinaryToNum, convertCharToBinary, splitIntoParts, mergeParts
from CBC import applyCBC
import cv2
import numpy

# ---Two DES keys and initial vector---
print("-" * 64)
# read the first des key
k1 = input("Enter the first key: ")
# check if key is not 8 characters
if(len(k1) != 8):
    print("\nYou need to enter a string of 8 characters!")
    exit(0)
# convert the text string into binary string
deskey1 = convertCharToBinary(k1)
# read the second des key
k2 = input("Enter the second key: ")
# check if key is not 8 characters
if(len(k2) != 8):
    print("\nYou need to enter a string of 8 characters!")
    exit(0)
# convert the text string into binary string
deskey2 = convertCharToBinary(k2)
# read the initial vector
iv = input("Enter the initial vector: ")
# check if key is not 8 characters
if(len(iv) != 16):
    print("\nYou need to enter a string of 8 characters!")
    exit(0)
# convert the text string into binary string
initVect = convertCharToBinary(iv)
ENCRYPT = "ENCRYPT"
DECRYPT = "DECRYPT"
print("-" * 64)

# ---Read the image---
imgPath = input("Enter the image path: ")
try:
    img = cv2.imread(imgPath, 0)
except:
    print("Invalid path!")
    exit(0)
print("-" * 64)

# ---Encryption---
# get the width and height of the image
w, h = img.shape
print("Encrypting...")
# iterate through each row
for i in range(h):
    # convert the list into a binary string
    pltxt = convertNumToBinary(img[i])
    # apply the CBC for the binary string in encryption mode
    cipher = applyCBC(pltxt, deskey1, deskey2, initVect, ENCRYPT)
    # convert the binary string into number list and create a list of type uint8 for the encrypted binary string
    cipherList = numpy.array(convertBinaryToNum(cipher), dtype=numpy.uint8)
    # replace the original row value with the new ciphered value
    img[i] = cipherList
print("Encryption done!")
# show the encrypted image
cv2.imshow("encrypted image", img)
cv2.waitKey(0)
# save the encrypted image to this directory
cv2.imwrite("./encrypted.png", img)
print("Saved the encrypted image into current directory!")
cv2.destroyAllWindows()

print("-" * 64)

# ---Decryption---
# read the encrypted image
imgPath = "./encrypted.png"
img = cv2.imread(imgPath, 0)
# get the width and height of the image
w, h = img.shape
print("Decrypting...")
# iterate through each row
for i in range(h):
    # convert the list into a binary string
    cipher = convertNumToBinary(img[i])
    # apply the CBC for the binary string in decryption mode
    decrypted = applyCBC(cipher, deskey1, deskey2, initVect, DECRYPT)
    # convert the binary string into number list and create a list of type uint8 for the decrypted binary string
    decryptedList = numpy.array(convertBinaryToNum(decrypted), dtype=numpy.uint8)
    # replace the original row value with the new decrypted value
    img[i] = decryptedList
print("Decryption done!")
# show the decrypted image
cv2.imshow("decrypted image", img)
cv2.waitKey(0)
# save the decrypted image to this directory
cv2.imwrite("./decrypted.jpg", img)
print("Saved the decrypted image to current directory!")
cv2.destroyAllWindows()

print("-" * 64)