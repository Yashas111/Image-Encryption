from utils import convertNumToBinary, convertBinaryToNum, convertCharToBinary, splitIntoParts, mergeParts
from CBC import applyCBC
import cv2
import numpy

def applyCBCOnAChannel(channel, h, deskey1, deskey2, initVect, mode):
    # convert the keys and plain text to binary string
    deskey1 = convertCharToBinary(deskey1)
    deskey2 = convertCharToBinary(deskey2)
    initVect = convertCharToBinary(initVect)
    # iterate through each row
    for i in range(h):
        # convert the list into a binary string
        pltxt = convertNumToBinary(channel[i])
        # apply the CBC for the binary string in the given mode
        cipher = applyCBC(pltxt, deskey1, deskey2, initVect, mode)
        # convert the binary string into number list and create a list of type uint8 for the encrypted binary string
        cipherList = numpy.array(convertBinaryToNum(cipher), dtype=numpy.uint8)
        # replace the original row value with the new ciphered value
        channel[i] = cipherList
    return channel