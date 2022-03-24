import re


def reverse(value):
    if value == 0:
        return 1
    else:
        return 0


def BracketsPairing(str, pos):
    pair = 1
    while pair != 0:
        pos = pos + 1
        if str[pos] == '(':
            pair = pair + 1
        elif str[pos] == ')':
            pair = pair - 1
    return pos


def operatorCalculation(previous_value, operator, current_value):  # b默认为-1时，表示是单操作符号' ! '
    if operator == '&':
        return previous_value * current_value

    elif operator == '|':
        if previous_value == 0 and current_value == 0:
            return 0
        else:
            return 1

    elif operator == '>':
        if previous_value == 1 and current_value == 0:
            return 0
        else:
            return 1

    elif operator == '=':
        if previous_value != current_value:
            return 0
        else:
            return 1

    else:
        # print("there is no such operator")
        raise IOError


def operation(str, dictionary):
    pos = 0
    length = len(str)
    previous_value_exist = False
    previous_value = 100
    current_value = 100
    operator = '0'
    while pos < length:
        ch = str[pos]

        # character at current position is a parameter
        if ch in dictionary:
            current_value = dictionary[ch]

        # character at current position is '('
        elif ch == '(':
            current_value = operation(str[pos + 1:BracketsPairing(str, pos)], dictionary)
            pos = BracketsPairing(str, pos)

        # character at current position is '!'
        elif ch == '!':

            # Two consecutive '!' are not allowed
            if str[pos + 1] == '!':
                raise IOError

            # next character of '!' is '('
            elif str[pos + 1] == '(':
                current_value = reverse(operation(str[pos + 1:BracketsPairing(str, pos + 1) + 1], dictionary))
                pos = BracketsPairing(str, pos + 1)

            # next character of '!' is the parameter
            else:
                pos += 1
                current_value = reverse(dictionary[str[pos]])

        # character at current position is an operator
        elif ch in "&|!>=":

            # no parameter between two operators / before the operator
            if operator != '0' or not previous_value_exist:
                raise IOError

            # no parameter after the operator
            elif previous_value_exist and pos == length - 1:
                raise IOError

            else:
                operator = ch

        # no operator between two parameters
        if previous_value_exist and operator == '0' and current_value != 100:
            raise IOError

        # next character of '!' is '('
        elif not previous_value_exist:
            if operator != '0':
                raise IOError
            previous_value = current_value
            current_value = 100
            previous_value_exist = True

        elif operator != '0' and current_value != 100:
            previous_value = operatorCalculation(previous_value, operator, current_value)

            # initialize the variable to be used further
            current_value = 100
            operator = '0'

        # next position
        pos += 1

    return previous_value


def Arrangement(str, dictionary):
    global original_str
    idx = len(str) - 1
    truth_table = []
    for i in range(pow(2, len(str))):
        result = operation(original_str, dictionary)
        # print(dictionary, ": ", result)

        lst = []
        for key in dictionary:
            lst.append(dictionary[key])
        lst.append(result)
        truth_table.append(lst)

        pos = idx
        while pos >= 0:
            if dictionary[str[pos]] == 1:
                dictionary[str[pos]] = 0
                pos -= 1
            else:
                dictionary[str[pos]] = 1
                break
    return truth_table


def AddToDictionary(str):
    dictionary = {}
    for i in range(len(str)):
        ch = str[i]
        if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
            dictionary[ch] = 0
        else:
            raise IOError

    return dictionary


def RemoveDuplication(text):
    text = re.sub(r'[{}]+'.format('!&|>=()'), '', text)
    return text.strip()


def ExtractLetters(s):
    s = RemoveDuplication(s)
    str = ""
    for i in range(len(s)):
        if s[i] not in str:
            str += s[i]
    return str


def CheckBrackets(str):
    pair = 0

    for i in range(len(str)):
        if str[i] == '(':
            pair += 1
        if str[i] == ')':
            pair -= 1
        if pair < 0:
            raise IOError

    if pair != 0:
        raise IOError


def generate(str):
    global original_str

    str = str.replace(" ", "")

    original_str = str

    CheckBrackets(str)

    str = ExtractLetters(str)

    dictionary = AddToDictionary(str)

    truth_table = Arrangement(str, dictionary)

    lst = []
    for i in range(len(str)):
        lst.append(str[i])

    lst.append(original_str)
    truth_table.insert(0, lst)

    return truth_table


original_str = ""

# s = "A = !B & (C > A)"
# str = s.replace(" ", "")
# original_str = str
#
# CheckBrackets(str)
#
# str = ExtractLetters(str)
#
# dictionary = AddToDictionary(str)
#
# Arrangement(str, dictionary)
