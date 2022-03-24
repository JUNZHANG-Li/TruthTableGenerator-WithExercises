import re


def reverse(value):
    if value == 0:
        return 1
    else:
        return 0


def BracketsPairing(str, pos):
    pair = 1  # 左括号的数目
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
            current_value = operation(str[pos+1:BracketsPairing(str, pos)], dictionary)
            pos = BracketsPairing(str, pos)

        # character at current position is '!'
        elif ch == '!':

            # next character of '!' is '('
            if str[pos+1] == '(':
                current_value = reverse(operation(str[pos+1:BracketsPairing(str, pos+1)+1], dictionary))
                pos = BracketsPairing(str, pos+1)

            # next character of '!' is the parameter
            else:
                pos += 1
                current_value = reverse(dictionary[str[pos]])

        # character at current position is an operator
        else:
            operator = ch

        # next character of '!' is '('
        if not previous_value_exist:
            if operator != '0':
                raise IOError
            previous_value = current_value
            current_value = 100
            previous_value_exist = True

        # elif previous_value_exist and current_value == 100:
        #     raise IOError

        elif operator != '0' and current_value != 100:
            previous_value = operatorCalculation(previous_value, operator, current_value)

            # initialize the variable to be used further
            current_value = 100
            operator = '0'

        # next position
        pos += 1

    return previous_value


def Arrangement(dictionary):
    global original_str
    truth_table = []

    lst = []
    for key in dictionary:
        lst.append(key)
    truth_table.append(lst)

    lst = []
    for key in dictionary:
        lst.append(dictionary[key])
    truth_table.append(lst)

    return truth_table


def AddToDictionary(str, values):
    dictionary = {}
    for i in range(len(str)):
        ch = str[i]
        if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
            dictionary[ch] = int(values[i])
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


def generate_exercise2(str, values):
    global original_str

    str = str.replace(" ", "")

    original_str = str

    CheckBrackets(str)

    str = ExtractLetters(str)

    dictionary = AddToDictionary(str, values)

    table = Arrangement(dictionary)

    result = operation(original_str, dictionary)

    return [result, table]


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
