from stack import MyStack


def reversefile(filename):
    s = MyStack()
    orig = open(filename)
    for line in orig:
        s.push(line, rstrip('\n'))
    orig.close()