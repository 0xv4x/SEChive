# hexToB64
# Feel free to use this, compiled from a few different sources
# Python3

import codecs


    #Hex to base64
hex = input('Enter an integer in HEX: ')
b64 = codecs.encode(codecs.decode(hex, 'hex'), 'base64').decode()
print('Hex: ' + hex + '\n' + 'Base64: ' + b64)
