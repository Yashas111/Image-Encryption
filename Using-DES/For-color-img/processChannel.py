from utils import convertNumToBinary, convertBinaryToNum, convertCharToBinary, splitIntoParts, mergeParts
from DES import applyDES
import cv2
import numpy

def applyDESOnAChannel(channel, h, deskey, mode):
    # convert the key to binary string
    deskey = convertCharToBinary(deskey)
    # iterate through row
    for i in range(h):
        # first split the row values into groups of 8
        channelListIntoParts = splitIntoParts(channel[i], 8)
        # then iterate through each group
        for k in range(len(channelListIntoParts)):
            # convert the list into a binary string
            pltxt = convertNumToBinary(channelListIntoParts[k])
            # apply the DES for the binary string in encryption mode
            cipher = applyDES(pltxt, deskey, mode)
            # convert the binary string into number list and create a list of type uint8 for the encrypted binary string
            cipherList = numpy.array(convertBinaryToNum(cipher), dtype=numpy.uint8)
            # replace the original value with the cipher value
            channelListIntoParts[k] = cipherList
        # replace the original row value with the new ciphered value
        channel[i] = mergeParts(channelListIntoParts)
    # return the channel
    return channel