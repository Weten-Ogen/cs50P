from stack import MyStack

# checks if all delimiters are matched
def delimit(txt):
    lefty = "([{"
    righty = ")]}"
    s = MyStack()
    for c in txt:
        if c in lefty:
            s.push(c)
        elif c in righty:
            if s.is_empty():
                return False
            if righty.index(c) != lefty.index(s.pop()):
                return False
    return s.is_empty()

string = '[(5 + x) - (6 + y)]'
print(delimit(string))


