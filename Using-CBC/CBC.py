from DES import applyDES
from utils import xor, splitIntoParts

ENCRYPT = "ENCRYPT"
DECRYPT = "DECRYPT"

def applyCBC(text, DESKey, initialVector, mode):
    # convert all parameters into binary
    # text = convertToBinary(text)
    # DESKey = convertToBinary(DESKey)
    # initialVector = convertToBinary(initialVector)
    feedback = initialVector

    # divide the text into blocks each of size 64 bits
    textIntoParts = splitIntoParts(text, 64)

    result = []

    for i in range(len(textIntoParts)):
        if(mode == ENCRYPT):
            res = xor(feedback, textIntoParts[i], 64)
            feedback = applyDES(res, DESKey, ENCRYPT)
            result.append(feedback)
        else:
            desres = applyDES(textIntoParts[i], DESKey, DECRYPT)
            res = ""
            if(i == 0):
                res = xor(desres, initialVector, 64)
            else:
                res = xor(desres, textIntoParts[i - 1], 64)
            result.append(res)
    # convert the binary back to characters
    return ("".join(result))