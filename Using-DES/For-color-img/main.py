import cv2
import numpy
from processChannel import applyDESOnAChannel

# ---DES Key---
# create a des key using a string with 8 characters
print("-" * 90)
k = input("Enter the key: ")
# check if key is not 8 characters
if(len(k) != 8):
    print("\nYou need to enter a string of 8 characters!")
    exit(0)
# convert the text string into binary string
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
    r = applyDESOnAChannel(r, h, k, ENCRYPT)
    g = applyDESOnAChannel(g, h, k, ENCRYPT)
    b = applyDESOnAChannel(b, h, k, ENCRYPT)
    print("Encryption done!")
elif(ch == 2):
    # apply DES in decryption mode on each of the color spaces
    print("Decrypting...")
    r = applyDESOnAChannel(r, h, k, DECRYPT)
    g = applyDESOnAChannel(g, h, k, DECRYPT)
    b = applyDESOnAChannel(b, h, k, DECRYPT)
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