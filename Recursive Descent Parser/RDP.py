insert = []
nextsymbol = ""
EOF = False
succeed = True
inputindex = 0
d_value = 0
e_value = 0


def getInputLine():
    global userInput
    userInput = input("Enter input line: ")


def getInput():
    global insert
    print("Enter your formula or quit to end: ")
    insert = raw_input()
    #2^2print("This is your insert: ", insert)
        
        
def getnextsymbol(): 
    global inputindex, insert, EOF, nextsymbol

   
    if inputindex <= len(insert) - 1:
            nextsymbol = insert[inputindex]
            inputindex += 1        
    else:
        EOF = True
        return
  
        
       


def elist():
    e()
    if succeed:
        elist_tail()


def elist_tail(): 
    global EOF, insert, succeed
    if EOF:
        print(EOF)
        print(e_value)
    else:
        if nextsymbol == ",":
            #print(e_value)
            getnextsymbol()
            elist()
        else:
            succeed = False
    

def e():
    n_value = 0
    n_value = n(n_value)
    
    if succeed:
        etail(n_value)
        
def etail(n_value):
    global inputindex, insert, e_value, succeed
    if not (nextsymbol == "," or EOF):
        if nextsymbol == "^":
            getnextsymbol()
            e()
            e_value = n_value ** e_value
            #print(e_value)
        else:
            succeed = False
    else:
        e_value = n_value
        #print(e_value)

def n(n_value):
    d()
    if succeed:
        n_value = n_value*10 + d_value
        return ntail(n_value)

def ntail(n_value):
    global inputindex, insert, succeed
    if not ((nextsymbol == "^" or nextsymbol == ",") or EOF):
        n_value = n(n_value)
    return n_value

def d():
    global d_value, nextsymbol, succeed
    if nextsymbol.isdigit():
        d_value = int(nextsymbol)
        getnextsymbol()
    else:
        succeed = False

if __name__ == '__main__':
    while not EOF :
        succeed = True
        getInput()
        if insert == 'quit':
            break
        else:
            getnextsymbol()
            elist()
            if succeed:
                print("good job")
            else:
                print("no no try again")
