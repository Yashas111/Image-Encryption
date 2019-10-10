import numpy

# a method to split the text into equal n parts
def splitIntoParts(text, n):
    return [text[i:i+n] for i in range(0, len(text), n)]

# a method to merge the parts
def mergeParts(l):
    myList = numpy.array(l[0], dtype=numpy.uint8)
    for i in range(1, len(l)):
        myList = numpy.concatenate((myList, l[i]), axis = 0)
    return myList

# a method to convert the text string into binary string
def convertCharToBinary(text):
    textToBin = ""
    for c in text:
        textToBin += bin(ord(c))[2:].zfill(8)
    return textToBin

# a method to convert the binary string into a text string
def convertBinaryToChar(binaryText):
    text = ""
    textIntoParts = splitIntoParts(binaryText, 8)
    for c in textIntoParts:
        text += chr(int(c, 2))
    return text

# a method to convert a list of numbers into a binary string
def convertNumToBinary(numList):
    binaryText = ""
    for n in numList:
        binaryText += bin(n)[2:].zfill(8)
    return binaryText

# a method to convert the binary string into a list of numbers
def convertBinaryToNum(binaryText):
    numList = []
    binaryTextIntoParts = splitIntoParts(binaryText, 8)
    for b in binaryTextIntoParts:
        numList.append(int(b, 2))
    return numList

# a method to perform xor with zfill number of bits in the result
def xor(x, y, zfill):
    return bin(int(x, 2) ^ int(y, 2))[2:].zfill(zfill)