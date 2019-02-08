import codecs


    #Hex to base64
hex = input('Enter an integer in HEX: ')
b64 = codecs.encode(codecs.decode(hex, 'hex'), 'base64').decode()
print('Hex: ' + hex + '\n' + 'Base64: ' + b64)



#10000000000002ae
