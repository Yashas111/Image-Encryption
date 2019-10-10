import cv2
import numpy
from processChannel import applyCBCOnAChannel

# ---DES Keys and initial vector---
# read the first deskey
print("-" * 90)
deskey1 = input("Enter the frist key: ")
# check if key is not 8 characters
if(len(deskey1) != 8):
    print("\nYou need to enter a string of 8 characters!")
    exit(0)
# read the second deskey
deskey2 = input("Enter the second key: ")
# check if key is not 8 characters
if(len(deskey2) != 8):
    print("\nYou need to enter a string of 8 characters!")
    exit(0)
# read the initial vector
initVect = input("Enter the inital vector: ")
# check if key is not 8 characters
if(len(initVect) != 16):
    print("\nYou need to enter a string of 16 characters!")
    exit(0)
print("-" * 90)

ENCRYPT = "ENCRYPT"
DECRYPT = "DECRYPT"

# ---Read the image---
imgPath = input("Enter the image path: ")
try:
    img = cv2.imread(imgPath, 1)
    # get the width, height, and number of channels in the image
    h, w, channel = img.shape
    # split the image into r, g, b color spaces
    r, g, b = cv2.split(img)
except:
    print("Invalid path!")
    exit(0)

print("-" * 90)
print("1-ENCRYPT \n2-DECRYPT")
ch = int(input("Enter you choice (1/2): "))
print("-" * 90)

if(ch == 1):
    # apply DES in encryption mode on each of the color spaces
    print("Encrypting...")
    r = applyCBCOnAChannel(r, h, deskey1, deskey2, initVect, ENCRYPT)
    g = applyCBCOnAChannel(g, h, deskey1, deskey2, initVect, ENCRYPT)
    b = applyCBCOnAChannel(b, h, deskey1, deskey2, initVect, ENCRYPT)
    print("Encryption done!")
elif(ch == 2):
    # apply DES in decryption mode on each of the color spaces
    print("Decrypting...")
    r = applyCBCOnAChannel(r, h, deskey1, deskey2, initVect, DECRYPT)
    g = applyCBCOnAChannel(g, h, deskey1, deskey2, initVect, DECRYPT)
    b = applyCBCOnAChannel(b, h,deskey1, deskey2, initVect, DECRYPT)
    print("Decryption done!")
else:
    print("Invalid choice!")
    exit(0)
    print("-" * 90)
print("-" * 90)

# merge the r, g, b color spaces back to form a new encrypted image
newImg = cv2.merge((r, g, b))

# read a name for the resultant image
print("Note: Don't provide an extension. Image will be automatically saved with extension .png")
newImgName = input("Enter the name for the resultant image : ")
print("-" * 90)

# write the new image to storage
print("Saving...")
cv2.imwrite("./" + newImgName + ".png", newImg)
print("Resultant image saved!")
print("-" * 90)

# show the resultant image
cv2.imshow("Result", newImg)
cv2.waitKey(0)
cv2.destroyAllWindows()