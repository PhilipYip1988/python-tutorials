import pickle
def float2binaryfloat(f1):
    hex1 = pickle.dumps(f1).hex()[24:40]
    sign1 = bin(int('0x' + hex1, base=16)).removeprefix('0b').zfill(64)[0]
    biasedexponent = bin(int('0x' + hex1, base=16)).removeprefix('0b').zfill(64)[1:12]
    mantissa = bin(int('0x' + hex1, base=16)).removeprefix('0b').zfill(64)[12:]

    if sign1 == '0':
        sign2 = '+'
    else:
        sign2 = '-'

    exponent2 = int(biasedexponent, base=2) - 1023
    
    if exponent2 < 1:
        absolute = '0.' + '0' * abs(exponent2 + 1) + '1' + mantissa
        result = sign2 + absolute
    elif exponent2 > 1:
        mantissa2 = '1' + mantissa
        absolute = mantissa2[:exponent2+1] + '.' + mantissa2[exponent2+1:]
        result = sign2 + absolute
    else:
        mantissa2 = '1.' + mantissa
        result = sign2 + mantissa2
    return result