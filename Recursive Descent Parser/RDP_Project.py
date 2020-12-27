input_line = ""
input_list = {}
input_index = -1
next_symbol = ''
succeeded = True
d_value = 0
e_value = 0
eof = False


def getInputLine():
    print("Enter your line(like line:2^2^3,15,20^3):")
    return raw_input()


def getEachSymbol():
    global input_list
    input_list = []
    for i_word in input_line:
        input_list += i_word
    return input_list


def getNextSymbol():
    global next_symbol, input_list, input_index
    input_index = input_index + 1
    if not EOL():
        next_symbol = input_list[input_index]
    #print("GetNextSymbol-next_symbol: " + next_symbol + " Index: " + str(input_index))  # Test

def EOL():
    if input_index < len(input_list):
        #print("EOL is False")
        return False
    else:
        #print ("EOL is True")
        return True


def e():
    n_value = 0
    n_value = n(n_value)
    if succeeded:
        #print ("e()-e_value: " + str(n_value))
        eTail(n_value)


def elist():
    global succeeded
    e()
    if succeeded:
        elistTail()


def elistTail():
    global succeeded, e_value
    eolstate = EOL()
    #print ("elistTail-EOL is: " + str(eolstate))    #Test
    if eolstate:  # EOL
        print str(e_value)
    else:
        if next_symbol == ',':
            print str(e_value)
            getNextSymbol()
            elist()
        else:
            succeeded = False

def eTail(n_value):
    global e_value, succeeded
    eolstate = EOL()
    if next_symbol != "," and not eolstate:  # EOL
        if next_symbol == "^":
            #print ("is eTail Func")
            getNextSymbol()
            e()
            #print ("e_value:" + str(e_value) + "n_value" + str(n_value))
            e_value = n_value ** e_value
            #print ("e_value: " + str(e_value) + " n_value: " + str(n_value) + " eTail-e_value: " + str(e_value))
        else:
            succeeded = False
    else:

        e_value = n_value
        #print ("e_value = n_value= " + str(e_value) + "hhhhhhhh")


def n(n_value):
    d()
    if succeeded:
        n_value = n_value * 10 + d_value
        state = nTail(n_value)
        if state != "Nonumber":
            n_value = state
    #print ("n_value changed = " + str(n_value))
    return n_value


def nTail(n_value):
    eolstate = EOL()
    if next_symbol != '^' and next_symbol != ',' and not eolstate:
        n_value = n(n_value)
        #print("nTail-n_value: " + str(n_value))
        return n_value
    return "Nonumber"


def d():
    global next_symbol, d_value, succeeded
    if next_symbol.isdigit():
        d_value = int(next_symbol)
        #print ("d-d_value: " + str(d_value))

        getNextSymbol()
    else:
        succeeded = False


if __name__ == '__main__':
    # execution
    while not eof:
        succeeded = True
        input_line = getInputLine()
        input_list = getEachSymbol()
        getNextSymbol()
        elist()
        if succeeded:
            print (":) succeeded")
        else:
            print (":( failure")