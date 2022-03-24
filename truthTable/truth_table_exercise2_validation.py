import re


def exercise2_validation(str, values):

    # remove space
    str = str.replace(" ", "")

    # remove symbol
    str = re.sub(r'[{}]+'.format('!&|>=()'), '', str).strip()

    # remove duplication
    s = ""
    for i in range(len(str)):
        if str[i] not in s:
            s += str[i]
    
    if len(s) != len(values):
        raise IOError
    
    return True

