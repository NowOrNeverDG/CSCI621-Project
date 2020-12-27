# Set stack property
class Stack(object):
    # Initializes the stack to an empty list
    def __init__(self):
        self.items = []

    # Whether the stack is empty and returns a Boolean value
    def is_empty(self):
        return self.items == []

    # return top element of stack
    def peek(self):
        return self.items[len(self.items) - 1]

    # return size of stack
    def size(self):
        return len(self.items)

    # push element into stack
    def push(self, item):
        self.items.append(item)

    # pop element from stack
    def pop(self, item):
        return self.items.pop()


def error():
    print("error occur")


def keyInList(k, l):
    return bool([True for i in l if k in i.values()])


def stringBuilder(str):
    for i in str:
        if i.isdigit():
            str = str.replace(i, "d")
    return str


# Matrix builder system
# method to add value
def addtwodimdict(thedict, key_a, key_b, val):
    if key_a in thedict:
        thedict[key_a].update({key_b: val})
    else:
        thedict.update({key_a: {key_b: val}})


# To easy to looking for, there is replace elist by l, elist' by L, e' by E, n' by N. Make sure every simbol include
# only one letter
def setMatrix():
    matrix = {"d": {"l": "eL", "e": "nE", "n": "dN", "N": "n"},
              "^": {"E": "^e", "N": ""},
              ",": {"L": ",l", "E": "", "N": ""},
              "$": {"L": "", "E": "", "N": ""}}
    return matrix


def outputBuilder(y1, mxy):
    if y1 == "l":
        y1 = "elist"
    elif y1 == "L":
        y1 == "elist'"
    elif y1 == "E":
        y1 = "e'"
    elif y1 == "N":
        y1 = "n'"

    for i in mxy:
        if i == "l":
            mxy = mxy.replace("l", "elist")
        elif i == "L":
            mxy = mxy.replace("L", "elist'")
        elif i == "E":
            mxy = mxy.replace("E", "e'")
        elif i == "N":
            mxy = mxy.replace("N", "n'")
    return y1 + "->" + mxy


if __name__ == '__main__':
    # Let T$ be the input string followed by a $.
    print("input your string(like 2^3^4,15,20^2)")
    inputString = raw_input()
    inputString = stringBuilder(inputString)
    inputStr_list = list(inputString)
    inputStr_list.insert(len(inputStr_list), "$")
    # Set ip to point to the first symbol of T$.
    ip = 0  # list index
    matrix = setMatrix()
    stack = Stack()
    stack.push("$")
    stack.push("l")

    while inputStr_list[ip] != "$":
        x = inputStr_list[ip]
        y = stack.peek()

        if y == inputStr_list[ip]:
            stack.pop(stack.peek())
            inputStr_list.remove(inputStr_list[0])
        elif x in matrix:
            if y in matrix[x]:
                # print y + " -> " + matrix[x][y]
                print outputBuilder(y, matrix[x][y])
                stack.pop(y)

                for ele in reversed(matrix[x][y]):
                    stack.push(ele)
        else:
            error()
